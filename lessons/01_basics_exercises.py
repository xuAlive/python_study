"""
Python 基础语法练习题
======================

运行方式：python lessons/01_basics_exercises.py
完成每道题后运行，查看是否通过测试
"""

# ============================================
# 练习1: 变量和数据类型
# ============================================
# 要求: 创建以下变量
# - my_name: 你的名字 (字符串)
# - my_age: 你的年龄 (整数)
# - my_height: 你的身高，单位米 (浮点数，如 1.75)
# - is_student: 你是否是学生 (布尔值)

# 在下面写代码:
my_name = None  # 改成你的名字
my_age = None  # 改成你的年龄
my_height = None  # 改成你的身高
is_student = None  # 改成 True 或 False
print(f"my_name",my_name:="王木木")
print(f"my_age",my_age:=18)
print(f"my_height",my_height:=1.75)
print(f"is_student",is_student:=True)


# ============================================
# 练习2: 字符串操作
# ============================================
# 要求: 给定字符串 text，完成以下操作

text = "  Hello, Python World!  "

# 2.1 去除首尾空格，赋值给 text_stripped
text_stripped = None  # 提示: strip()
text_stripped = text.strip()
print(f"text_stripped",text_stripped)

# 2.2 将字符串转为全大写，赋值给 text_upper
text_upper = None  # 提示: upper()
text_upper = text.upper()
print(f"text_upper",text_upper)

# 2.3 统计字母 'o' 出现的次数，赋值给 count_o
count_o = None  # 提示: count()
count_o = text.count("o")
print(f"count_o",count_o)
count_l=text.count("l")
print(f"count_l",count_l)

# 2.4 将 "Python" 替换为 "Java"，赋值给 text_replaced
text_replaced = None  # 提示: replace()
text_replaced = text.replace("Python","Java")


# ============================================
# 练习3: 列表操作
# ============================================
# 要求: 对列表进行操作

numbers = [5, 2, 8, 1, 9, 3, 7]

# 3.1 获取列表长度，赋值给 list_length
list_length = None  # 提示: len()
list_length = len(numbers)
print(f"list_length",list_length)
# 3.2 获取最大值，赋值给 max_num
max_num = None  # 提示: max()
max_num = max(numbers)
print(f"max_num",max_num)

# 3.3 获取最小值，赋值给 min_num
min_num = None  # 提示: min()
min_num = min(numbers)
print(f"min_num",min_num)

# 3.4 计算所有数字的和，赋值给 total
total = None  # 提示: sum()
total = sum(numbers)
print(f"total",total)

# 3.5 将列表排序（从小到大），赋值给 sorted_numbers
sorted_numbers = None  # 提示: sorted()
sorted_numbers = sorted(numbers)

# 3.6 使用列表推导式，获取所有偶数，赋值给 even_numbers
even_numbers = None  # 提示: [x for x in numbers if x % 2 == 0]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"even_numbers",even_numbers)

# ============================================
# 练习4: 字典操作
# ============================================
# 要求: 创建和操作字典

# 4.1 创建一个字典 student，包含以下信息:
#     - name: "小明"
#     - age: 18
#     - grade: "高三"
#     - scores: {"语文": 90, "数学": 95, "英语": 88}
student = None  # 创建字典
student = {
    "name": "小明",
    "age": 18,
    "grade": "高三",
    "scores": {"语文": 90, "数学": 95, "英语": 88}
}
# 4.2 从 student 中获取数学成绩，赋值给 math_score
math_score = None  # 提示: student["scores"]["数学"]
math_score = student["scores"]["数学"]

# 4.3 给 student 添加一个新字段 "city": "上海"
# 提示: student["city"] = "上海"
student["city"] = "上海"

# ============================================
# 练习5: 条件语句
# ============================================
# 要求: 根据分数判断等级

score = 75

# 完成函数: 根据分数返回等级
# >= 90: "A"
# >= 80: "B"
# >= 70: "C"
# >= 60: "D"
# < 60: "F"


def get_grade(score):
    # 在下面写代码:
    if score>=90:
      return "A"
    elif score>=80:
      return "B"
    elif score>=70:
      return "C"
    elif score>=60:
      return "D"
    else:
      return "F"


grade = get_grade(score)


# ============================================
# 练习6: 循环
# ============================================

# 6.1 使用 for 循环计算 1 到 100 的和，赋值给 sum_1_to_100
sum_1_to_100 = None  # 提示: for i in range(1, 101)

for i in range(1,101):
  sum_1_to_100 = 0 if sum_1_to_100==None else sum_1_to_100
  sum_1_to_100 += i

print(f"sum_1_to_100",sum_1_to_100)
# 6.2 使用 for 循环找出 1-50 中所有能被 3 整除的数，存入列表 divisible_by_3
divisible_by_3 = None  # 提示: 列表推导式或 for 循环 + append
divisible_by_3 = []
for i in range(1,51):
  if i%3==0:
    divisible_by_3.append(i)

# ============================================
# 练习7: 函数
# ============================================

# 7.1 编写函数 calculate_area，计算圆的面积
# 参数: radius (半径)
# 返回: 面积 (公式: 3.14159 * radius * radius)


def calculate_area(radius):
    # 在下面写代码:
    return 3.14159* radius**2


# 7.2 编写函数 is_palindrome，判断字符串是否是回文
# 回文: 正着读和倒着读一样，如 "level", "noon"
# 参数: s (字符串)
# 返回: True 或 False


def is_palindrome(s):
    # 在下面写代码:
    # 提示: s[::-1] 可以反转字符串
    return s==s[::-1]


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
    print("\n【练习1: 变量和数据类型】")
    if my_name is not None and isinstance(my_name, str):
        print(f"  ✓ my_name = '{my_name}'")
        passed += 1
    else:
        print("  ✗ my_name 未完成")
        failed += 1

    if my_age is not None and isinstance(my_age, int):
        print(f"  ✓ my_age = {my_age}")
        passed += 1
    else:
        print("  ✗ my_age 未完成")
        failed += 1

    if my_height is not None and isinstance(my_height, float):
        print(f"  ✓ my_height = {my_height}")
        passed += 1
    else:
        print("  ✗ my_height 未完成")
        failed += 1

    if is_student is not None and isinstance(is_student, bool):
        print(f"  ✓ is_student = {is_student}")
        passed += 1
    else:
        print("  ✗ is_student 未完成")
        failed += 1

    # 练习2 测试
    print("\n【练习2: 字符串操作】")
    if text_stripped == "Hello, Python World!":
        print(f"  ✓ text_stripped 正确")
        passed += 1
    else:
        print(f"  ✗ text_stripped 错误，期望 'Hello, Python World!'")
        failed += 1

    if text_upper == "  HELLO, PYTHON WORLD!  ":
        print(f"  ✓ text_upper 正确")
        passed += 1
    else:
        print(f"  ✗ text_upper 错误")
        failed += 1

    if count_o == 3:
        print(f"  ✓ count_o = 2 正确")
        passed += 1
    else:
        print(f"  ✗ count_o 错误，期望 2")
        failed += 1

    if text_replaced and "Java" in text_replaced:
        print(f"  ✓ text_replaced 正确")
        passed += 1
    else:
        print(f"  ✗ text_replaced 错误")
        failed += 1

    # 练习3 测试
    print("\n【练习3: 列表操作】")
    if list_length == 7:
        print(f"  ✓ list_length = 7 正确")
        passed += 1
    else:
        print(f"  ✗ list_length 错误，期望 7")
        failed += 1

    if max_num == 9:
        print(f"  ✓ max_num = 9 正确")
        passed += 1
    else:
        print(f"  ✗ max_num 错误，期望 9")
        failed += 1

    if min_num == 1:
        print(f"  ✓ min_num = 1 正确")
        passed += 1
    else:
        print(f"  ✗ min_num 错误，期望 1")
        failed += 1

    if total == 35:
        print(f"  ✓ total = 35 正确")
        passed += 1
    else:
        print(f"  ✗ total 错误，期望 35")
        failed += 1

    if sorted_numbers == [1, 2, 3, 5, 7, 8, 9]:
        print(f"  ✓ sorted_numbers 正确")
        passed += 1
    else:
        print(f"  ✗ sorted_numbers 错误")
        failed += 1

    if even_numbers is not None and sorted(even_numbers) == [2, 8]:
        print(f"  ✓ even_numbers 正确")
        passed += 1
    else:
        print(f"  ✗ even_numbers 错误，期望 [2, 8]")
        failed += 1

    # 练习4 测试
    print("\n【练习4: 字典操作】")
    if student and student.get("name") == "小明":
        print(f"  ✓ student 字典创建正确")
        passed += 1
    else:
        print(f"  ✗ student 字典未完成")
        failed += 1

    if math_score == 95:
        print(f"  ✓ math_score = 95 正确")
        passed += 1
    else:
        print(f"  ✗ math_score 错误，期望 95")
        failed += 1

    if student and student.get("city") == "上海":
        print(f"  ✓ student['city'] 添加正确")
        passed += 1
    else:
        print(f"  ✗ student['city'] 未添加")
        failed += 1

    # 练习5 测试
    print("\n【练习5: 条件语句】")
    if get_grade(95) == "A" and get_grade(85) == "B" and get_grade(75) == "C":
        print(f"  ✓ get_grade 函数正确")
        passed += 1
    else:
        print(f"  ✗ get_grade 函数错误")
        failed += 1

    # 练习6 测试
    print("\n【练习6: 循环】")
    if sum_1_to_100 == 5050:
        print(f"  ✓ sum_1_to_100 = 5050 正确")
        passed += 1
    else:
        print(f"  ✗ sum_1_to_100 错误，期望 5050")
        failed += 1

    expected_div3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
    if divisible_by_3 and sorted(divisible_by_3) == expected_div3:
        print(f"  ✓ divisible_by_3 正确")
        passed += 1
    else:
        print(f"  ✗ divisible_by_3 错误")
        failed += 1

    # 练习7 测试
    print("\n【练习7: 函数】")
    area = calculate_area(5)
    if area and abs(area - 78.53975) < 0.01:
        print(f"  ✓ calculate_area(5) = {area:.2f} 正确")
        passed += 1
    else:
        print(f"  ✗ calculate_area 错误，期望约 78.54")
        failed += 1

    if is_palindrome("level") == True and is_palindrome("hello") == False:
        print(f"  ✓ is_palindrome 函数正确")
        passed += 1
    else:
        print(f"  ✗ is_palindrome 函数错误")
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
