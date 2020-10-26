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

- 函数嵌套：

函数的嵌套能够保证内部函数的隐私：

```python
def connect_DB():
    def get_DB_configuration():
        return host, username, password
    conn = connector.connect(get_DB_configuration())
    return conn
```

提高程序的运行效率,因为在计算之前，需要检查输入是否合法， 所以我写成了函数嵌套的形式，这样一来，输入是否合法就只用检查一次。而如果我们不使 用函数嵌套，那么每调用一次递归便会检查一次，这是没有必要的，也会降低程序的运行效率。

```python
def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input - 1)

    return inner_factorial(input)
```



- 闭包：

```python
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of
if __name__ == '__main__':
    square = nth_power(2)
    print(square)
    print(square(2))
    cube = nth_power(3)
    print(cube)
    print(cube(3))
    
<function nth_power.<locals>.exponent_of at 0x105e3b378>
4
<function nth_power.<locals>.exponent_of at 0x105e3b268>
27
```

这里外部函数 nth_power() 返回值，是函数 exponent_of()，而不是一个具体的数值。需 要注意的是，在执行完square = nth_power(2)和cube = nth_power(3)后，外部 函数 nth_power() 的参数 exponent，仍然会被内部函数 exponent_of() 记住。这样，之 后我们调用 square(2) 或者 cube(2) 时，程序就能顺利地输出结果，而不会报错说参数 exponent 没有定义了。

使用闭包的原因？

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201026134507.png" alt="image-20201026134501989" style="zoom:33%;" />

函数开头需要做一些额外工作，而你又需要多次调 用这个函数时，将那些额外工作的代码放在外部函数，就可以减少多次调用导致的不必要的 开销，提高程序的运行效率。

## 10 匿名函数

```
lambda argument1, argument2,... argumentN : expression
```

```
>>> square = lambda x: x**2
>>> square(3)
9
```

**lambda 是一个表达式(expression)，并不是一个语句(statement)**

所谓的表达式，就是用一系列“公式”去表达一个东西，比如x + 2、 x**2等等;

而所谓的语句，则一定是完成了某些功能，比如赋值语句x = 1完成了赋值，print 语句 print(x)完成了打印，条件语句 if x < 0:完成了选择功能等等。

lambda 可以用在一些常规函数 def 不能用的地方，比如，lambda 可以用在列表内 部，而常规函数却不能:

```
>>> [(lambda x: x*x)(x) for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

lambda 可以被用作某些函数的参数，而常规函数 def 也不能:

```java
>>> l = [(1, 20), (3, 0), (9, 10), (2, -1)]
>>> l.sort(key=lambda x: x[1])
>>> print(l)
[(2, -1), (3, 0), (9, 10), (1, 20)]
>>> l
[(2, -1), (3, 0), (9, 10), (1, 20)]
```

常规函数 def 必须通过其函数名被调用，因此必须首先被定义。但是作为一个表达式的 lambda，返回的函数对象就不需要名字了。



函数式编程：

TODO

## 11. **面向对象(上)**

## 12. 面向对象（下）

```java

class SearchEngineBase(object):
    def __init__(self):
        pass
    # 负责读取文件内容，将文件路径作为 ID，连同内容一起送到 process_corpus 中。
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    # 对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')
    # 给定一个询问，处理询问，再通过索引检索，然后返回。
    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)



class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

if __name__ == '__main__':
    search_engine = SimpleEngine()
    main(search_engine)
```

![image-20201026153805939](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201026153806.png)



查询语句：

```main

import re

class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)

search_engine = BOWEngine()
main(search_engine)
```

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201026154054.png" alt="image-20201026154053889" style="zoom:50%;" />

## 13. python模块化

```python
# utils.py
def get_sum(a, b):
    return a + b
# class_utils.py
from audioop import reverse

class Encoder(object):
    def encode(self, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reverse(list(s)))
      
# main.py
from utils import get_sum
from class_utils import *

if __name__ == '__main__':
    print(get_sum(1, 2))
    encoder = Encoder()
    decoder = Decoder()
    print(encoder.encode('abcde'))
    print(encoder.encode('edcba'))
```

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201026155256.png" alt="image-20201026155256252" style="zoom:33%;" />



1. 通过绝对路径和相对路径，我们可以 import 模块;
2. 在大型工程中模块化非常重要，模块的索引要通过绝对路径来做，而绝对路径从程序的根目录开始;

3. 记着巧用if __name__ == '__main__'来避开 import 时执行。





# 2. 进阶

## 15. **Python**对象的比较、拷贝

== vs is：

'=='操作符比较对象之间的值是否相等，'is'操作符比较的是对象的身份标识是否相等，即它们是否是同一个对象，是否指向同一个内存地址。

```python
>>> a = 10
>>> b = 10
>>> a == b
True
>>> id(a)
4411706560
>>> id(b)
4411706560
>>> a is b
True
```

对于整型数字来说，以上a is b为 True 的结论，只适用于 -5 到 256 范围内的数字。

```
>>> a = 257
>>> b=257
>>> a is b
False
>>> a==b
True
```

出于对性能优化的考虑，Python 内部会对 -5 到 256 的整型维持一个数组，起到一个缓存的作用。

比较操作符'is'的速度效率，通常要优于'=='。因为'is'操作符不能被重载，这样，Python 就不需要去寻找，程序中是否有其他地方重载了比较操作符，并去调用。执行比较操作符'is'，就仅仅是比较两个变量的 ID 而已。但是'=='操作符却不同，执行a == b相当于是去执行a.__eq__(b)，而 Python 大部分的数据类型都会去重载__eq__这个函数，其内部的处理通常会复杂一些。比如，对于列表，__eq__函数会去遍历列表中的元素，比较它们的顺序和值是否相等。不过，对于不可变（immutable）的变量，如果我们之前用'=='或者'is'比较过，结果是不是就一直不变了呢？

```python
>>> t1 = (1, 2, [3, 4])
>>> t2 = (1, 2, [3, 4])
>>> t1 == t2
True
>>> t1[-1].append(5)
>>> t1
(1, 2, [3, 4, 5])
>>> t1 == t2
False
```

元组是不可变的，但元组可以嵌套，它里面的元素可以是列表类型，列表是可变的，所以如果我们修改了元组中的某个可变元素，那么元组本身也就改变了，之前用'is'或者'=='操作符取得的结果，可能就不适用了。

**深拷贝和浅拷贝**

Python 中的浅拷贝（shallow copy）和深度拷贝（deep copy）

```java
>>> l1 = [1, 2, 3]
>>> l2 = list(l1)
>>> l2
[1, 2, 3]
>>> l1==l2
True
>>> l1 is l2
False
>>> s1 = set([1, 2, 3])
>>> s2 = set(s1)
>>> s2
{1, 2, 3}
>>> s1 == s2
True
>>> s1 is s2
False
```

l2 就是 l1 的浅拷贝，s2 是 s1 的浅拷贝。当然，对于可变的序列，我们还可以通过切片操作符':'完成浅拷贝，比如下面这个列表的例子：

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1[:]
>>> l2
[1, 2, 3]
>>> l1 == l2
True
>>> l1 is l2
False
```

还可以使用copy.copy

```python
>>> import copy
>>> l1 = [1, 2, 3]
>>> l2 = copy.copy(l1)
>>> l2
[1, 2, 3]
>>> l1==l2
True
>>> l1 is l2
False
```

特殊情况：对于元组，使用 tuple() 或者切片操作符':'不会创建一份浅拷贝，相反，它会返回一个指向相同元组的引用：

```java
>>> t1 = (1, 2, 3)
>>> t2 = tuple(t1)
>>> t1 == t2
True
>>> t1 is t2
True
```

**浅拷贝，是指重新分配一块内存，创建一个新的对象，里面的元素是原对象中子对象的引用**。因此，如果原对象中的元素不可变，那倒无所谓；但如果元素可变，浅拷贝通常会带来一些副作用，尤其需要注意。我们来看下面的例子：

```java
>>> l1 = [[1, 2], (30, 40)]
>>> l2 = list(l1)
>>> l1.append(100)
>>> l1[0].append(3)
>>> l1
[[1, 2, 3], (30, 40), 100]
>>> l2
[[1, 2, 3], (30, 40)]
>>> l1[1] += (50, 60)
>>> l1
[[1, 2, 3], (30, 40, 50, 60), 100]
>>> l2
[[1, 2, 3], (30, 40)]
```

我们首先初始化了一个列表 l1，里面的元素是一个列表和一个元组；然后对 l1 执行浅拷贝，赋予 l2。因为浅拷贝里的元素是对原对象元素的引用，因此 l2 中的元素和 l1 指向同一个列表和元组对象。l1.append(100)，表示对 l1 的列表新增元素 100。这个操作不会对 l2 产生任何影响，因为 l2 和 l1 作为整体是两个不同的对象，并不共享内存地址。操作过后 l2 不变，l1 会发生改变。再来看，l1[0].append(3)，这里表示对 l1 中的第一个列表新增元素 3。因为 l2 是 l1 的浅拷贝，l2 中的第一个元素和 l1 中的第一个元素，共同指向同一个列表，因此 l2 中的第一个列表也会相对应的新增元素 3。操作后 l1 和 l2 都会改变：最后是l1[1] += (50, 60)，因为元组是不可变的，这里表示对 l1 中的第二个元组拼接，然后重新创建了一个新元组作为 l1 中的第二个元素，而 l2 中没有引用新元组，因此 l2 并不受影响。操作后 l2 不变，l1 发生改变。

**深度拷贝，是指重新分配一块内存，创建一个新的对象，并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。因此，新对象和原对象没有任何关联。**Python 中以 copy.deepcopy() 来实现对象的深度拷贝。

```python
>>> import copy
>>> l1 = [[1, 2], (30, 40)]
>>> l2 = copy.deepcopy(l1)
>>> l1 is l2
False
>>> l1.append(100)
>>> l1[0].append(3)
>>> 1
1
>>> l1
[[1, 2, 3], (30, 40), 100]
>>> l2
[[1, 2], (30, 40)]
>>> l2
[[1, 2], (30, 40)]
```

深度拷贝也不是完美的，往往也会带来一系列问题。如果被拷贝对象中存在指向自身的引用，那么程序很容易陷入无限循环：

```python
>>> import copy
>>> x = [1]
>>> x.append(x)
>>> x
[1, [...]]
>>> y = copy.deepcopy(x)
>>> y
[1, [...]]
>>> x==y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RecursionError: maximum recursion depth exceeded in comparison
```

上面这个例子，列表 x 中有指向自身的引用，因此 x 是一个无限嵌套的列表。但是我们发现深度拷贝 x 到 y 后，程序并没有出现 stack overflow 的现象。这是为什么呢？其实，这是因为深度拷贝函数 deepcopy 中会维护一个字典，记录已经拷贝的对象与其 ID。拷贝过程中，如果字典里已经存储了将要拷贝的对象，则会从字典直接返回，我们来看相对应的源码就能明白：

```python

def deepcopy(x, memo=None, _nil=[]):
    """Deep copy operation on arbitrary Python objects.
      
  See the module's __doc__ string for more info.
  """
    if memo is None:
        memo = {}
    d = id(x) # 查询被拷贝对象x的id
  y = memo.get(d, _nil) # 查询字典里是否已经存储了该对象
  if y is not _nil:
      return y # 如果字典里已经存储了将要拷贝的对象，则直接返回
        ...    
```

## 16. 值传递，引用传递or其他，Python里参数是如何传递的？

TODO

## 17. **强大的装饰器**

函数的核心概念：

- 把函数赋予变量；
- 把函数当作参数，传入另一个函数中；
- 可以在函数里定义函数，也就是函数的嵌套；

- 函数的返回值也可以是函数对象，闭包



## 20. **揭秘** **Python** **协程**

C10K 瓶颈，也就是 同时连接到服务器的客户达到了一万个。

使用生成器，是 Python 2 开头的时代实现协程的老方法了，Python 3.7 提供了新的基于 asyncio 和 async / await 的方法。

简单的爬虫代码：

```python
import time


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)


if __name__ == '__main__':
    main(['url_1', 'url_2', 'url_3', 'url_4'])
```

<img src="https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201025142308.png" alt="image-20201025142308521" style="zoom:50%;" />

使用协程：

```python
import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)


if __name__ == '__main__':
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
```

![image-20201025144558682](https://raw.githubusercontent.com/haojunsheng/ImageHost/master/img/20201025144558.png)

发现效率并没有提高，



