//boolean variable to check if the user wants to try again at the end of the algorithm
START
SET runagain to TRUE
WHILE (runagain is TRUE)

 //get the user genre input and validate it 
	WRITE “Pick one of the following genres you would like to read: Fantasy, Classics, Fiction, or Young Adult. Write End to exit.” 
	GET user_genre 
	SET user_genre to TO_LOWER(user_genre)

	WHILE (user_genre is not "fantasy” AND user_genre is not "classics" AND user_genre is not "fiction" AND user_genre is not "young adult" AND user_genre is not "end")
		WRITE "Invalid input, please try again. Pick a genre from Fantasy/Classics/Fiction/Young Adult or write End to exit." 
		GET user_genre
		SET user_genre to TRIM(TO_LOWER(user_genre))
	ENDWHILE

	IF (user_genre is "end")
		SET runagain to FALSE
		EXIT PROGRAM
	ENDIF

//get user input about time available and speed of reading
	WRITE "How many days do you have available to read your next book?"
	GET timeframe 
    WHILE (timeframe is not a number OR timeframe <= 0)
    	WRITE "Please enter a positive number of days."
    	GET timeframe
	ENDWHILE
	
	WRITE “How many pages a day do you read?” 
	GET speed 
	WHILE (speed is not a number OR speed <= 0)
    	WRITE "Please enter a positive number of pages per day."
    	GET speed
	ENDWHILE


 //load the csv dataset into a books array 
 //filter the books for genre and time constraints into a new array 
	LOAD goodreads_cleaned_fixed.csv as books 
	RETRIEVE all records in books
	CREATE empty array Filtered
	SET index to 0
	
	WHILE (index < length(books))
		SET book_genre to TO_LOWER(books[index].genre)
		IF (book_genre is user_genre)
			SET days to books[index].page_count/speed
			IF (days <= timeframe) 
				SET books[index].days to days
				ADD books[index] to Filtered
			ENDIF
		ENDIF
		SET index to index + 1
	ENDWHILE

	IF (Filtered is EMPTY)
		WRITE "None of the”, user_genre, “books could be read within the specified time limit at the specified speed.”
	ELSE
     //find the highest rated 10 of them to display final recommendations (ratings descending and time they take ascending)
		SET firstUnsorted to 0
		WHILE (firstUnsorted<=9 AND firstUnsorted < length(Filtered)-1)
			SET indexOfBiggest to firstUnsorted
			SET index to firstUnsorted + 1 
			WHILE (index <= length(Filtered) - 1)
				IF (Filtered[index].average_rating > Filtered[indexOfBiggest].average_rating) OR (Filtered[index].average_rating = Filtered[indexOfBiggest].average_rating AND
            Filtered[index].days < Filtered[indexOfBiggest].days)
					SET indexOfBiggest to index
				ENDIF
				SET index to index + 1 		
			ENDWHILE
			SET tempItem to Filtered[firstUnsorted]
			SET Filtered[firstUnsorted] to Filtered[indexofBiggest]
			SET Filtered[indexOfBiggest] to tempItem
			SET firstUnsorted to firstUnsorted + 1 	
		ENDWHILE

	 WRITE "Please see the top-rated ", user_genre, "books that can be read in ",timeframe," days and the number of days they would each take to read: ”
	 	SET index to 0
		WHILE (index < length(Filtered) AND index <= 9)
			SET rank to index+1
			WRITE rank,". ", Filtered[index].title, Filtered[index].author, Filtered[index].average_rating, Filtered[index].year, Filtered[index].days, ENDLINE
			SET index to index + 1
		ENDWHILE	
	ENDIF 
	
	WRITE “Would you like to try again? Write yes or no”
		GET user_runagain 
		SET user_runagain to TO_LOWER(user_runagain)
	WHILE (user_runagain is not "yes" AND user_runagain is not "no")
		WRITE "Invalid input, please write yes or no." 
		GET user_runagain
		SET user_runagain to TO_LOWER(user_runagain)
	ENDWHILE 

	IF (user_runagain is "no")
		SET runagain to FALSE 	
	ENDIF
	
ENDWHILE

END
