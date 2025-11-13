##功能:
1.添加收入、支出记录
2.查看所有记录
3.按日期或者类别筛选
4.统计总收入，总支出，余额
5.数据保存到本地 json

##项目构建
文件：

1.程序入口   main.py

2.核心功能逻辑  finance.py

3.数据读写 json    storage.py

4.工具函数（？日期格式化等）  utils.py

5data/records.json 存储记录

#### 第一步 

实现添加记录并保存到 JSON 文件

ps：创建项目文件，并判断，如果有直接写入utf-8格式的

假如没有这个文件 就创建这个文件

使用的库函数 json os

1.使用模块和固定路径（相对路径）

2.加载文件，如果文件不存在返回空，假如存在，只读方式打卡并把文件转化成python 的列表

3.保存记录

![1762932512694](C:\Users\1\AppData\Roaming\Typora\typora-user-images\1762932512694.png)





#### 第二步

写关键功能

ps：首先完成功能 写操作

定义函数

add_recode(category,description,amoutn,date=None)

​                    category	类别，如 "food"、"salary"
​                description	描述，如 "午餐"、"工资"
​                  amount	金额，字符串或数字；正数代表收入，负数代表支出
​                       date	可选，不传就默认今天

   date = date or get_current_date()

**读取 追加 写回**

读取整个列表  records=load_records()

追加新的字典 records.append(

{

"data" : data,

"category" : category,

"description" : description ,

"amount" :  float(amount)  , 支持小数点

}

)

写入 save_records(records)

print("记录添加成功")

#### 第三步

数据处理函数

暂时只处理日期时间

def get_current_date():

```python
  return datetime.today().strftime("%Y-%m-%d")
```

#### 第四步

编写main函数

def main():

​	print("个人记账本 ")
​	category = input("类别: ")
​	description = input("描述: ")
​	amount = input("金额（收入为正，支出为负）: ")
​	add_record(category, description, amount)
if __name__ == "__main__":
​	main()



### 升级

#### 第一步

升级finance核心功能函数

增加：

产看所有记录

统计总收入、总支出、余额

命令行菜单循环

list_records()

读取数据 records=load_records()

if not records:

pint("暂无数据")

return

print













