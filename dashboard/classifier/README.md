## Classifier

`def classifier(data) -> None`

parameter:

+ data: 一个数据集，提前填充了100条数据，最后加入3组数据来自3个mac地址的；分别是无害、恶意和无害，因此预期结果为0、1、0

没有return，而是直接print	（mac地址，ip地址，分类结果）

其中mac地址，ip地址为手动输出

功能: 对某一个 mac 地址对应的一系列数据包进行分类



main.py中有调用classify的示范

```
from classify import classifier

classifier(data) # data为数据集
```

