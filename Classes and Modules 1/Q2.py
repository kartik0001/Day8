# Q2.

class Student():
    ''' Class to Set the Name,Age,Marks and Display the Student Information '''
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll
    def display(self):
        '''This Method is used to display the Student Information'''
        print('Name:',self.name)
        print('Roll No:',self.roll)
    def setAge(self,age):
        '''setter method is used to set the Age of student'''
        self.age=age
        print('Age:',self.age)
    def setMarks(self,marks):
        '''This method set the marks of the Student'''
        self.marks = marks
        print('Marks:',self.marks)

s1=Student('abc',123)
s1.display()
s1.setAge(18)
s1.setMarks(80)

'''
OUTPUT:
Name: abc
Roll No: 123
Age: 18
Marks: 80
'''

