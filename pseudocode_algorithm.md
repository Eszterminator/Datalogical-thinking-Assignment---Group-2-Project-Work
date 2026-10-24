//STEP BY STEP PSEUDOCODE TO BREAK DOWN THE ALGORITHM

START
WRITE “Pick one of the following genres you would like to read: Fantasy, Crime, General Fiction, Young Adult” 
READ user_genre 

IF user_genre == "Fantasy" OR "Crime" OR "General Fiction" OR "Young Adult"
	break
ELSE
	WRITE "Invalid input, please try again. Pick a genre from Fantasy/Crime/General Fiction/Young Adult" 

WRITE “How many pages a day do you read?”
GET speed

1. Select the books in the genre

LOAD csv dataset as books 
RETRIEVE all records
SET books_index to 0
SET genre_found to FALSE
WHILE (books_index < length(books))
    RETRIEVE book_id, title, author, page_num, genre
    IF genre == user_genre
        DISPLAY B_id, Title, Author, page_num, genre
        SET genre_found to TRUE    
    SET book_index to book_index + 1

IF genre_found is FALSE
    WRITE "No books found in the selected genre, try another genre:"
    SET user_genre to input 



2. Sort by avg_rating to get top 10
//selection sort, because the way it works I will be able to stop when I found the top 10 

RETRIEVE book_id, title, author, avg_rating, genre, page_nb
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
DISPLAY book_id, title, author, avg_rating, genre, (page_nb/speed) AS books_genre //save as dataframe

4. ask for the time limit to read the next books and show the books from the list above that fit in it (see python below)
//if using the top 10 rated list, could maybe have an if saying "none of the top 10 rated are readable in the suggested timeframe, would you like to read some other books in the ... genre?" and then add some more from full books list 
//or should it be from the full list of books to begin with?

WRITE "How many days do you have available to read your next book?"
READ timeframe 

RETRIEVE all records (books_genre)
SET index to 0 
WHILE (index <= length (books_genre)
IF (page_nb/speed) <= timeframe
    WRITE b_id, title, author, genre, page_nb/speed



5. is there a specific author you would like to read? gives books by author that fit in the time limit descending order by avg_rating, from all genres 