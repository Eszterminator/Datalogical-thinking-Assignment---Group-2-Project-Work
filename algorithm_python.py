import pandas as pd

books = pd.read_csv("data/goodreads_cleaned_fixed.csv")

books["genre"] = books["genre"].fillna("").str.lower().str.strip()
books["page_count"] = pd.to_numeric(books["page_count"], errors="coerce")
books["average_rating"] = pd.to_numeric(books["average_rating"], errors="coerce")

run_again = True

while run_again:

 print("Pick one of the following genres you would like to read: Fantasy, Fiction, Young Adult, Classics. Write End to exit")
 user_genre = input().lower().strip()
 while user_genre != "fantasy" and user_genre!= "fiction" and user_genre != "young adult" and user_genre != "classics" and user_genre != "end":
  print("Invalid input, please try again. Please type Fantasy, Classics, Fiction, Young Adult or write End to exit.")  
  user_genre = input().lower().strip()
    
 if user_genre=="end":
  print("Thank you for trying our programme!")
  run_again = False
  break
 
 speed = input("How many pages a day do you read?").strip()
 while not speed.isdigit() or int(speed) <= 0:
   print("Enter a positive number please:")
   speed = input().strip()
 speed=int(speed)
 
 timeframe = input("How many days do you have available to read your next book?").strip()
 while not timeframe.isdigit() or int(timeframe) <= 0:
  print("Enter a positive number please:")  
  timeframe = input().strip()
 timeframe=int(timeframe)
 
 filtered = books[(books["genre"] == user_genre) & (books["page_count"] > 0) & (books["average_rating"].notna())].copy()
 
 filtered["days"] = filtered["page_count"]/speed
 
 filtered = filtered[filtered["days"] <= timeframe]
 
 
 if filtered.empty:
  print(f"No {user_genre} books match your reading time limit " f"of {timeframe} days at {speed} pages per day.")
 else:  
  sorted_books = filtered.sort_values(by=["average_rating", "days"], ascending=[False, True])
  top_10 = sorted_books.head(10).copy()
  top_10.insert(0, "Rank", range(1, len(top_10) + 1))
  print("The top 10 rated",user_genre,"books, and the number of days they would take to read at",speed,"pages per day:")
  print(top_10[["Rank", "title", "author", "average_rating", "page_count", "year", "days"]].to_string(index=False))
 
 
 print("Would you like to try again? Write yes or no")
 user_runagain=input().lower().strip()
  
 while user_runagain != "yes" and user_runagain != "no":
  print ("Invalid input, please write yes or no.")
  user_runagain=input().lower().strip()
  
 if user_runagain=="no":
  run_again=False
  print("Thank you for using our programme!")




