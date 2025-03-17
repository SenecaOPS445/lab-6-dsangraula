#!/usr/bin/env python3

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.grades = {}
    
    def displayStudent(self):
        return f"Student Name: {self.name}\nStudent Number: {self.number}"
    
    def addGrade(self, course, grade):
        self.grades[course] = grade
    
    def displayGPA(self):
        if not self.grades:
            return f"GPA of student {self.name} is 0.0"
        gpa = sum(self.grades.values()) / len(self.grades)
        return f"GPA of student {self.name} is {gpa}"
    
    def displayCourses(self):
        return [course for course, grade in self.grades.items() if grade > 0.0]
