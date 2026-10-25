//STEP BY STEP PSEUDOCODE TO BREAK DOWN THE ALGORITHM

START
SET run_again to TRUE
WHILE (run_again is TRUE)

WRITE “Pick one of the following genres you would like to read: Fantasy, Crime, Fiction, Young Adult” 
READ user_genre 

IF user_genre == "Fantasy" OR "Crime" OR "Fiction" OR "Young Adult"
	break
ELSE
	WRITE "Invalid input, please try again. Pick a genre from Fantasy/Crime/Fiction/Young Adult" 

WRITE “How many pages a day do you read?”
GET speed

1. Select the books in the genre

LOAD csv dataset as books 
RETRIEVE all records
SET books_index to 0
SET genre_found to FALSE
WHILE (books_index < length(books))
    RETRIEVE b_id, title, author, pg_count, genre
    IF genre is user_genre
        DISPLAY B_id, Title, Author, pg_count, genre
        SET genre_found to TRUE    
    SET book_index to book_index + 1

IF genre_found is FALSE
    WRITE "No books found in the selected genre, try another genre:"
    SET user_genre to input 


2. Sort by avg_rating to get top 10
//selection sort, because the way it works I will be able to stop when I found the top 10 

RETRIEVE b_id, title, author, avg_rating, pg_count, genre
SET firstUnsorted to 0 
WHILE (firstUnsorted <= 9 AND firstUnsorted<length)
	SET indexOfBiggest to firstUnsorted
	SET index to firstUnsorted + 1 
	WHILE (index <= length - 1)
		IF(data[index]>data[indexOfBiggest])
			SET indexOfBiggest to index
		SET index to index + 1 
	SET tempItem to data[firstUnsorted]
	SET data[firstUnsorted] to data[indexOfBiggest]
	SET data[indexOfBiggest] to tempItem 
	SET firstUnsorted to firstUnsorted + 1 

3. Divide each page number by speed to get duration
WRITE "Please see the top 10 rated ", user_genre, "books , and the number of days they would take to read at ", speed, " pages read per day: "
DISPLAY book_id, title, author, avg_rating, genre, (page_nb/speed) AS books_genre 
//save as books_genre dataframe


4. ask for the time limit to read the next books and show the books from the list above that fit in it (see python below)

WRITE "How many days do you have available to read your next book?"
READ timeframe 
WRITE "You can read the following books from the top 10 list above in the given timeframe:"

RETRIEVE records in books_genre
SET index to 0 
SET found to FALSE

WHILE (index <= length(books_genre)-1)
	IF (page_nb/speed) <= timeframe
    	WRITE b_id, title, author, genre, page_nb/speed
		SET found to TRUE 
		SET index to index+1

IF found is FALSE
	WRITE "None of the top 10 rated books could be read under the specified time limit at the specified speed, would you like a lower rated recommendation? Write Yes or No"
	SET valid to FALSE
		WHILE (valid is FALSE)
			GET user_decision	
			IF user_decision is not "YES" OR "NO" OR "yes" OR "no" OR "Yes" OR "No"
				WRITE "Invalid input, please write Yes or No" 
			
			ELSEIF 	user_decision is "YES" OR "yes" OR "Yes"
				SET valid to TRUE
				SET index to 0
				SET genre_found to FALSE
				SET time to FALSE
				RETRIEVE all records from books
				WRITE: "The following books in the specified genre can be read in the given timeframe, with the number of days each of them would take: " 
//would be nice to have column names for the days, in python we will 
				WHILE (index < length(books))
//this part will be faster in python using a function: argue this on website 
//also this dataframe of selected genres will be saved in python so we don't have to run the filtering again 	
					IF genre is user_genre AND timeframe <= (pg_count/speed)
						DISPLAY B_id, Title, Author, avg_rating, (pg_count/speed)
						SET genre_found to TRUE
						SET time to TRUE     
					SET book_index to book_index + 1
				IF time is FALSE AND genre_found is FALSE
    				WRITE "None of the books in the selected genre can be read in the given timeframe"								
			
			ELSEIF user_decision is "NO" OR "no" OR "No"
//do i add invalid input here as well? 
				SET valid to TRUE 
				WRITE "Would you like to pick another genre? Write Yes or No"
					GET user_runagain
					IF user_runagain is "Yes" OR "YES" OR "yes"
					BREAK 
					ELSEIF user_runagain is "No" OR "no" OR "NO"
					SET runagain to FALSE 
			ENDIF

END 
