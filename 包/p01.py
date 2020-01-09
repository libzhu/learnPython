# coding=utf-8

class Student():
    def __init__(self, name = "noName", age = 18):
        self.name = name
        self.age = age


    def say(self):
        print("my name is {0}".format(self.name))


def sayHello():
    print("Hi, 天安门")



# 此判断语句建议一直作为程序入口
if __name__ == '__main__':
    print("我是模块p01")




