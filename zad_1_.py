# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:53:48 2023

@author: student
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


student1 = Student("Lukasz", [70, 75, 80, 90])
student2 = Student("Daniel", [20, 30, 60, 45])

# Wywoływanie metody is_passed dla obiektów
result1 = student1.is_passed()
result2 = student2.is_passed()

# Wyświetlanie wyników
print(f"{student1.name} passed: {result1}")
print(f"{student2.name} passed: {result2}")
