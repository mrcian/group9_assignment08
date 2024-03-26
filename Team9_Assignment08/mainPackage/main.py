# Name: Aanika Garre, Cian Roopnarine, & Connor Laughlin
# email: garreaa@mail.uc.edu, roopnacn@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on collaboration, using GitHub, and connecting to a database in Microsoft
#SQL Server Studio.

# Brief Description of what this module does: This module focuses on accessing data in SQL Server Studio and running SQL queries to output data
#in Eclipse.
# Citations:
# Anything else that's relevant:

from connectPackage.connect import *

if __name__ == "__main__":
    print("test test test:")
    for Employee_Last_Name, Employee_First_Name in exampleList:
        print("Last Name", Employee_Last_Name,"First Name", Employee_First_Name)

'''
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
#I only want private schools
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference WHERE IsPrivate = 1')

#mod the code to store all the university values into a list
#after the loop, print that list

#take out all the spaces that are padding the names
Universities = list()  #instantiate an empty list
for row in cursor:
    Universities.append(row.University.strip())
    
print(Universities)
'''