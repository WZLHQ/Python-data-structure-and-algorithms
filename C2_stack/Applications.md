# 栈的应用

## 应用1：简单括号匹配

首先，每个开括号要恰好对应一个闭括号；其次，每对开闭括号要正确嵌套。

最新打开的左括号应该匹配最先遇到的右括号。

尝试看看此[视频](https://www.bilibili.com/video/BV1uxCzYrEvK?spm_id_from=333.788.videopod.sections&vd_source=5a390d9ceffbe62da24960caba35e434)的题目描述。

## 应用2：十进制转换为二进制

Q：搞清楚原理

```python
from src.Stack import Stack

def decimal2binary(item):
	S=Stack()
	while item>0:
		rem=item%2
		S.push(rem)
		item = item//2
	B=""
	while not S.isEmpty():
		B+=str(S.pop())
	return B

# test
print(decimal2binary(233))
```

### 练习进阶：将十进制转换为十六以下任意进制

```python
# TODO
```

## 应用3：通用的中缀转后缀表达式算法（只带加减乘除）

```python
# TODO
from src.Stack import Stack

def infix2postfix(item):
	orders={"*":1,"/":1,"+":2,"-":2}

```

### 进阶练习：带加减乘除与括号

```python
# TODO
```

## 应用4：后缀表达式求值

```python
# TODO
```
