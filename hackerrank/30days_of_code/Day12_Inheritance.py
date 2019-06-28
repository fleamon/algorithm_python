#!/usr/bin/env python
# -*- encoding: utf-8


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        res = 0.0
        sum = 0
        for i in scores:
            sum = sum + i
        res = sum / len(scores)
        if res >= 90:
            return "O"
        elif res >= 80:
            return "E"
        elif res >= 70:
            return "A"
        elif res >= 55:
            return "P"
        elif res >= 40:
            return "D"
        else:
            return "T"


line = raw_input().split()
