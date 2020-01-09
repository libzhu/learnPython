# coding=utf-8


class Student():
    def __init__(self, name = "noName", age = 18):
        self.name = name
        self.age = age


    def say(self):
        print("my name is {0}".format(self.name))


def sayHello():
    print("Hi, 武汉")

print("我是模块01")
