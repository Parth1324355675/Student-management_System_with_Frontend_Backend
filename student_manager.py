from student import Student
import json
import logging
import csv

logging.basicConfig(filename="app.log", level=logging.INFO)


class StudentManager:

    def __init__(self):
        self.students = [] # Stores all student objects.
        self.load_students()

    # Now when program starts → it loads saved students.


    def add_student(self, roll, name, marks):
        student = Student(roll, name, marks)
        if marks < 0 or marks > 100:
            print("Invalid marks! Enter between 0 and 100")
            logging.error("Invalid marks")
            return
        for s in self.students:
            if s.roll == roll:
                print("Roll number already exists!")
                return
            
        self.students.append(student)
        logging.info("Student added")
        self.save_students()
        print("Student added successfully!")

    def display_students(self):

        if len(self.students) == 0:
            print("No students found")
            return

        # sort by marks (highest first)
        self.students.sort(key=lambda s: s.marks, reverse=True)

        for s in self.students:
            print(f"Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")

#### Until now we have:
    # Add Student
    # Display Students


#### Now we will add:
    # Search Student
    # Update Student
    # Delete Student
    # All these changes will be inside student_manager.py and main.py.


### Step 4 — Search Student
    # Update student_manager.py

    # Add this method inside the StudentManager class.

    # def search_student(self, roll):
    #     for s in self.students:
    #         if s.roll == roll:
    #             print(f"Student Found → Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")
    #             return

    #     print("Student not found")


# Better search

# 👉 Problem: Search is limited

# Improve:

# Search by roll OR name

    def search_student(self, key):
        for s in self.students:
            if s.roll == key or s.name.lower() == key.lower():
                print(s)
                return
        print("Student not found")

### Step 5 — Update Student

    # Add this method in student_manager.py

    def update_student(self, roll):
                
        for s in self.students:
            if s.roll == roll:
                s.name = input("Enter new name: ")
               
               
                # Error handling
                try:
                    marks = float(input("Enter marks: "))
                except ValueError:
                    print("Invalid input!")
                    return
            
            # validation AFTER input
                if not (0 <= marks <= 100):
                    print("Invalid marks! Enter between 0 and 100")
                    logging.error("Invalid marks")
                    return
            
                s.marks = marks
                print("Student updated successfully!")
                logging.info("Student updated")
                self.save_students()
                return

        print("Student not found")

### Step 6 — Delete Student

    # Add this method in student_manager.py

    def delete_student(self, roll):

        for s in self.students:

            if s.roll == roll:
                self.students.remove(s)
                print("Student deleted successfully!")
                self.save_students()
                return

        print("Student not found")

    # This removes the student from list.

### Step 10 — Update student_manager.py

    # Add file loading and saving.

    # First import JSON : 

### Step 11 — Load Students from File

    def load_students(self):

        try:

            with open("students.json","r") as file:

                data = json.load(file)

                for item in data:
                    student = Student.from_dict(item)
                    self.students.append(student)

        except FileNotFoundError:
            pass

#### Explanation:
    # open file
    # read JSON
    # convert dictionaries → Student objects
    # store in list


    ### Step 12 — Save Students to File

    def save_students(self):

        data = []

        for s in self.students:
            data.append(s.to_dict())

        with open("students.json","w") as file:
            json.dump(data,file,indent=4)


    # Now we convert: Student objects → dictionary → JSON


### Step 13 — Save Data After Changes

#     Update these methods in student_manager.py

#     Inside add_student :    self.save_students()
#     Inside update_student : self.save_students()
#     Inside delete_student : self.save_students()

#     Now every change automatically updates the file.
# #### Example students.json
#     After adding students:
# ```json
# [
#     {
#         "roll": 1,
#         "name": "Rahul",
#         "marks": 85
#     },
#     {
#         "roll": 2,
#         "name": "Priya",
#         "marks": 90
#     }
# ]


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



        #   CSV export

# 👉 Save data in Excel format


    def export_to_csv(self):
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll", "Name", "Marks"])

            for s in self.students:
                writer.writerow([s.roll, s.name, s.marks])

        print("Data exported to CSV!")



    # Report generation

    def generate_report(self):
        total = len(self.students)

        if total == 0:
            print("No students available")
            return

        avg = sum(s.marks for s in self.students) / total
        highest = max(self.students, key=lambda s: s.marks)
        lowest = min(self.students, key=lambda s: s.marks)

        print(f"Total Students: {total}")
        print(f"Average Marks: {avg}")
        print(f"Topper: {highest.name} ({highest.marks})")
        print(f"Lowest: {lowest.name} ({lowest.marks})")