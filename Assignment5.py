# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Joe Aldana,15FEB22,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
textFile = open(objFile, 'r')
for row in textFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)
textFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print(row)

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        while True:
            strTask = input("Task: ")
            strPriority = input("Priority: ")
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit? Y/N")
            if strChoice.lower().strip() == 'y':
                break
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        while True:
            strTask = input("Task to Remove:")
            for row in lstTable:
                if row["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    print("Task removed.")
                    print(lstTable)
                else:
                    print("Task not found.")
                    print(lstTable)
            strChoice = input("Exit? Y/N")
            if strChoice.lower() == 'y':
                break

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        textFile = open(objFile, 'w')
        for row in lstTable:
            textFile.write(str(row["Task"]) + ',' + str(row["Priority"]) + '\n')
        textFile.close()

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program
