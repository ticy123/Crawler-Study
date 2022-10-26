import time
from datetime import datetime
def timing(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(f"{start.strftime('%Y-%m-%d %H:%M:%S')} : {func.__name__}函数开始运行....")
        func(*args, **kwargs)
        end = datetime.now()
        print(f"{end.strftime('%Y-%m-%d %H:%M:%S')} : {func.__name__}函数结束运行,运行总时间为{(end-start).seconds}s")
    return wrapper

