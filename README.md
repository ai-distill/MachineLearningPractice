# MachineLearningPractice
《机器学习实战》 学习记录



## 学习记录
<table><th><tr><td>序号</td><td>文件名</td><td>对应书的章节</td><td>主要讲解的内容</td></tr></th><tbody>
        <tr><td>1</td><td>example1.py</td><td>1.7</td><td>初步了解Numpy</td></tr>
        
</tbody>
</table>

## 纠错
### 2.1.2的代码示例
> python 3.5之后将iteritems变为items

按照书上代码书写会报错：
AttributeError: 'dict' object has no attribute 'iteritems'

解决方案：
```python
# 将下面这行代码修改成最后一行的代码
sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
```
