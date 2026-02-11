"""
Python 入门学习 - 第一课：基础语法
=====================================

运行方式：
1. 激活虚拟环境：source venv/bin/activate
2. 运行脚本：python 01_basics.py
3. 或使用交互式：ipython
"""

# ============================================
# 1. 变量和数据类型
# ============================================

# 整数 (int)
age = 25
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数 (float)
price = 19.99
print(f"价格: {price}, 类型: {type(price)}")

# 字符串 (str)
name = "Python学习者"
print(f"名字: {name}, 类型: {type(name)}")

# 布尔值 (bool)
is_student = True
print(f"是否学生: {is_student}, 类型: {type(is_student)}")

# 空值 (None)
nothing = None
print(f"空值: {nothing}, 类型: {type(nothing)}")

print("\n" + "=" * 50)

# ============================================
# 2. 基本运算
# ============================================

a, b = 10, 3

print(f"加法: {a} + {b} = {a + b}")
print(f"减法: {a} - {b} = {a - b}")
print(f"乘法: {a} * {b} = {a * b}")
print(f"除法: {a} / {b} = {a / b}")
print(f"整除: {a} // {b} = {a // b}")
print(f"取余: {a} % {b} = {a % b}")
print(f"幂运算: {a} ** {b} = {a ** b}")

print("\n" + "=" * 50)

# ============================================
# 3. 字符串操作
# ============================================

text = "Hello, Python!"

print(f"原字符串: {text}")
print(f"长度: {len(text)}")
print(f"大写: {text.upper()}")
print(f"小写: {text.lower()}")
print(f"替换: {text.replace('Python', 'World')}")
print(f"分割: {text.split(', ')}")
print(f"索引[0]: {text[0]}")
print(f"切片[0:5]: {text[0:5]}")
print(f"反转: {text[::-1]}")

print("\n" + "=" * 50)

# ============================================
# 4. 列表 (List)
# ============================================

fruits = ["苹果", "香蕉", "橙子"]
print(f"水果列表: {fruits}")

# 添加元素
fruits.append("葡萄")
print(f"添加后: {fruits}")

# 访问元素
print(f"第一个: {fruits[0]}")
print(f"最后一个: {fruits[-1]}")

# 列表推导式
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"原数字: {numbers}")
print(f"平方: {squares}")

print("\n" + "=" * 50)

# ============================================
# 5. 字典 (Dict)
# ============================================

person = {
    "name": "张三",
    "age": 28,
    "city": "北京",
}

print(f"人员信息: {person}")
print(f"名字: {person['name']}")
print(f"所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")

# 添加/修改
person["job"] = "工程师"
print(f"添加职业后: {person}")

print("\n" + "=" * 50)

# ============================================
# 6. 条件语句
# ============================================

score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数: {score}, 等级: {grade}")

# 三元表达式
result = "成年" if age >= 18 else "未成年"
print(f"年龄 {age}: {result}")

print("\n" + "=" * 50)

# ============================================
# 7. 循环
# ============================================

# for 循环
print("for 循环遍历列表:")
for fruit in fruits:
    print(f"  - {fruit}")

# range 循环
print("\nrange(5) 循环:")
for i in range(5):
    print(f"  i = {i}")

# while 循环
print("\nwhile 循环:")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1

# enumerate 带索引遍历
print("\nenumerate 遍历:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\n" + "=" * 50)

# ============================================
# 8. 函数
# ============================================


def greet(name: str, greeting: str = "你好") -> str:
    """问候函数

    Args:
        name: 被问候的人名
        greeting: 问候语，默认为"你好"

    Returns:
        完整的问候语句
    """
    return f"{greeting}, {name}!"


print(greet("小明"))
print(greet("小红", "早上好"))


# 带多个返回值的函数
def calculate(a: int, b: int) -> tuple:
    """返回加减乘除的结果"""
    return a + b, a - b, a * b, a / b if b != 0 else None


add, sub, mul, div = calculate(10, 3)
print(f"calculate(10, 3) = 加:{add}, 减:{sub}, 乘:{mul}, 除:{div:.2f}")

print("\n" + "=" * 50)

# ============================================
# 9. 异常处理
# ============================================


def safe_divide(a: float, b: float) -> float | None:
    """安全除法，处理除零错误"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误: 除数不能为零!")
        return None
    finally:
        print("除法运算完成")


print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

print("\n" + "=" * 50)

# ============================================
# 10. 文件操作示例
# ============================================

# 写入文件
with open("test_output.txt", "w", encoding="utf-8") as f:
    f.write("这是测试文件\n")
    f.write("Python 文件操作很简单\n")

# 读取文件
with open("test_output.txt", encoding="utf-8") as f:
    content = f.read()
    print("文件内容:")
    print(content)

print("=" * 50)
print("恭喜! 你已完成 Python 基础语法学习!")
print("=" * 50)
