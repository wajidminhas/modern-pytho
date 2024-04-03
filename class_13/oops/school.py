

class Student():
    # class variables
    school_name = 'ABC School'
    school_address = 'ABC Street'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name, 'School address:', Student.school_address)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
Student.school_address = 'XYZ Street'
print('School name:', Student.school_name, 'School address:', Student.school_address)


# HOW TO USE __INIT__ METHOD IN OOPS? 
# STUDENT INSTANCE IN OOP 

class NewStudent():

    # constructor
    # initialize instance variable
    def __init__(self, name, id):
        print('Inside Constructor')
        self.name = name
        self.id = id
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)
        print('My ID is', self.id)

    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')




# create object using constructor
n1 : NewStudent = NewStudent('John', 456)
n1.show()

del n1