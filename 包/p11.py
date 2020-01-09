
from pkg02 import  *

stu = p01.Student("dandan", 30)
stu.say()

# 因为 __init__.py 中设置了 __all__  只会加载 __all__ 中的内容， 所以会报错下面语句
# inInit() # NameError: name 'inInit' is not defined

