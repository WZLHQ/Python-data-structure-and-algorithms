



## 引子

一个小算法题：如果a+b+c=1000，且a^2+b^2=c^2，abc均为自然数，如何求出所有abc可能的组合？

解法1：

```python
import time
start_time=time.time()
for a in range(1001):
	for b in range(1001):
		for c in range(1001):
            if a+b+c==1000 and a**2+b**2==c**2:
                print(a,b,c)
end_time=time.time()
print("complete time: %f" % (end_time-start_time))
                
```

解法2：

```python
import time
start_time=time.time()
for a in range(1001):
    for b in range(1001):
        c=1000-a-b
        if a**2+b**2==c**2:
            print(a,b,c)
end_time=time.time()
print("complete time: %f" % (end_time-start_time))
```

解法1和2告诉我们不同的算法有需要不同的时间，但如何客观地描述出算法的耗时情况呢？



## 时间复杂度与大O表示法

用于描述算法的时间效率，一般使用最坏时间复杂度。



## 时间复杂度的几条基本计算规则

1. 基本操作，即只有常数项，认为其时间复杂度为O(1)
2. 顺序结构，时间复杂度按加法进行
3. 条件结构，时间复杂度按加法进行
4. 循环结构，时间复杂度取最大值
5. 判断一个算法的效率时，往往只需要关注操作数量的最高次项，其他次要项和常数项可以忽略
6. 在没有特殊说明，都采用最坏时间复杂度

























