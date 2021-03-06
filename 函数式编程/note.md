# Python 语言的高级特性
## 函数式编程
- 基于lambada演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数， 同样可以作为返回值
    - 纯函数式编程 LISP Haskell
- 高阶函数
    - 把函数作为参数使用的函数，叫高阶函数
    - 系统定义的高阶函数
        - map 函数
            - 原意就是映射，即把集合或列表中的元素，每一个元素都按照一定规则进行操作，生成
            一个新的列表或集合
            - map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
        - reduce 函数
            - 原意就是归并，缩减
            - 把一个可迭代对象归并成一个结果
            - 对于作为参数的函数，必须由两个参数和一个返回值
            - reduce 需要导入functool包
            
        - filter 函数
            - 过滤函数：对一组新的数据进行过滤，符合条件的数据会生成一个新的
            列表并返回
            - 跟map函数比较
                - 相同：都对列表中的每一个元素逐一操作生成新的队列
                - filter不一定，只要符合条件的才会进入新的数据集合
            - filter函数
                - 利用给定函数进行判断
                - 返回值一定是布尔值
                - 调用格式
                    filter(f, data) f是过滤函数，data是数据
            - sorted - 排序
                - 把一个序列按照给定的算法进行排序
                - key: 在排序前对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序
                  
        
- 返回函数
    - 函数可以返回具体的值
    - 也可以返回一个函数作为结果
    - 闭包（closure）
        - 当一个函数在内部定义函数，并且内部的函数使用外部函数的参数或局部变量，内部函数被当成返回值放回时，
        相关参数和值保存在返回的函数中 我们称 这种结果为闭包。
    
- 匿名函数
- 装饰器
    - 在不改变函数代码的基础上无线扩展函数功能的一种机制，本质上装饰器是返回一个函数的高阶函数
    - 装饰器的使用：使用@语法 即在每次要扩展到函数定义前使用@+函数
- 偏函数
    - 参数固定的函数， 相当于由一个特定参数的函数体
    - functools.partial 的作用，把函数的某些参数固定，返回一个新的函数。

### lambda表达式
- 函数：最大程度复用代码
    - 存在问题：如果函数很小，很短，会造成啰嗦
    - 如果函数被调用次数少，则造成浪费
- lambda（匿名函数）
    - 一个表达式， 函数体相对简单
    - 不是代码块，仅仅是一个表达式
    - 可以有参数，有多个参数也可以，用逗号隔开
    
    
 