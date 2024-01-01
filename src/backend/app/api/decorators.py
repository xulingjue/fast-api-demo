from functools import wraps


# 装饰器函数
def log_request(func):
    '''
    此处省略了decorator层
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result

    return wrapper
