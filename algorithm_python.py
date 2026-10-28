import pandas as pd

books = pd.read_csv("data/goodreads_cleaned.csv", sep=";")
print(books.columns.tolist())

run_again = True
genres = ["Fantasy", "Fiction", "Classics", "Young Adult"]

while(run_again):

 print("Pick one of the following genres you would like to read: Fantasy, Fiction, Young Adult, Classics. Write End to exit")
 user_genre = input()
 while user_genre not in genres and user_genre != "End":
  print("Invalid input, please try again. Please type Fantasy, Classics, Fiction, Young Adult or write End to exit.")  
  user_genre = input()
    
 if user_genre=="End":
  print("Thank you for trying our programme!")
  run_again = False
  break
 
 speed = input("How many pages a day do you read?")
 while not speed.isdigit() or int(speed) <= 0:
   print("Enter a positive number please:")
   speed = input().strip()
 speed=int(speed)
 
 timeframe = input("How many days do you have available to read your next book?")
 while not timeframe.isdigit() or int(timeframe) <= 0:
  print("Enter a positive number please:")  
  timeframe = input().strip()
 timeframe=int(timeframe)
 
 filtered = books[books["genres"].str.lower().str.strip() == user_genre.lower().strip()].copy()
 
 filtered["days"] = filtered["page_count"]/speed
 
 filtered = filtered[filtered["days"] <= timeframe]
 
 
 if filtered.empty:
  print ("None of the ",user_genre,"books could be read in ",timeframe,"days at ",speed,"pages per day")
 else:  
  sorted_books = filtered.sort_values(by=["rating", "days"], ascending=[False, True])
  top_10 = sorted_books.head(10).copy()
  top_10.insert(0, "Rank", range(1, len(top_10) + 1))
  print("The top 10 rated",user_genre,"books, and the number of days they would take to read at",speed,"pages per day:")
  print(top_10[["Rank","title", "author", "rating", "rating_count", "year", "days"]].to_string(index=False))
 
 
 print("Would you like to try again? Write yes or no")
 user_runagain=input().lower().strip()
  
 while user_runagain != "yes" and user_runagain != "no":
  print ("Invalid input, please write yes or no.")
  user_runagain=input().lower().strip()
  
 if user_runagain=="no":
  run_again=False
  print("Thank you for using our programme!")




