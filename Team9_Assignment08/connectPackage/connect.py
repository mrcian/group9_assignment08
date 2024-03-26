import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

cursor.execute('''
                USE GroceryStoreSimulator
                GO
                
                SELECT
                   se.LastName AS Employee_Last_Name,
                   e.FirstName AS Employee_First_Name,
                   t.EmplTitle AS Employee_Title,
                   s.Store AS Store_Location_Total,
                   COUNT(tr.EmplID) AS Employee_Transactions
                FROM
                    tEmpl as e
                    JOIN tStore AS s ON e.StoreID = s.StoreID
                    JOIN tEmplTitle AS T ON e.EmplTitleID = t.EmplTitleID
                    JOIN tTransaction as tr ON tr.EmplID = e.EmplID
                WHERE 
                    s.Store = 'Amelia'
                GROUP BY 
                    s.Store, t.EmplTitle, e.FirstName, e.LastName
                ORDER BY
                    Employee_Transactions
                ''')

exampleList = list()

for row in cursor:
    if row.Store_Location_Total.strip() == "Amelia":
        exampleList.append((row.Employee_Last_Name,row.Employee_First_Name))
    
if __name__ == "__main__":
    print(exampleList)