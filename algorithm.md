//notes during the process - messy, in progress
//22 october: will rewrite the algorithm based on the new dataset found 

Should we limit genre options to some - and the user can click on one of the options: multiple choice, that way we don’t have to have endless rows of data?
    Fantasy 
    Crime 
    General Fiction
    Romance 
    History
Could add an extra cleaning line to the beginning? However already done in stage 1 

Pick a genre you would like to read
Input how many pages a day you read

START
	WRITE “Pick one of the following genres you would like to read: Fantasy, Crime, General Fiction, Romance, History” 
//if we keep full database I can leave this as open question, then do a check IF and display ‘genre not found’ if not one of them 
	GET user_genre 
	WRITE “How many pages a day do you read?”
	GET speed

1. Select the books in the genre

LOAD csv dataset as books //what if i have two: one for books, one for ratings?
RETRIEVE all records
SET books_index to 0
SET genre_found to false 
WHILE books_index < number of books
    RETRIEVE book_id, title, author, page_num, genre
    IF genre == user_genre
        DISPLAY B_id, Title, Author, page_num, genre
        SET genre_found to true    
    SET book_index to book_index + 1

IF genre_found is false
    WRITE "No books found under the genre, try another genre:"
    SET user_genre to input 

//this step is redundant with the new dataset we switched to that has the averages already
2. Will need an average of the ratings for each specific book and a sum of how many users it is from 
    Avg_rating variable created 
    Probably go inside the above if statement (instead of the DISPLAY line)
    Tables used: ratings and books
    Maybe first I select all the ratings that are for books in the right genre - should i just have everything in a mega table for ease? But then it is not normalised 
    I am marking tables with . - books.book_id meaning book_id attribute in books table etc

Set sum=0
Set count = 0
Set index_books =0
Set index_ratings 

WHILE index_books <length-1(books)
    IF (Books.genre == user_genre) 
//I check for each book in books table whether they are the right genre, then i run the book id through the ratings table to find the average rating of the book 
        WHILE index_ratings<length-1(ratings)
            IF (Books.Book_id[index_books] == Ratings.Book_id)
                Sum = sum + rating
                Count = count+1
                index_ratings=index_ratings+1
            ELSE 
                index_ratings=index_ratings+1
// adding a column avg_rating to books table, and trying to fill the value for each book id (unique primary keys), before moving on to the next booktitle  
	    SET avg_rating(book_id[index.books]) = sum/count 
	    SET count_rating(book_id[index.books])=count 
	index_books=index+books+1
	
	
3. Sort by avg_rating to get top 10
//Selection sort (or should it be bubble?)
//At this stage it would be great if i had a table with all the books in the genre category, with their respective average ratings - or would i read in an array of values that include only relevant columns, then display the rest of the attributes based on the book_id when i sorted the avg_rating?

//this sorts them into descending order by avg_rating 
READ book_id, avg_rating  
SET firstunsorted = 0 
WHILE firstunsorted< length-1 
//if i can create a new table (dataframe?) with the selected books it can be the index of that, not the whole books 
	SET index_highestt =firstunsorted
	SET index = firstunsorted +1 
	WHILE (index<=length-1)
		If data[index] < data[indexhighest]
			SET indexhighest = index
		SET index = index + 1 
	SET tempitem to data [firstunsorted]
	SET data[firstunsorted] to data[indexhighest]
	SET data[indexhighest] to tempitem 
	
SET firstunsorted to firstunsorted + 1  

4. Divide each page number by speed to get duration
5. Display: rank, title, author, avg_rating (no of raters),  days-it-will-take-to-read and “Please see below the top 10 rated books in the”> …. <”Genre and how many days each would take to read:”

//then to display the top ten (do i still have ratecount variable?)
SET index to 1
WHILE index <= 10
    SET days = pg_nb/speed
    DISPLAY index, title, author, avg_rating, rate_count, days 
//also add column names here like "Days it would take to read" and "Rank" 




//trying to unite the algorithm into one:

START 
WRITE “Pick one of the following genres you would like to read: Fantasy, Crime, General Fiction, Romance, History” 
GET user_genre() 
WRITE “How many pages a day do you read?”
GET speed()

LOAD csv dataset as books //what if i have two: one for books, one for ratings?
RETRIEVE all records

SET book_index to 0
SET genre_found to false 
WHILE book_index < len(books)
    RETRIEVE book_id, title, author, page_num, genre
    IF (Books(genre) == user_genre) 
        SET genre_found to true
        SET sum = 0
        SET count = 0
        SET days = 0
        WHILE index_ratings<len(ratings)
            IF (Books(Book_id) == Ratings(Book_id))
                Sum = sum + rating
                Count = count + 1
                index_ratings=index_ratings+1
            ELSE 
                index_ratings=index_ratings+1
            ENDIF    
	    ENDWHILE
        SET avg_rating(book_id[book_index]) = sum/count 
	    SET rate_count(book_id[book_index])= count
        SET days = pg_num(book_id[book_index])/speed
        book_index = book_index+1
//this is where i have the row ready with avg_ratin and days, but do i add them all to a new table, or sort them already before i even have the full list? how to keep the data in the variables for avg_rating and days for all the different books as if in a table - can i create a new table with these values plus ones retrieved from the csv? how else do i keep all this extra data i calculated for all the books under the genre so i can sort them later for top 10 
    ELSE
        SET book_index to book_index + 1
    ENDIF
ENDWHILE
IF genre_found = false
    WRITE "No books found under the genre, try another genre:"
    SET user_genre to input()             

    
    
    

#python experimenting
import pandas as pd

#read in the data file as dataframe 
books = pd.read_csv("goodreads.csv")

#get the user input
print(“Pick one of the following genres you would like to read: Fantasy, Crime, General Fiction, Romance, History”)
user_genre = input()
speed = int(input(“How many pages a day do you read?”))

#select the ones where the genre matches user input 
Filtered_genre = books[books[“genre”] == user_genre]

#create speed of reading column, first copying dataframe before modying 
filtered_speed=filtered_genre.copy()
Filtered_speed[“days”] = (filtered_speed[“page_count”]/speed)

#sort the filtered list by the avg_ratings 
Sorted_books = filtered_speed.sort_values(by=”avg_rating”, ascending=false)
Top_10 = sorted_books.head(10)
print(top_10)


