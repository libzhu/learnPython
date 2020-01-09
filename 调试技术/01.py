# coding=utf-8

def sayHello(name):
    print("i want to say hello with your, {0}".format(name))
    print("Hello {0}".format(name))
    print("Done。。。。。。。。。。。")

if __name__ == '__main__':
    print("****" * 10)
    name = input("please input your name:")
    print(sayHello(name=name))
    print("@@@@" * 10)