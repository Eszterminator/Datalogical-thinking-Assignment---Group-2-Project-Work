import pandas as pd

#read in the data file as dataframe 
#need to change this to the github file when it is uploaded
books = pd.read_csv(r"C:\Users\madar\Documents\Masters degree Boras uni\datalogical thinking\goodreads.csv")

#to repeat the program, asking for another genre if they want to at the end 
run_again = True
genres = ["Fantasy", "Fiction", "Classics", "Young Adult"]

while(run_again):
 #getting the user input and validating it

 print("Pick one of the following genres you would like to read: Fantasy, Fiction, Young Adult, Classics. Write End to exit")
 user_genre = input()
 while user_genre not in genres:
  if user_genre=="end":
   print("Thank you for trying our programme")
   exit()
  else:
   print("Invalid genre. Please choose from Fantasy, Fiction, Young Adult or Classics")
  user_genre = input()
 
 #select the books where the genre matches user input 
 filtered_genre = books[books["genre"] == user_genre]


 #get user speed of reading 
 speed = input("How many pages a day do you read?")
 while not speed.isdigit() or int(speed) <= 0:
   print("Enter a positive number please:")
   speed = input("How many pages a day do you read?")
 speed=int(speed)
 
 #get user time limit for reading
 timeframe = input("How many days do you have available to read your next book?")
 timeframe = float(timeframe)
 while not timeframe.isdigit() or timeframe <= 0:
  print("Enter a positive number please:")  
  timeframe = input()

 #filter the genre books to fit timeframe and add days needed to read column 
 filtered_genre["days"] = (filtered_genre["num_pages"]/speed)
 filtered_time = filtered_genre[filtered_genre["days"]<= timeframe]
 
#do i need this from before?? THINK THROUGH
 index = 0
  count = 0
  found = False
  filtered_time=[]
   
  while index<len(filtered_genre):
    if filtered_genre.iloc[index]["days"] <= timeframe:
     filtered_time.append(top_10.iloc[index])
     found = True
    index += 1
   
  if found:
   filtered_time_df = pd.DataFrame(filtered_time)
   print(filtered_time_df[["title", "author", "average_rating", "days"]].to_string(index=False))
  else:
   print("....")
##insertion ends here  
 
 
 
 if filtered_time is empty: #how to mark empty??
   print ("None of the ",user_genre,"books could be read in the given time at the given speed.")
 else: #sort for top 10 rated from the filtered dataframe  
  sorted_books = filtered_time.sort_values(by=["average_rating", "days"], ascending=[False, True])
  top_10 = sorted_books.head(10)
  print("The top 10 rated",user_genre,"books, and the number of days they would take to read at",speed,"pages per day:")
  print(top_10[["title", "author", "average_rating", "days"]].to_string(index=False))
 
 
#left off changing the code here 26/oct
 
  
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




