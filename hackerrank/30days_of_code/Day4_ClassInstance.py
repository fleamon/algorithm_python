# -*- encoding: utf-8

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if initialAge < 0:
            print "Age is not valid, setting age to 0."
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print "You are young."
        elif 13 <= self.age < 18:
            print "You are a teenager."
        elif self.age >= 18:
            print "You are old."
    def yearPasses(self):
        # Increment the age of the person in here
        self.age = self.age + 1

