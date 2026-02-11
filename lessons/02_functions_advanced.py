"""
Python 进阶学习 - 第二课：函数进阶
=====================================

本课内容:
1. 参数类型 (*args, **kwargs)
2. Lambda 表达式
3. 闭包 (Closure)
4. 装饰器 (Decorator)
5. 生成器 (Generator)

运行方式: python lessons/02_functions_advanced.py
"""

# ============================================
# 1. 函数参数类型
# ============================================

print("=" * 50)
print("1. 函数参数类型")
print("=" * 50)


# 1.1 默认参数
def greet(name, greeting="你好"):
    """默认参数必须放在非默认参数后面"""
    return f"{greeting}, {name}!"


print(greet("小明"))  # 使用默认值
print(greet("小红", "早上好"))  # 覆盖默认值


# 1.2 *args - 接收任意数量的位置参数
def sum_all(*args):
    """*args 将所有位置参数打包成元组"""
    print(f"  收到的参数: {args}, 类型: {type(args)}")
    return sum(args)


print(f"\nsum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# 1.3 **kwargs - 接收任意数量的关键字参数
def print_info(**kwargs):
    """**kwargs 将所有关键字参数打包成字典"""
    print(f"  收到的参数: {kwargs}, 类型: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")


print("\nprint_info(name='张三', age=25, city='北京'):")
print_info(name="张三", age=25, city="北京")


# 1.4 混合使用
def mixed_args(a, b, *args, default="默认值", **kwargs):
    """参数顺序: 普通参数 -> *args -> 默认参数 -> **kwargs"""
    print(f"  a={a}, b={b}")
    print(f"  args={args}")
    print(f"  default={default}")
    print(f"  kwargs={kwargs}")


print("\nmixed_args(1, 2, 3, 4, default='自定义', x=10, y=20):")
mixed_args(1, 2, 3, 4, default="自定义", x=10, y=20)


# 1.5 解包参数
def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
info = {"a": 10, "b": 20, "c": 30}

print(f"\n解包列表: add(*[1,2,3]) = {add(*numbers)}")
print(f"解包字典: add(**{{'a':10,'b':20,'c':30}}) = {add(**info)}")


# ============================================
# 2. Lambda 表达式
# ============================================

print("\n" + "=" * 50)
print("2. Lambda 表达式")
print("=" * 50)

# Lambda: 匿名函数，用于简单的单行函数
# 语法: lambda 参数: 表达式

# 普通函数
def square(x):
    return x**2


# 等价的 Lambda
square_lambda = lambda x: x**2

print(f"square(5) = {square(5)}")
print(f"square_lambda(5) = {square_lambda(5)}")

# Lambda 常用场景

# 2.1 排序
students = [("小明", 85), ("小红", 92), ("小刚", 78)]

# 按分数排序
by_score = sorted(students, key=lambda x: x[1])
print(f"\n按分数排序: {by_score}")

# 按分数降序
by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"按分数降序: {by_score_desc}")

# 2.2 filter - 过滤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\n过滤偶数: {evens}")

# 2.3 map - 映射
squares = list(map(lambda x: x**2, numbers))
print(f"平方映射: {squares}")

# 2.4 reduce - 累积 (需要导入)
from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"累乘 1*2*3*4*5 = {product}")


# ============================================
# 3. 闭包 (Closure)
# ============================================

print("\n" + "=" * 50)
print("3. 闭包 (Closure)")
print("=" * 50)


# 闭包: 内部函数引用外部函数的变量，并返回内部函数
def make_multiplier(n):
    """创建一个乘法器"""

    def multiplier(x):
        return x * n  # 引用外部变量 n

    return multiplier


# 创建不同的乘法器
double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")  # 5 * 2 = 10
print(f"triple(5) = {triple(5)}")  # 5 * 3 = 15


# 闭包实际应用: 计数器
def make_counter():
    """创建一个计数器"""
    count = 0

    def counter():
        nonlocal count  # 声明使用外部变量
        count += 1
        return count

    return counter


counter1 = make_counter()
counter2 = make_counter()

print(f"\ncounter1: {counter1()}, {counter1()}, {counter1()}")  # 1, 2, 3
print(f"counter2: {counter2()}, {counter2()}")  # 1, 2 (独立计数)


# ============================================
# 4. 装饰器 (Decorator)
# ============================================

print("\n" + "=" * 50)
print("4. 装饰器 (Decorator)")
print("=" * 50)

import time


# 装饰器: 在不修改原函数的情况下，增加额外功能
# 本质是一个接收函数并返回新函数的高阶函数


# 4.1 基础装饰器 - 计时器
def timer(func):
    """测量函数执行时间的装饰器"""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  [{func.__name__}] 执行时间: {end - start:.4f}秒")
        return result

    return wrapper


@timer
def slow_function():
    """模拟耗时操作"""
    time.sleep(0.1)
    return "完成"


print("调用 slow_function():")
result = slow_function()
print(f"  返回值: {result}")


# 4.2 带参数的装饰器
def repeat(times):
    """重复执行函数的装饰器"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"  第 {i + 1} 次执行")
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def say_hello():
    print("    Hello!")


print("\n调用 say_hello():")
say_hello()


# 4.3 保留原函数信息
from functools import wraps


def log(func):
    """日志装饰器，使用 @wraps 保留原函数信息"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  调用函数: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    """加法函数"""
    return a + b


print(f"\nadd(3, 5) = {add(3, 5)}")
print(f"函数名: {add.__name__}")  # 保留了原函数名
print(f"文档: {add.__doc__}")  # 保留了原文档


# 4.4 类装饰器
class Counter:
    """统计函数调用次数的类装饰器"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  {self.func.__name__} 已调用 {self.count} 次")
        return self.func(*args, **kwargs)


@Counter
def greet_someone(name):
    return f"Hello, {name}!"


print(f"\n{greet_someone('Alice')}")
print(f"{greet_someone('Bob')}")
print(f"{greet_someone('Charlie')}")


# ============================================
# 5. 生成器 (Generator)
# ============================================

print("\n" + "=" * 50)
print("5. 生成器 (Generator)")
print("=" * 50)


# 生成器: 惰性计算，节省内存
# 使用 yield 关键字


# 5.1 基础生成器
def count_up_to(n):
    """生成 1 到 n 的数字"""
    i = 1
    while i <= n:
        yield i  # 暂停并返回值
        i += 1


print("生成器 count_up_to(5):")
for num in count_up_to(5):
    print(f"  {num}")


# 5.2 生成器表达式
squares_gen = (x**2 for x in range(5))  # 用圆括号
squares_list = [x**2 for x in range(5)]  # 用方括号是列表推导式

print(f"\n生成器表达式: {squares_gen}")
print(f"列表推导式: {squares_list}")
print(f"生成器转列表: {list(squares_gen)}")


# 5.3 无限生成器
def fibonacci():
    """无限斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n斐波那契数列前10个:")
fib = fibonacci()
for _ in range(10):
    print(f"  {next(fib)}", end="")
print()


# 5.4 yield from - 委托生成器
def chain(*iterables):
    """连接多个可迭代对象"""
    for it in iterables:
        yield from it  # 委托给子生成器


print("\nchain([1,2], [3,4], [5,6]):")
print(f"  {list(chain([1, 2], [3, 4], [5, 6]))}")


# 5.5 生成器的 send 方法
def accumulator():
    """累加器，可以通过 send 发送值"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value


print("\n累加器演示:")
acc = accumulator()
print(f"  初始值: {next(acc)}")  # 必须先 next 启动
print(f"  发送 10: {acc.send(10)}")
print(f"  发送 20: {acc.send(20)}")
print(f"  发送 30: {acc.send(30)}")


# ============================================
# 总结
# ============================================

print("\n" + "=" * 50)
print("本课总结")
print("=" * 50)
print("""
1. *args   - 接收任意位置参数，打包成元组
2. **kwargs - 接收任意关键字参数，打包成字典
3. Lambda  - 匿名函数，适合简单操作
4. 闭包    - 内部函数引用外部变量
5. 装饰器  - 不修改原函数，增加功能
6. 生成器  - 惰性计算，节省内存
""")
