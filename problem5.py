# Design & develop a web application to maintain records of students.
# The single the record shall contain the following information:
# | Name | Roll number | Age | Gender |

import os
from enum import Enum

os.system("")


class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class Student(object):
    VALID_GENDER = ['Male', 'Female', 'Other']

    def __init__(self, name, roll_no, age, gender):
        self.__name = name
        self.__roll_no = roll_no
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def roll_no(self):
        return self.__roll_no

    @roll_no.setter
    def roll_no(self, value):
        self.__roll_no = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    def is_valid(self):
        try:
            self.__age = int(self.__age)
            if self.age < 0:
                return False, "Invalid age: {0}, Age should be above 0".format(self.__age)
            if self.age > 100:
                return False, "Invalid age: {0}, Age should be below 100".format(self.__age)
        except Exception:
            return False, "Invalid age: {0}".format(self.__age)
        if not isinstance(self.__name, str):
            return False, "Invalid Name: {0}".format(self.__name)
        valid_gender_list = [Gender.MALE.value.lower(), Gender.FEMALE.value.lower()]
        print(valid_gender_list, self.__gender)
        if self.__gender and self.__gender.lower() not in valid_gender_list:
            return False, "Gender Should be in {0}".format(valid_gender_list)
        return True, "Valid student"


students = dict()


class StudentDb(object):
    def __init__(self):
        pass

    def is_student_exists(self, name):
        """
        :param name:
        :return:
        """
        if name in students:
            return True
        return False

    def insert(self):
        print(Style.BLACK + "Enter student detail: ")
        name = input("Name: ")
        if self.is_student_exists(name):
            print(Style.YELLOW + 'Student already exists with this name')
            return False
        roll_no = input("Roll No: ")
        age = input("Age: ")
        gender = input("Gender: ")
        student = Student(name, roll_no, age, gender)
        ret_val, message = student.is_valid()
        if not ret_val:
            print(Style.RED + "Failed to create student. " + message)
            return False
        students[name] = student
        print(Style.GREEN + "Successfully created {0} student".format(student.name))
        return True

    def delete(self):
        name = input("Enter student name to delete: ")
        if self.is_student_exists(name):
            students.pop(name, None)
            print(Style.GREEN + 'Successfully deleted {0} student'.format(name))
            return True
        print(Style.RED + "{0} student not found to delete".format(name))
        return False

    def __display(self, student):
        print(Style.BLUE + '************************************')
        print(Style.BLUE + "Name: ", student.name)
        print(Style.BLUE + "Roll No: ", student.roll_no)
        print(Style.BLUE + "Age: ", student.age)
        print(Style.BLUE + "Gender: ", student.gender)
        print(Style.BLUE + '************************************')

    def update(self):
        name = input("Enter student name to update Details: ")
        if not self.is_student_exists(name):
            print(Style.RED + "{0} Student not present to update".format(name))
            return False
        student = students.get(name)
        yes_or_no = input("Do you want to update roll_no: (y/n): ")
        if yes_or_no and yes_or_no.lower() == 'y':
            roll_no = input("Enter Roll No: ")
            student.roll_no = roll_no

        yes_or_no = input("Do you want to update Age: (y/n): ")
        if yes_or_no and yes_or_no.lower() == 'y':
            age = input("Enter Age: ")
            student.age = age

        yes_or_no = input("Do you want to update Gender: (y/n): ")
        if yes_or_no and yes_or_no.lower() == 'y':
            gender = input("Enter Gender: ")
            student.gender = gender
        ret_val, message = student.is_valid()
        if not ret_val:
            print(Style.RED + "Failed to update {0} student. ".format(name) + message)
            return False
        students[name] = student
        print(Style.GREEN + "Successfully updated {0} student".format(name))
        return True

    def search(self):
        name = input("Enter name to search: ")
        if not isinstance(name, str):
            print(Style.RED + "Invalid name: {0}".format(name))
            return False
        if self.is_student_exists(name=name.lower()):
            self.__display(students.get(name))
            return True
        print(Style.MAGENTA + "{0} Student not found".format(name))
        return False

    def exit(self):
        print(Style.BLUE + "Terminating...")
        exit()


def main():
    student_db = StudentDb()
    mapped_methods = {'1': student_db.insert, '2': student_db.search, '3': student_db.delete,
                      '4': student_db.update, '5': student_db.exit}
    while True:
        print(Style.BLACK + "Enter 1 : Insert Student:\nEnter 2 : Search Details of a Student\n"
              "Enter 3 : Delete Details of Student\nEnter 4 : Update Student Details\nEnter 5 : To Exit")
        print(Style.BLACK + '-------------------------------------')
        operation = str(input())
        map_method = mapped_methods.get(operation, None)
        if map_method is None:
            print(Style.RED + "Invalid input provided")
            continue
        map_method()
        print(Style.BLACK + '-------------------------------------')


if __name__ == '__main__':
    main()
