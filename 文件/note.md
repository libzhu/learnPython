# 文件
- 长久保存信息的一种数据信息集合
- 常用操作
    - 打开关闭（文件一旦打开， 需要关闭操作）
    - 读写内容
    - 查找
# With 语句
- with语句，使用的技术一种上下文管理协议的技术（ContextManagementProtocol）系统负责关闭文件
- 自动判断文件的作用域，自动关闭不在使用的打开文件的句柄
# open 函数
- open函数负责打开文件， 带有很多参数
    - 第一个参数必须要有，文件的路径和名称
    - mode: 表明文件用什么方式打开
        - r:以只读方式打开
        - w:写方式打开，会覆盖以前的内容
            - write(str) 把字符串写入文件
            - writeline(str):把字符串按行写入
            - 区别
                - write参数只能是字符串
                - writeline 参数可以是字符串， 也可以是字符序列
        - x:创建方式打开，如果文件存在，报错
        - a: appendf方式，已追加的方式对文件内容进行写入
        - b:binary方式，二进制方式写入
        - t: 文本方式打开
        - +：可读写
# seek(offset, from)
- 移动文件的读取位置
- from的取值范围
    - 0：从文件头开始偏移
    - 1：从文件当前位置开始偏移
    - 2：从文件末尾开始偏移   
- 移动的单位是字节（byte）
- 一个汉字有若干个字节组成
# 持久化 pickle
- 序列化（持久化， 落地),把程序运行中的信息保存在磁盘上
- 反序列化：序列号的逆过程
- pickle：Python提供的序列化模块
- pickle.dump: 序列化
- pickle.load: 反序列化
# 持久化 - shelve
- 持久化工具
- 类似字典，用kv对保存数据，存取方式和字典也类似
- open close
- shelve特性 
    - 不支持多个应用并行写入
        - 为了解决这个问题，open的时候可以使用flag=r
    - 写回问题
        - shelve：特殊情况下不会等待持久化对象进行任何修改
        - 解决办法：强制写回，writeback = True


        