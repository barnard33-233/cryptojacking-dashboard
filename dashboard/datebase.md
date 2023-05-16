# 数据库说明

库名 result

## 表
**待优化**

1. Record

   |mac|ip|safety|time|
   |---|---|---|
   |String|String|Int|timestring|

   + mac 是主键
   + IP 为当前设备的IP地址 *? 可不可以没有这个*
   + safety 字段暂时定为一个二值的字段，0为安全，1为有风险
   + Time 记录分类器写数据库的时候的时间(数据库更新)
2. Modified
|mtime|
|---|
|timestring|

用于标记最新一次更新的时间

*timestring 的格式都是 *

## 更新

### 分类器

分类器进程将分类完的结果写到数据库里面。

### server主进程

server 进程每次接收到请求的时候对数据库进行查询。

先查询 `Modified.mtime`，和内存中的记录`modles.mtime`对比，如果是更新的结果就对整个Record表进行读取


