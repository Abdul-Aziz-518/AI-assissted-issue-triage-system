'''Create a Python program that:
Takes issue input from user
Generates a unique ID
Stores it in a CSV file
Another function that:
Reads all issues
Displays:
Total issues
Issues per category (manual for now)

import pandas as pd
from datetime import date, time
df=pd.read_csv("issues.csv")
def _issue(): 
    dict1={
    "name": input("Enter your name"),
    "rollno": input("Enter your Roll Number"),
    "location": input("Enter the location of the issue"),
    "issue": input("Enter your issue in detail"),
    "d": date.today(),
    "t": time.today(),
    }
    df.append({dict1})
_issue()
print(df)'''
from datetime import datetime
print(datetime.now().date())
print(datetime.now().time())
