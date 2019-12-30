# coding=utf-8

def printFunc():
    print("*" * 100)
    return None

# 实例方法、类方法、静态方法的案例
class Person():
    # 实例方法
    def eat(self):
        print(self)
        print("eating.....")

    # 类方法
    # 类方法的第一个参数，一般命名为cls 区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("play.....")

    # 静态方法
    # 不需要用第一个参数表示自己或者类
    @staticmethod
    def say():
        print("say.....")

# 实例方法调用
yueyue = Person()
yueyue.eat()

printFunc()

# 类方法
Person.play()
yueyue.play()
printFunc()

# 静态方法
Person.say()
yueyue.say()

