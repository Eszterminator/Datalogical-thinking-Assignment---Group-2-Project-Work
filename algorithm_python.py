import pandas as pd

#read in the data file as dataframe 
books = pd.read_csv(r"C:\Users\madar\Documents\Masters degree Boras uni\datalogical thinking\goodreads.csv")

#to have the program run again, asking for another genre if they want to at the end 
run_again = True
genres = ["Fantasy", "Fiction", "Classics", "Young Adult"]

while(run_again):
#getting the user input and validating it

 print("Pick one of the following genres you would like to read: Fantasy, Fiction, Young Adult, Classics. Write END to exit")
 user_genre = input()
 while user_genre not in genres:
  if user_genre=="end":
   print("Thank you for trying our programme")
   break
  else:
   print("Invalid genre. Please choose from Fantasy, Fiction, Young Adult or Classics")
  user_genre = input()
  
 speed = input("How many pages a day do you read?")
 while not speed.isdigit() or int(speed) <= 0:
   print("Enter a positive number please:")
   speed = input("How many pages a day do you read?")
 speed=int(speed)
 
#select the ones where the genre matches user input 
 filtered_genre = books[books["genre"] == user_genre]

#create a time of reading column, first copying dataframe before modying 
 filtered_speed=filtered_genre.copy()
 filtered_speed["days"] = (filtered_speed["pg_count"]/speed)

#sort the filtered list by the avg_ratings descending and time to read ascending 
 sorted_books = filtered_speed.sort_values(by=["avg_rating", "days"], ascending=[False, True])
 top_10 = sorted_books.head(10)
 print("The top 10 rated",user_genre,"books, and the number of days they would take to read at",speed,"pages per day:")
 print(top_10[["title", "author", "avg_rating", "days"]].to_string(index=False))

#show books that can be read under time limit from the genre list above 
 timeframe = input("How many days do you have available to read your next book?")
 timeframe = float(timeframe)
#add a value error check here  
 
#first we filter only from the top 10 list above 
 print("You can read the following ",user_genre,"books from the top 10 list in ",timeframe,"days: ")
 index = 0
 count = 0
 found = False
 suitable_books=[]
 
 while index<len(top_10):
  if top_10.iloc[index]["days"] <= timeframe:
   suitable_books.append(top_10.iloc[index])
   found = True
  index += 1
 
 if found:
    suitable_books_df = pd.DataFrame(suitable_books)
    print(suitable_books_df[["title", "author", "avg_rating", "days"]].to_string(index=False))
 else:
  print("None of the top 10 rated books in the ",user_genre,"category can be read in ", timeframe, "days.")
  
  print("Would you like a lower rated recommendation? Write Yes or No")
  user_decision=input().lower()
  low_rated=[]
  while user_decision not in ("yes", "no"):
   print("Invalid input, please write yes or no.")
   user_decision=input().lower()	
	
  if user_decision=="yes":
   index = 0
   time = False
   while index<len(sorted_books):
    if sorted_books.iloc[index]["days"] <= timeframe:
     low_rated.append(sorted_books.iloc[index])   
     time = True
    index += 1
    
   if time:
    low_rated_df = pd.DataFrame(low_rated)
    print(low_rated_df[["title", "author", "avg_rating", "days"]].to_string(index=False)) 
   else:
    print("None of the books in the ", user_genre, "category can be read in", timeframe, "days.") 
         
  elif user_decision=="no":
   print("Would you like to pick another genre? Write yes or no")
   user_runagain=input().lower()
   if user_runagain=="no":
    run_again=False
    print("Thank you for using our programme!")




