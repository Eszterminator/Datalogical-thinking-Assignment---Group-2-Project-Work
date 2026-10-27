//STEP BY STEP PSEUDOCODE TO BREAK DOWN THE ALGORITHM

//boolean variable to check if the user wants to try again at the end of the algorithm
START
SET runagain to TRUE
WHILE (runagain is TRUE)

 //get the user genre input and validate it 

	WRITE “Pick one of the following genres you would like to read: Fantasy, Classics, Fiction, or Young Adult. Write End to exit programme.” 
	GET user_genre 

	WHILE (user_genre is not "Fantasy” AND user_genre is not "Classics" AND user_genre is not "Fiction" AND user_genre is not "Young Adult" AND user_genre is not "End")
		WRITE "Invalid input, please try again. Pick a genre from Fantasy/Classics/Fiction/Young Adult or write End to exit." 
		GET user_genre
	ENDWHILE

	IF (user_genre is "End")
		EXIT PROGRAM
	ENDIF

//get user input about time available and speed of reading

	WRITE "How many days do you have available to read your next book?"
	READ timeframe 
	WRITE “How many pages a day do you read?” 
	GET speed 
 //validate for negative answers
	WHILE (timeframe <= 0 OR speed <= 0)
        WRITE "Please enter positive values for days available and pages read per day (press enter after each)."
        GET timeframe
        GET speed
	ENDWHILE


 //load the csv dataset into a books array 
 //filter the books for genre and time constraints into a new array 

	LOAD goodreads.csv as books 
	RETRIEVE all records in books
	CREATE empty array Filtered
	SET index to 0
	
	WHILE (index < length(books))
		IF (books[index].genre is user_genre)
			SET days to (books[index].num_pages/speed) 
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
     //find the highest rated 10 of them to display final recommendations 
		WRITE "Please see the top 10 rated ", user_genre, "books that can be read in ",timeframe, " days and the number of days they would each take to read: ”
		SET firstUnsorted to 0
		WHILE (firstUnsorted<=9 AND firstUnsorted < length(Filtered)-1)
			SET indexOfBiggest to firstUnsorted
			SET index to firstUnsorted + 1 
			WHILE (index <= length(Filtered) - 1)
				IF (Filtered[index].average_rating > Filtered[indexOfBiggest].average_rating)
					SET indexOfBiggest to index
				SET index to index + 1 		
			ENDWHILE
			SET tempItem to Filtered[firstUnsorted]
			SET Filtered[firstUnsorted] to Filtered[indexofBiggest]
			SET Filtered[indexOfBiggest] to tempItem
			SET firstUnsorted to firstUnsorted + 1 	
		ENDWHILE
	 //and display the top 10 
	 	SET index to 0
		WHILE (index < length(Filtered) AND index <= 9)
			WRITE Filtered[index], ENDLINE
			index = index + 1
		ENDWHILE	
	ENDIF 
	
 //check whether user wants to try another genre
	WRITE “Would you like to pick another genre? Write yes or no”
		GET user_runagain 
	WHILE (user_runagain is not "yes" AND user_runagain is not "no")
		WRITE "Invalid input, please write yes or no" 
		GET user_runagain
	ENDWHILE 

	IF (user_runagain is "no")
		SET runagain to FALSE 	
	ENDIF
ENDWHILE
END