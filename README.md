# PythonLearning
record python learning.

# 1. 基础

## 2.  **Jupyter Notebook**

Jupyter 官方的 Binder 平 台(介绍文档:https://mybinder.readthedocs.io/en/latest/index.html)

Google 提 供的 Google Colab 环境(介绍: https://colab.research.google.com/notebooks/welcome.ipynb)。

## Python数据结构

### 3. **列表和元组**

列表和元组，都是**一个可以放置任意数据类型的有序集合**。

```python
[1, 2, 'hello', 'world'] # 列表中同时含有 int 和 string 类型的元素
tup = ('jason', 22) # 元组中同时含有 int 和 string 类型的元素
```

**列表是动态的**，长度大小不固定，可以随意地增加、删减或者改变元素(mutable)。

**而元组是静态的**，长度大小固定，无法增加删减或者改变(immutable)。

```python
>>> l = [1, 2, 3, 4]
>>> l[3]=40
>>> l
[1, 2, 3, 40]
>>> tup = (1, 2, 3, 4)
>>> tup[3]=40
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

修改元组的方法，必须新创建一个。

```python
>>> tup = (1, 2, 3, 4)
>>> new_tup=tup+(5,)
>>> new_tup
(1, 2, 3, 4, 5)
>>> l = [1, 2, 3, 4]
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5]
```

**基本操作**

- 二者都支持负数索引，-1 表示最后一个元 素，-2 表示倒数第二个元素：

```
>>> l = [1, 2, 3, 4]
>>> l[-1]
4
>>> tup = (1, 2, 3, 4)
>>> tup[-1]
4
```

- **都支持切片操作**

```
>>> l = [1, 2, 3, 4]
>>> l[1:3]
[2, 3]
>>> tup = (1, 2, 3, 4)
>>> tup[1:3]
(2, 3)
```

- 可以**随意嵌套**

```
>>> l = [[1, 2, 3], [4, 5]]
>>> l
[[1, 2, 3], [4, 5]]
>>> tup = ((1, 2, 3), (4, 5, 6))
>>> tup
((1, 2, 3), (4, 5, 6))
```

- 相互转换

```
>>> list((1, 2, 3))
[1, 2, 3]
>>> tuple([1, 2, 3])
(1, 2, 3)
```

- 其他内置函数

```python
>>> l = [3, 2, 3, 7, 8, 1]
>>> l.count(3)
2
>>> l.index(7)
3
>>> l.reverse()
>>> l
[1, 8, 7, 3, 2, 3]
>>> l.sort()
>>> l
[1, 2, 3, 3, 7, 8]
>>> tup = (3, 2, 3, 7, 8, 1)
>>> tup.count(3)
2
>>> tup.index(7)
3
>>> list(reversed(tup))
[1, 8, 7, 3, 2, 3]
>>> sorted(tup)
[1, 2, 3, 3, 7, 8]
```

**存储方式差异**：

```java
>>> l = [1, 2, 3]
>>> l.__sizeof__()
64
>>> tup = (1, 2, 3)
>>> tup.__sizeof__()
48
```

我们可以看到list所需空间大于tuple，由于列表是动态的，所以它需要存储指针，来指向对应的元素；由于列表可变，所以需要额外存储已经分配的长度大小(8 字 节)，这样才可以实时追踪列表空间的使用情况，当空间不足时，及时分配额外空间。

下面的例子大概描述了列表空间分配的过程。我们可以看到，为了减小每次增加 / 删减 操作时空间分配的开销，Python 每次分配空间时都会额外多分配一些，这样的机制 (over-allocating)保证了其操作的高效性:增加 / 删除的时间复杂度均为 O(1)。

```python
>>> l = []
>>> l.__sizeof__()// 空列表的存储空间为 40 字节
40
>>> l.append(1)
>>> l.__sizeof__()加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
72
>>> l.append(2)
>>> l.__sizeof__()
72
>>> l.append(3)
>>> l.__sizeof__()
72
>>> l.append(4)
>>> l.__sizeof__()
72
>>> l.append(5)// 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间
>>> l.__sizeof__()
104
```

**列表和元组的性能**

元组要比列表更加轻量级一些， 所以总体上来说，元组的性能速度要略优于列表。

Python 会在后台，对静态数据做一些**资源缓存**(resource caching)。通常来说， 因为垃圾回收机制的存在，如果一些变量不被使用了，Python 就会回收它们所占用的内存，返还给操作系统，以便其他变量或其他应用使用。但是对于一些静态变量，比如元组，如果它不被使用并且占用空间不大时，Python 会暂时 缓存这部分内存。这样，下次我们再创建同样大小的元组时，Python 就可以不用再向操作 系统发出请求，去寻找内存，而是可以直接分配之前缓存的内存空间，这样就能大大加快程 序的运行速度。

- 初始化耗时对比：

![image-20201023155214180](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023155214.png)

- **索引**耗时对比：

![image-20201023155527319](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023155527.png)

**使用场景**：

存储的数据和数量不变，用元组；存储的数据或数量是可变的，用列表；

### 4. 字典和集合

字典：java中的hashmap，3.7及之后是有序的。

集合：java中的set，无序，唯一。

```python
>>> d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
>>> d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
>>> d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
>>> d4 = dict(name='jason', age=20, gender='male')
>>> d1 == d2 == d3 ==d4
True
>>> d1
{'name': 'jason', 'age': 20, 'gender': 'male'}
>>> d2
{'name': 'jason', 'age': 20, 'gender': 'male'}
>>> d3
{'name': 'jason', 'age': 20, 'gender': 'male'}
>>> d4
{'name': 'jason', 'age': 20, 'gender': 'male'}
>>> s1={1,2,3}
>>> s2 = set([1, 2, 3])
>>> s1==s2
True
```

字典访问：

```python
>>> d = {'name': 'jason', 'age': 20}
>>> d['name']
'jason'
>>> d['location']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'location'
>>> d.get('name')
'jason'
>>> d.get('location', 'null')
'null'
```

集合索引（不支持）：

```java
>>> s = {1, 2, 3}
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> 1 in s
True
>>> 10 in s
False
>>> d = {'name': 'jason', 'age': 20}
>>> 'name' in d
True
```

增删改查：

```java
>>> d = {'name': 'jason', 'age': 20}
>>> d['gender'] = 'male' # 增加元素对'gender': 'male'
>>> d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
>>> d
{'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
>>> d['dob'] = '1998-01-01' # 更新键'dob'对应的值
>>> d.pop('dob') # 删除键为'dob'的元素对
'1998-01-01'
>>> d
{'name': 'jason', 'age': 20, 'gender': 'male'}
>>> s = {1, 2, 3}
>>> s.add(4) # 增加元素 4 到集合
>>> s
{1, 2, 3, 4}
>>> s.remove(4) # 从集合中删除元素 4
>>> s
{1, 2, 3}
```

排序：

```java
>>> d = {'b': 1, 'a': 2, 'c': 10}
>>> d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
>>> d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
>>> d_sorted_by_key
[('a', 2), ('b', 1), ('c', 10)]
>>> d_sorted_by_value
[('b', 1), ('a', 2), ('c', 10)]
>>> s = {3, 4, 2, 1}
>>> sorted(s) # 对集合的元素进行升序排序
[1, 2, 3, 4]
```

性能：

```python
import time

def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


# list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:  # A
        if price not in unique_price_list:  # B
            unique_price_list.append(price)
    return len(unique_price_list)


if __name__ == '__main__':
    id = [x for x in range(0, 100000)]
    price = [x for x in range(200000, 300000)]
    products = list(zip(id, price))
    # 计算列表版本的时间
    start_using_list = time.perf_counter()
    find_unique_price_using_list(products)
    end_using_list = time.perf_counter()
    print("time elapse using list: {}".format(end_using_list - start_using_list))

    # 计算集合版本的时间
    start_using_set = time.perf_counter()
    find_unique_price_using_set(products)
    end_using_set = time.perf_counter()
    print("time elapse using set: {}".format(end_using_set - start_using_set))
```

![image-20201023163041948](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023163042.png)

老dict的数据结构：

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023164649.png" alt="image-20201023164649705" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023164749.png" alt="image-20201023164748944" style="zoom:25%;" />

新的dict结构，把索引和哈希值、键、值分开，提高空间利用率。

<img src="../../../Library/Application Support/typora-user-images/image-20201023164857663.png" alt="image-20201023164857663" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023164912.png" alt="image-20201023164912310" style="zoom:33%;" />

### 5. 字符串

```python
>>> s1 = 'hello'
>>> s2 = "hello"
>>> s3 = """hello"""
>>> s1 == s2 == s3
True
```

常用操作：

```java
>>> name = 'jason'
>>> name[0]
'j'
>>> name[1:3]
'as'
```

python字符串不可变：

```
>>> s = 'hello'
>>> s[1]='r'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```



```
>>> s='hello'
>>> s = 'H' + s[1:]
>>> s
'Hello'
>>> s='hello'
>>> s = s.replace('h', 'H')
>>> s
'Hello'
```

**特殊:str1 += str2，打破了字符串不可变的特性**。

![image-20201023170113407](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023170113.png)

时间复杂度为O(n),自从 Python2.5 开始，每次处理字符串的拼接操作时(str1 += str2)，Python 首先会检 测 str1 还有没有其他的引用。如果没有的话，就会尝试原地扩充字符串 buffer 的大小，而 不是重新分配一块内存来创建新的字符串并拷贝。

除此之外，还可以使用内置的join函数：

![image-20201023170251337](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023170251.png)

- 字符串分割函数：split

```
path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] # 返回'ads'
```

- string.strip(str)，表示去掉首尾的 str 字符串; 
- string.lstrip(str)，表示只去掉开头的 str 字符串; 
- string.rstrip(str)，表示只去掉尾部的 str 字符串。

字符串的格式化：

```java
# 最新的
print('no data available for person with id: {}, name: {}'.format(id, name))
# 旧的
print('no data available for person with id: %s, name: %s' % (id, name))
```

## 6. python的输入输出

```
>>> name = input('your name:')
your name:hjs
```

input() 函数暂停程序运行，同时等待键盘输入;直到回车被按下，函数的参数即为提示 语，输入的类型永远是字符串型(str)。

str 强制转换为 int 请用 int()，转为浮点数请用 float()。

**文件的输入与输出**：

待处理文件：

```

I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today.

I have a dream that one day down in Alabama, with its vicious racists, . . . one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers. I have a dream today.

I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together.

This is our hope. . . With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day. . . .

And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual: "Free at last! Free at last! Thank God Almighty, we are free at last!"
```

处理步骤：

读取文件；

去除所有标点符号和换行符，并把所有大写变成小写；

合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；

将结果按行输出到文件 out.txt。

```java
import re


# 你不用太关心这个函数
def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', ' ', text)

    # 转为小写
    text = text.lower()

    # 生成所有单词的列表
    word_list = text.split(' ')

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))
if __name__ == '__main__':
    open()
```

我们先要用 open() 函数拿到文件的指针。其中，第一个参数指定文件位置（相对位置或者绝对位置）；第二个参数，如果是 'r'表示读取，如果是'w' 则表示写入，当然也可以用 'rw' ，表示读写都要。a 则是一个不太常用（但也很有用）的参数，表示追加（append），这样打开的文件，如果需要写入，会从原始文件的最末尾开始写入。



**json的处理**

```java
import json

if __name__ == '__main__':
    params = {
        'symbol': '123456',
        'type': 'limit',
        'price': 123.4,
        'amount': 23
    }

    params_str = json.dumps(params)

    print('after json serialization')
    print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

    original_params = json.loads(params_str)

    print('after json deserialization')
    print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
```

![image-20201023172315663](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023172315.png)

json.dumps() 这个函数，接受 Python 的基本数据类型，然后将其序列化为 string；

json.loads() 这个函数，接受一个合法字符串，然后将其反序列化为 Python 的基本数据类型。

## 7. 条件与循环

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023172824.png" alt="image-20201023172824349" style="zoom:33%;" />

![image-20201023172903213](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023172903.png)

字典的遍历比较特殊：

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023172957.png" alt="image-20201023172957129" style="zoom:33%;" />

当我们需要使用索引来进行遍历的时候，有两种方法:

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023173105.png" alt="image-20201023173104920" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023173121.png" alt="image-20201023173121111" style="zoom:33%;" />

## 8. 异常处理

```java
import sys

try:
    f = open('file.txt', 'r')
    # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()
```

此外，还可以用with open，会自动关闭文件：

```python
with open('in.txt', 'r') as fin:
    text = fin.read()
```

**自定义异常**：

```java
class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的 string 表达形式
        return ("{} is invalid input".format(repr(self.value)))

if __name__ == '__main__':
    try:
        raise MyInputError(1)  # 抛出 MyInputError 这个异常
    except MyInputError as err:
        print('error: {}'.format(err))
```

![image-20201023174125022](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201023174125.png)

## 9. 自定义函数

TODO

## 10 匿名函数

