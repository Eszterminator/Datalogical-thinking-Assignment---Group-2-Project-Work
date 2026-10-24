#python
import pandas as pd

#read in the data file as dataframe 
books = pd.read_csv("goodreads.csv")

#get the user input
print(“Pick one of the following genres you would like to read: Fantasy, Crime, General Fiction, Young Adult”)
user_genre = input()
speed = int(input(“How many pages a day do you read?”))
#ADD HERE A LINE ABOUT CHECKING WHETHER IT IS VALID INPUT FROM THE ONES ABOVE 


#select the ones where the genre matches user input 
filtered_genre = books[books[“genre”] == user_genre]


#create speed of reading column, first copying dataframe before modying 
filtered_speed=filtered_genre.copy()
filtered_speed[“days”] = (filtered_speed[“page_count”]/speed)


#sort the filtered list by the avg_ratings 
Sorted_books = filtered_speed.sort_values(by = ”avg_rating”, ascending = false)
top_10 = sorted_books.head(10)
print("Please see the top 10 rated ", user_genre, "books , and the number of days they would take to read at ", speed, " pages read per day: ", top_10)



#show books that can be read under time limit from the genre list above 
print(“How many days do you have to read your next book?”)
timeframe = float.input() 

#first i’ll create a darataframe where they are sorted ascending by days they would take to read, so when i go through them checking which fits the time limit i can stop display them in growing time order and stop when reach max 
#i am also sorting them by avg_rating descending, so they still display as top 

Sorted_books_days = filtered_speed.sort_values(by =[“avg_rating”, ”days”], ascending = [false, true])

fits_time = true 
index = 0
Count = 0
Print (“The following ", user_genre, " books can be read in ”, timelimit, “days, sorted by highest rated:”)
while index<len(sorted_books_days) and fits_time = true
	if sorted_books_days[“days”] <= timeframe
		print sorted_books_days.loc[index] //look up correct formula to print record by index
		index = index+1
	else 
		fits_time = false 

#MAKE THIS INTO A FUNCTION TO BE USED AGAIN BELOW 
 
#an extra step added here to expand algorithm? DISCUSS
#make this author step about all books, not genre specific, or group by genre actually 

print(“Is there a specific author you would like to read? State their name:”)
User_author = str.input()

#filter for the author in all genres 
filtered_author = books[books[“author”] == user_author]

#sort by days ascending and average rating descending 
Sorted_books_author = filtered_author.sort_values(by =[“avg_rating”, ”days”], ascending = [false, true])

fits_time = true 
Author = false
index = 0

While index<len(sorted_books_days) and fits_time is true
If  sorted_books_days[“author”]=author 
#replace by the function from above 
Author = true 
	If sorted_books_days[“days”] <= timeframe
				Print loc.sorted_books_days(index)
			Else 
				Fits_time = false 
Index = index+1

If author = true and fits_time = false
	print(“None of the author’s books can be read in the given timeframe”)
Elseif author = false 
	Print (“No books were found by the author”)



#further ideas:
#Could potentially add an algorithm step where i display the image with the books? 
#Extra: i will add some lines for cleainng in the python and argue that in order to avoid human error etc 
#POTENTIALLY CREATE A FAKE USER DATABASE AND THEN CAN QUERY IT LIKE INPUT USER ID AND WILL GIVE YOU WHAT YOUR AVERAGE RATINGS ARE IN EACH GENRE
#OR ALL THE BOOKS YOU RATED TOP DOWN TO FIND YOUR FAVOURITE?
