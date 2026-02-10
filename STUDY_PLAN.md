# Python 学习计划

## 环境信息
- Python 版本: 3.13.12
- 虚拟环境: venv
- 激活命令: `source venv/bin/activate`

---

## 第一阶段：基础语法（1-2周）

### Week 1: 核心概念
- [ ] 变量和数据类型 (int, float, str, bool, None)
- [ ] 运算符 (算术、比较、逻辑)
- [ ] 字符串操作和格式化 (f-string)
- [ ] 条件语句 (if/elif/else)
- [ ] 循环 (for, while, break, continue)

### Week 2: 数据结构
- [ ] 列表 (List) - 增删改查、切片、推导式
- [ ] 元组 (Tuple) - 不可变序列
- [ ] 字典 (Dict) - 键值对操作
- [ ] 集合 (Set) - 去重、集合运算
- [ ] 函数定义和调用

**练习文件**: `01_basics.py`

---

## 第二阶段：进阶语法（2-3周）

### Week 3: 函数进阶
- [ ] 参数类型 (*args, **kwargs)
- [ ] Lambda 表达式
- [ ] 装饰器 (Decorator)
- [ ] 闭包 (Closure)
- [ ] 生成器 (Generator)

### Week 4: 面向对象
- [ ] 类和对象
- [ ] 继承和多态
- [ ] 魔术方法 (__init__, __str__, __repr__)
- [ ] 属性和方法 (@property, @classmethod, @staticmethod)
- [ ] 数据类 (dataclass)

### Week 5: 模块和包
- [ ] 模块导入 (import)
- [ ] 包结构
- [ ] __init__.py 作用
- [ ] 相对导入和绝对导入

---

## 第三阶段：实用技能（2-3周）

### Week 6: 文件和异常
- [ ] 文件读写 (with open)
- [ ] JSON/YAML 处理
- [ ] 异常处理 (try/except/finally)
- [ ] 自定义异常
- [ ] 日志 (logging)

### Week 7: 常用标准库
- [ ] os / pathlib - 文件系统
- [ ] datetime - 日期时间
- [ ] re - 正则表达式
- [ ] collections - 高级数据结构
- [ ] itertools - 迭代器工具

### Week 8: 网络和并发
- [ ] requests - HTTP 请求
- [ ] 多线程 (threading)
- [ ] 多进程 (multiprocessing)
- [ ] 异步编程 (asyncio)

---

## 第四阶段：专项方向（按兴趣选择）

### Web 开发
- [ ] Flask / FastAPI 基础
- [ ] REST API 设计
- [ ] 数据库 (SQLite/PostgreSQL)
- [ ] ORM (SQLAlchemy)

### 数据分析
- [ ] NumPy - 数值计算
- [ ] Pandas - 数据处理
- [ ] Matplotlib - 数据可视化
- [ ] Jupyter Notebook

### 自动化脚本
- [ ] 爬虫 (BeautifulSoup/Scrapy)
- [ ] 自动化测试 (pytest)
- [ ] 命令行工具 (argparse/click)

---

## 学习资源

### 在线文档
- Python 官方文档: https://docs.python.org/zh-cn/3/
- Real Python: https://realpython.com/

### 练习平台
- LeetCode: https://leetcode.cn/
- Codewars: https://www.codewars.com/

### 推荐书籍
- 《Python编程：从入门到实践》
- 《流畅的Python》(进阶)

---

## 学习建议

1. **每天写代码** - 至少 30 分钟实践
2. **多动手实验** - 不要只看，要亲自敲代码
3. **做小项目** - 学完基础后做个小工具练手
4. **阅读源码** - 看优秀项目是怎么写的
5. **使用 ipython** - 交互式探索很高效

```bash
# 激活环境
source venv/bin/activate

# 运行学习文件
python 01_basics.py

# 交互式学习
ipython
```
