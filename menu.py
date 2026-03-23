#### This file runs the program.


from student_manager import StudentManager

manager = StudentManager()

while True:

    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Export to CSV")
    print("7. Generate Report")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        if name.isalpha():
            print("valid input")
        else:
            print("enter valid name")

        try:
            roll = int(input("Enter Roll: "))
            marks = float(input("Enter Marks: "))
        except ValueError:
            print("Enter valid input") 


        manager.add_student(roll, name, marks)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":

        roll = int(input("Enter Roll to search: "))
        manager.search_student(roll)

    elif choice == "4":

        roll = int(input("Enter Roll to update: "))
        manager.update_student(roll)

    elif choice == "5":

        roll = int(input("Enter Roll to delete: "))
        manager.delete_student(roll)

    elif choice == "6":
        manager.export_to_csv()

    elif choice == "7":
        manager.generate_report()

    elif choice == "8":

        print("Exiting program")
        break

    else:

        print("Invalid choice")

#### This project now covers:

#     Classes

#     Objects

#     List of objects

#     Methods

#     CRUD operations

#     Modular Python files

#     Importing modules

#     Menu driven program
# #### Right now the data disappears when program closes.
#     Next we can add:
#     File Handling
#     Student data saved in file
#     Data loads automatically when program starts
# ### next level: Persistent Storage using File Handling.
#     Right now: When program closes → all student data is lost

#     So we will add: 
#                     Save students to file
#                     Load students automatically when program starts
    
#     We will use JSON file because it is simple and readable.
# ---
# ### Step 8 — Project Structure (Updated)
#     Your folder now looks like this:
# ```python
# student_management/
# │
# ├── main.py
# ├── student.py
# ├── student_manager.py
# └── students.json
# ```
#     students.json will store all student records.
# ---



#### Example Program Flow
#     Start Program
#         ↓
#     Load students.json
#         ↓
#     Students appear in list
#         ↓
#     Add / Update / Delete
#         ↓
#     Save back to file

#     Now the system behaves like a real database system.
# #### This upgrade teaches very important real skills:

#     File handling

#     JSON

#     Object → dictionary conversion

#     Dictionary → object conversion

#     Persistence

#     Exception handling

#     Better OOP design



## Level 2 Improvements
#     Duplicate roll number prevention
#     Marks validation
#     __str__ method
#     Better search
#     Sorting students


# ## Level 3 (Industry Style)
#     Logging system
#     Error handling
#     CSV export
#     Report generation



# ## Level 4 (Advanced Python OOP)
#     Inheritance (Person → Student)
#     Encapsulation
#     Properties
#     Unit Testing