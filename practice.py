# birth_year = input("In what year were you born? ")
# age = 2023 - int(birth_year)
# print("You are", age, "years old")
# correct_year = input("Is the age provided correct? ")
# print(correct_year)

# name = input("Name: ")

# if name == "Dennis":
#     print("You are great!")
#     print("Please let's finish this")
# elif name == "Joe":
#     print("You are not Dennis my friend!")
# else: 
#     print("Always print this")
    
# print("I am the last guy for the lines of code")


# x = [4, True, 'hi']
# x.append('hello')
# x.extend([4,5,5,5,5,5,5,'dennis','default'])
# y = x[:] 
# this is going to copy the list
# print(x.pop())
# print(x, y)
# print(x[3])

# x = (0,0,2,2,2)
#  tuple is different from a list

# for loops
# for i in range(10):
#     print(i)
# the range has three arguments start stop step

# for i in range(10, -2, -2):
#     print(i)


# list = [2,4,1,4,'string item',4,114,4]

# for i in range(len(list)):
#     print(list[i])

# for i, element in enumerate(list):
#     print(i, element)

# i = 0
# while i < 10:
#     print("run ooo", i)
#     i += 1

# i = 0
# while True:
#     print("run ooo", i)
#     i += 1
#     if i == 10:
#         break
    
    
# x = [0,1,2,4,5,3,2,3,5]
# y = ['hi','hello','goodbye','cya','sure']
# s = "hello"

# sliced = s[::-1]
# msliced = x[1:]
# ssliced = x[:4]
# print(sliced)

#slicing start stop and step...slicing can also reverse a list
#interesting the things slicing can do yep

#functions in python

# def func():
#     print("Run 99 or sleep")

# func()

# tim = 89
# x = f'hello {4 + 8} {tim} {67 + 9}'
# print(f'hello {tim}')
# Object Oriented Programming in Python 

# x = 17
# print(type(x))

# def hello():
#     print("Hello")
    
# print(type(hello))

# string = "hello"
# print(string.upper())

# class Dog:
#     def bark(self):
#         print("bark")
        
# dog = Dog()
# print(dog.bark())
# print(type(dog))


# class Dog:
#     def __init__(self):
#         pass
    
#     def add_one(self, x):
#         return x + 1
    
#     def bark(self):
#         print("bark")

# dog = Dog()
# print(dog.add_one(5))
# print(type(dog))


# class Dog: 
#     def __init__(self, name):
#         self.name = name
#         print(name)
        
# dog = Dog("Rocky")

# class Dog:
#     def __init__(self, name):
#         self.name = name
        
#     def get_name(self):
#         return self.name
    
# dog = Dog("Tim")
# print(dog.get_name())
# dog = Dog("Bill")
# print(dog.get_name())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
    
#     def set_age(self, age):
#         self.age = age
    
# dog = Dog("Tim", 34)
# dog2 = Dog("Bill", 12)
# dog2.set_age(23)
# print(dog.get_age())
# print(dog2.get_age())
# print(dog.get_name())
# print(dog2.get_name())


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade   # 0 - 100
        
#     def get_grade(self):
#         return self.grade
    
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
        
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
            
#         return value / len(self.students)
    
# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)

# print(course.students[0].name)
# print(course.students[0].age)
# print(course.students[0].grade)
# print("The average grade for the courses taken by the students is: ")
# print(course.get_average_grade())



# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def speak(self):
#         print("Meow")
        
# class Dog: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def speak(self):
#         print("Bark")


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
        
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
        
#     def speak(self):
#         print("Meow")
        
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
# class Dog(Pet):
#     def speak(self):
#         print("Bark")   
        
# p = Pet("Tim", 19)
# p.show()    
# d = Dog("Kim", 29)
# d.show()
# d.speak()
# c = Cat("Vio", 23, "Blue")
# c.show()

# class Person:
#     number_of_people = 0
    
#     def __init__(self, name):
#         self.name = name
#         Person.number_of_people += 1
        
# p1 = Person("tim")
# print(Person.number_of_people)
# p2 = Person("jill")
# print(Person.number_of_people)

# class Person:
#     number_of_people = 0
    
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
        
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
    
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("tim")
# p2 = Person("jill")

# print(Person.number_of_people_())



class Math:

    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")
        
        
print(Math.add10(29))
print(Math.add5(29))
Math.pr()