# LOG
- [https://www.cnblogs.com/yyds/p/6901864.html]
- logging
- logging模块提供模块级别的函数记录日志
- 包括四大组件

## 1、日志相关概念
- 日志
- 日志的级别(level)
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作=> 不要频繁操作
- LOG 的作用
    - 调用
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - Level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
    
# 2 logging 模块
- 日志级别
    - 级别可以定义
        - DEBUG
        - INFO
        - WARNING
        - ERROR
        - CRITICAL
        
- 初始化、写日志实例化需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方式
    - 直接使用 logging(封装了其他组件) 模块
    - logging四大组件
    
# 2.1 logging模块级别的日志
- 使用一下函数

        函数	                                        说明
        logging.debug(msg, *args, **kwargs) 	    创建一条严重级别为DEBUG的日志记录
        logging.info(msg, *args, **kwargs)	        创建一条严重级别为INFO的日志记录
        logging.warning(msg, *args, **kwargs)	    创建一条严重级别为WARNING的日志记录
        logging.error(msg, *args, **kwargs)	        创建一条严重级别为ERROR的日志记录
        logging.critical(msg, *args, **kwargs)	    创建一条严重级别为CRITICAL的日志记录
        logging.log(level, *args, **kwargs)	        创建一条严重级别为level的日志记录
        logging.basicConfig(**kwargs)	            对root logger进行一次性配置
    
- logging.basicConfig(**kwargs)	            对root logger进行一次性配置
    - 只在第一次调用时候起作用
    - 不配置logger 则使用默认
        - 输出：sys.stderr(标准错误输出)
        - 级别：WARNING
        - 格式：level：log_name:content
    - format参数
        
            字段/属性名称     	使用格式            	    描述
            asctime	            %(asctime)s	            日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
            created	            %(created)f	            日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
            relativeCreated	    %(relativeCreated)d 	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
            msecs	            %(msecs)d	            日志事件发生事件的毫秒部分
            levelname	        %(levelname)s	        该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
            levelno	            %(levelno)s	            该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
            name	            %(name)s	            所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
            message             %(message)s	            日志记录的文本内容，通过 msg % args计算得到的
            pathname	        %(pathname)s	        调用日志记录函数的源码文件的全路径
            filename	        %(filename)s	        pathname的文件名部分，包含文件后缀
            module	            %(module)s	            filename的名称部分，不包含后缀
            lineno	            %(lineno)d	            调用日志记录函数的源代码所在的行号
            funcName	        %(funcName)s	        调用日志记录函数的函数名
            process	            %(process)d	            进程ID
            processName	        %(processName)s	        进程名称，Python 3.1新增
            thread	            %(thread)d	            线程ID
            threadName	        %(thread)s	            线程名称  
- 案例 01.py

# 2.2 logging模块的处理器
- 四大组件
    - 日志器(Logger): 参数日志的一个接口
        - 产生一个日志
        - 操作
        
                方法	                                            描述
                Logger.setLevel()	                            设置日志器将会处理的日志消息的最低严重级别
                Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
                Logger.addFilter() 和 Logger.removeFilter()	    为该logger对象添加 和 移除一个filter对象
                Logger.debug(), Logger.info(), Logger.warning(),
                Logger.error(), Logger.critical()	            创建一个与它们的方法名对应等级的日志记录
                Logger.exception()	                            创建一个类似于Logger.error()的日志消息
                Logger.log()                                    需要获取一个明确的日志level参数来创建一个日志记录
   
    - 处理器(Handler): 把产生的日志发到对应的目的地
        - Handler对象的作用是（基于日志消息的level）将消息分发到handler指定的位置（文件、网络、邮件等）。
        Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象。
        比如，一个应用程序可能想要实现以下几个日志需求：

            - 1）把所有日志都发送到一个日志文件中；
            - 2）把所有严重级别大于等于error的日志发送到stdout（标准输出）；
            - 3）把所有严重级别为critical的日志发送到一个email邮件地址。
        - 这种场景就需要3个不同的handlers，每个handler复杂发送一个特定严重级别的日志到一个特定的位置。
        一个handler中只有非常少数的方法是需要应用开发人员去关心的。对于使用内建handler对象的应用开发人员来说，
        似乎唯一相关的handler方法就是下面这几个配置方法：
        
                方法	                                                描述
                Handler.setLevel()	                                设置handler将会处理的日志消息的最低严重级别
                Handler.setFormatter()	                            为handler设置一个格式器对象
                Handler.addFilter() 和 Handler.removeFilter()        为handler添加 和 删除一个过滤器对象
        - 需要说明的是，应用程序代码不应该直接实例化和使用Handler实例。因为Handler是一个基类，它只定义了素有handlers都应该有的接口，
        同时提供了一些子类可以直接使用或覆盖的默认行为。下面是一些常用的Handler：
        
                Handler	                                                描述
                logging.StreamHandler	                                将日志消息发送到输出到Stream，如std.out, std.err或任
                                                                        何file-like对象。
                                                                        
                logging.FileHandler	                                    将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
                logging.handlers.RotatingFileHandler	                将日志消息发送到磁盘文件，并支持日志文件按大小切割
                logging.hanlders.TimedRotatingFileHandler	            将日志消息发送到磁盘文件，并支持日志文件按时间切割
                logging.handlers.HTTPHandler	                        将日志消息以GET或POST的方式发送给一个HTTP服务器
                logging.handlers.SMTPHandler	                        将日志消息发送给一个指定的email地址
                
                logging.NullHandler	                                    该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来
                                                                        避免'No handlers could be found for logger XXX'信息的出现。   
    - 过滤器(Filter): 更精细的控制哪些日志输出
        - Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，
        它只允许某个logger层级下的日志事件通过过滤。该类定义如下：   
            
                class logging.Filter(name='')
                        filter(record)
        - 比如，一个filter实例化时传递的name参数值为'A.B'，那么该filter实例将只允许名称为类似如下规则的loggers产生的日志记录通过过滤：'A.B'，'A.B,C'，'A.B.C.D'，'A.B.D'，而名称为'A.BB', 'B.A.B'的loggers产生的日志
        则会被过滤掉。如果name的值为空字符串，则允许所有的日志事件通过过滤。
        - filter方法用于具体控制传递的record记录是否能通过过滤，如果该方法返回值为0表示不能通过过滤，返回值为非0表示可以通过过滤。
                
                说明：
                如果有需要，也可以在filter(record)方法内部改变该record，比如添加、删除或修改一些属性。
                我们还可以通过filter做一些统计工作，比如可以计算下被一个特殊的logger或handler所处理的record数量等
    
    - 格式器(Formatter): 对输出信息进行格式化
        - Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化
        - Formatter类。另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。
        - Formatter类的构造方法定义如下：
            
                logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
                
        - 可见，该构造方法接收3个可选参数：
            - fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
            - datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
            - style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'
        