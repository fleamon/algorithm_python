# -*- encoding: utf-8

from abc import ABCMeta, abstractmethod


class Book:
    __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print "Title: " + title
        print "Author: " + author
        print "Price: " + str(price)


title = raw_input()
author = raw_input()
price = int(raw_input())
new_novel = MyBook(title, author, price)
new_novel.display()
