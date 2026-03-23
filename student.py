class Person:
    def __init__(self, name):
        self.name = name



class Student(Person):

    def __init__(self, roll, name, marks):
        self.roll = roll
        super().__init__(name)   # call Person
        
        self.marks = marks
   

        
    # 3. __str__ method
    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}"

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "marks": self.marks
            }
    @classmethod
    def from_dict(cls, data): # here cls = Student class
        return cls(data["roll"], data["name"], data["marks"]) # converts dictionary → object

# s1 = Student(1,"Rahul",85)
# print(s1.roll)
# print(s1.name)
# print(s1.marks)
# print("-----------------------------------")
# s2 = Student(2,"Aman",90)
# print(s2.roll)
# print(s2.name)
# print(s2.marks)
# print("-----------------------------------")
# s3 = Student(3,"Priya",88)
# print(s3.roll)
# print(s3.name)
# print(s3.marks)




    

# #### What is @classmethod?
#     The method belongs to the class, not to a specific object.

#     @classmethod defines a method that works with the class itself rather than instances. It receives
# the class (cls) as the first parameter and is often used for factory methods like creating objects from dictionaries or other data formats.

#     Normally methods use self (object).
#     But class methods use cls (the class itself).

# #### Example :

#     Normal Method :


# class Student:
#     def show(self):
#         print("Hello")
# s = Student()
# s.show()


#     Class Method :

# class Student:
#     @classmethod
#     def hello(cls):
#         print("Hello from class")
# Student.hello()


#### why we do this
# @classmethod
#     def from_dict(cls, data):
#         return cls(data["roll"], data["name"], data["marks"])


#     because sometimes we receive data in the form of dictionary, so make that data in the form of object
# #### Why this is needed
#     JSON stores dictionary, not objects.

#     Example JSON: 

# [
#  {"roll":1,"name":"Rahul","marks":85},
#  {"roll":2,"name":"Aman","marks":90}
# ]
# ```
#     so we convert : Student object → dictionary → JSON file

    ### Step 9 — Improve student.py

    # We add two helper methods to convert object → dictionary and dictionary → object.

##############################################################################################################################

# Encapsulation

# class Person:
#     def __init__(self, name):
#         self.name = name


# class Student(Person):

#     def __init__(self, roll, name, marks):
#         super().__init__(name)
#         self.__roll = roll      # private
#         self.__marks = marks    # private

#     # getter for roll
#     def get_roll(self):
#         return self.__roll

#     # getter for marks
#     def get_marks(self):
#         return self.__marks

#     # setter for marks (with validation)
#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid marks!")

#     # __str__ method
#     def __str__(self):
#         return f"Roll: {self.__roll}, Name: {self.name}, Marks: {self.__marks}"

#     # convert object → dictionary
#     def to_dict(self):
#         return {
#             "roll": self.__roll,
#             "name": self.name,
#             "marks": self.__marks
#         }

#     # convert dictionary → object
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data["roll"], data["name"], data["marks"])

###################################################################################

# Properties (@property) — modern encapsulation

# 👉 Better than getters/setters


# class Person:
#     def __init__(self, name):
#         self.name = name


# class Student(Person):

#     def __init__(self, roll, name, marks):
#         super().__init__(name)
#         self._roll = roll
#         self._marks = marks

#     # property for marks (getter)
#     @property
#     def marks(self):
#         return self._marks

#     # setter with validation
#     @marks.setter
#     def marks(self, value):
#         if 0 <= value <= 100:
#             self._marks = value
#         else:
#             print("Invalid marks!")

#     def __str__(self):
#         return f"Roll: {self._roll}, Name: {self.name}, Marks: {self._marks}"