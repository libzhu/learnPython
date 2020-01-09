# coding=utf-8

# 导入数字开头的模块
import importlib
tuling = importlib.import_module("01")
stu = tuling.Student("dana", 30)
stu.say()