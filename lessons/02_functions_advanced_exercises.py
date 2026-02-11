"""
Python 函数进阶练习题
======================

运行方式：python lessons/02_functions_advanced_exercises.py
完成每道题后运行，查看是否通过测试
"""

# ============================================
# 练习1: *args 和 **kwargs
# ============================================

# 1.1 编写函数 calculate_average，接收任意数量的数字，返回平均值
# 示例: calculate_average(1, 2, 3, 4, 5) -> 3.0


def calculate_average(*args):
    # 在下面写代码:
    # 提示: sum(args) / len(args)
    pass


# 1.2 编写函数 create_profile，接收任意关键字参数，返回格式化的字符串
# 示例: create_profile(name="张三", age=25) -> "name: 张三, age: 25"
# 提示: 用 ", ".join() 连接


def create_profile(**kwargs):
    # 在下面写代码:
    pass


# 1.3 编写函数 merge_dicts，接收任意数量的字典，合并成一个字典返回
# 示例: merge_dicts({"a": 1}, {"b": 2}, {"c": 3}) -> {"a": 1, "b": 2, "c": 3}


def merge_dicts(*dicts):
    # 在下面写代码:
    # 提示: 遍历每个字典，使用 update() 或 **解包
    pass


# ============================================
# 练习2: Lambda 表达式
# ============================================

# 2.1 使用 lambda 创建一个函数，计算两个数的乘积
multiply = None  # lambda x, y: ...

# 2.2 使用 lambda 和 sorted，按字符串长度排序
words = ["apple", "pie", "banana", "cat"]
sorted_by_length = None  # sorted(words, key=lambda ...)

# 2.3 使用 lambda 和 filter，过滤出所有正数
numbers = [-3, -1, 0, 2, 5, -4, 8]
positive_numbers = None  # list(filter(lambda ..., numbers))

# 2.4 使用 lambda 和 map，将列表中每个字符串转为大写
fruits = ["apple", "banana", "cherry"]
upper_fruits = None  # list(map(lambda ..., fruits))


# ============================================
# 练习3: 闭包
# ============================================

# 3.1 编写闭包 make_power，创建一个幂函数
# 示例:
#   square = make_power(2)
#   cube = make_power(3)
#   square(5) -> 25
#   cube(2) -> 8


def make_power(n):
    # 在下面写代码:
    # 提示: 返回一个内部函数，该函数计算 x ** n
    pass


# 3.2 编写闭包 make_greeting，创建不同语言的问候函数
# 示例:
#   greet_cn = make_greeting("你好")
#   greet_en = make_greeting("Hello")
#   greet_cn("小明") -> "你好, 小明!"
#   greet_en("Tom") -> "Hello, Tom!"


def make_greeting(greeting):
    # 在下面写代码:
    pass


# ============================================
# 练习4: 装饰器
# ============================================

from functools import wraps
import time

# 4.1 编写装饰器 log_call，在函数调用前后打印日志
# 输出格式:
#   ">>> 调用 函数名"
#   "<<< 函数名 返回: 返回值"


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在下面写代码:
        # 提示:
        # 1. print(f">>> 调用 {func.__name__}")
        # 2. 调用原函数获取结果
        # 3. print(f"<<< {func.__name__} 返回: {result}")
        # 4. 返回结果
        pass

    return wrapper


# 4.2 编写带参数的装饰器 retry，在函数失败时重试指定次数
# 示例: @retry(times=3) 表示最多重试3次


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 在下面写代码:
            # 提示: 用 for 循环尝试 times 次
            # 成功则返回结果，失败则捕获异常继续
            # 所有尝试失败后抛出最后的异常
            pass

        return wrapper

    return decorator


# ============================================
# 练习5: 生成器
# ============================================

# 5.1 编写生成器 countdown，从 n 倒数到 1
# 示例: list(countdown(5)) -> [5, 4, 3, 2, 1]


def countdown(n):
    # 在下面写代码:
    # 提示: while n > 0: yield n; n -= 1
    pass


# 5.2 编写生成器 even_numbers，生成无限偶数序列 (0, 2, 4, 6, ...)


def even_numbers():
    # 在下面写代码:
    # 提示: n = 0; while True: yield n; n += 2
    pass


# 5.3 编写生成器 take，从可迭代对象中取前 n 个元素
# 示例: list(take(3, [1,2,3,4,5])) -> [1, 2, 3]


def take(n, iterable):
    # 在下面写代码:
    # 提示: 用 for 循环和计数器，或用 enumerate
    pass


# 5.4 使用生成器表达式，创建一个生成器，生成 1-10 的立方
# 即: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000
cubes_gen = None  # (x**3 for x in range(...))


# ============================================
# 测试代码 (不要修改)
# ============================================


def run_tests():
    print("=" * 50)
    print("开始测试...")
    print("=" * 50)

    passed = 0
    failed = 0

    # 练习1 测试
    print("\n【练习1: *args 和 **kwargs】")

    try:
        result = calculate_average(1, 2, 3, 4, 5)
        if result == 3.0:
            print("  ✓ calculate_average 正确")
            passed += 1
        else:
            print(f"  ✗ calculate_average 错误，期望 3.0，得到 {result}")
            failed += 1
    except Exception as e:
        print(f"  ✗ calculate_average 出错: {e}")
        failed += 1

    try:
        result = create_profile(name="张三", age=25)
        if result and "name: 张三" in result and "age: 25" in result:
            print("  ✓ create_profile 正确")
            passed += 1
        else:
            print(f"  ✗ create_profile 错误")
            failed += 1
    except Exception as e:
        print(f"  ✗ create_profile 出错: {e}")
        failed += 1

    try:
        result = merge_dicts({"a": 1}, {"b": 2}, {"c": 3})
        if result == {"a": 1, "b": 2, "c": 3}:
            print("  ✓ merge_dicts 正确")
            passed += 1
        else:
            print(f"  ✗ merge_dicts 错误")
            failed += 1
    except Exception as e:
        print(f"  ✗ merge_dicts 出错: {e}")
        failed += 1

    # 练习2 测试
    print("\n【练习2: Lambda 表达式】")

    if multiply and multiply(3, 4) == 12:
        print("  ✓ multiply 正确")
        passed += 1
    else:
        print("  ✗ multiply 错误，期望 multiply(3,4) = 12")
        failed += 1

    if sorted_by_length == ["pie", "cat", "apple", "banana"]:
        print("  ✓ sorted_by_length 正确")
        passed += 1
    else:
        print(f"  ✗ sorted_by_length 错误，期望 ['pie', 'cat', 'apple', 'banana']")
        failed += 1

    if positive_numbers and sorted(positive_numbers) == [2, 5, 8]:
        print("  ✓ positive_numbers 正确")
        passed += 1
    else:
        print(f"  ✗ positive_numbers 错误，期望 [2, 5, 8]")
        failed += 1

    if upper_fruits == ["APPLE", "BANANA", "CHERRY"]:
        print("  ✓ upper_fruits 正确")
        passed += 1
    else:
        print(f"  ✗ upper_fruits 错误，期望 ['APPLE', 'BANANA', 'CHERRY']")
        failed += 1

    # 练习3 测试
    print("\n【练习3: 闭包】")

    try:
        square = make_power(2)
        cube = make_power(3)
        if square and cube and square(5) == 25 and cube(2) == 8:
            print("  ✓ make_power 正确")
            passed += 1
        else:
            print("  ✗ make_power 错误")
            failed += 1
    except Exception as e:
        print(f"  ✗ make_power 出错: {e}")
        failed += 1

    try:
        greet_cn = make_greeting("你好")
        greet_en = make_greeting("Hello")
        if greet_cn and greet_cn("小明") == "你好, 小明!" and greet_en("Tom") == "Hello, Tom!":
            print("  ✓ make_greeting 正确")
            passed += 1
        else:
            print("  ✗ make_greeting 错误")
            failed += 1
    except Exception as e:
        print(f"  ✗ make_greeting 出错: {e}")
        failed += 1

    # 练习4 测试
    print("\n【练习4: 装饰器】")

    try:
        @log_call
        def test_add(a, b):
            return a + b

        import io
        import sys

        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        result = test_add(1, 2)
        output = buffer.getvalue()
        sys.stdout = old_stdout

        if result == 3 and "调用" in output and "返回" in output:
            print("  ✓ log_call 正确")
            passed += 1
        else:
            print("  ✗ log_call 错误")
            failed += 1
    except Exception as e:
        print(f"  ✗ log_call 出错: {e}")
        failed += 1

    try:
        call_count = 0

        @retry(times=3)
        def flaky_function():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("失败")
            return "成功"

        result = flaky_function()
        if result == "成功" and call_count == 3:
            print("  ✓ retry 正确")
            passed += 1
        else:
            print("  ✗ retry 错误")
            failed += 1
    except Exception as e:
        print(f"  ✗ retry 出错: {e}")
        failed += 1

    # 练习5 测试
    print("\n【练习5: 生成器】")

    try:
        result = list(countdown(5))
        if result == [5, 4, 3, 2, 1]:
            print("  ✓ countdown 正确")
            passed += 1
        else:
            print(f"  ✗ countdown 错误，期望 [5,4,3,2,1]")
            failed += 1
    except Exception as e:
        print(f"  ✗ countdown 出错: {e}")
        failed += 1

    try:
        gen = even_numbers()
        result = [next(gen) for _ in range(5)]
        if result == [0, 2, 4, 6, 8]:
            print("  ✓ even_numbers 正确")
            passed += 1
        else:
            print(f"  ✗ even_numbers 错误，期望 [0,2,4,6,8]")
            failed += 1
    except Exception as e:
        print(f"  ✗ even_numbers 出错: {e}")
        failed += 1

    try:
        result = list(take(3, [1, 2, 3, 4, 5]))
        if result == [1, 2, 3]:
            print("  ✓ take 正确")
            passed += 1
        else:
            print(f"  ✗ take 错误，期望 [1,2,3]")
            failed += 1
    except Exception as e:
        print(f"  ✗ take 出错: {e}")
        failed += 1

    try:
        if cubes_gen is not None:
            result = list(cubes_gen)
            expected = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
            if result == expected:
                print("  ✓ cubes_gen 正确")
                passed += 1
            else:
                print(f"  ✗ cubes_gen 错误")
                failed += 1
        else:
            print("  ✗ cubes_gen 未完成")
            failed += 1
    except Exception as e:
        print(f"  ✗ cubes_gen 出错: {e}")
        failed += 1

    # 总结
    print("\n" + "=" * 50)
    print(f"测试完成: {passed} 通过, {failed} 未通过")
    if failed == 0:
        print("🎉 恭喜! 全部通过!")
    else:
        print("继续加油! 完成剩余练习题")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
