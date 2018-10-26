# install:

```pip install -r requirements.txt -I```

# usage:

* 进出口税则查询
```python hello.py {page_index_from:0} {page_index_end:0} {csv_format:excel}```
page_index_from=0表示默认第一页，page_index_end=0表示默认最大页

从第一页开始，生成excel格式的csv文件：```python hello.py```

从第三页开始，生成excel格式的csv文件：```python hello.py 3```

从第一页开始，最多爬三页，生成excel格式的csv文件：```python hello.py 0 3```

从第一页开始，最多爬三页，生成excel格式的csv文件：```python hello.py 1 3```

从第一页开始，最多爬三页，生成原始内容的csv文件：```python hello.py 1 3 source```

从第一页开始，爬所有页的数据，生成原始内容的csv文件：```python hello.py 0 0 source```

excel格式是指遇到字符串以“-”开头时，自动在字符串前面加上“="”，在字符串后面加上“"”，默认使用excel格式
比如<pre>
税则号列	货品名称	最惠国税率	普通税率	出口税率	暂定税率
97060000	超过100年的古物	0	0	 	  	 	 	 
97040090	---其他	6	50	 	 
</pre>
生成
<pre>
税则号列,货品名称,最惠国税率,普通税率,出口税率,暂定税率
97060000,超过100年的古物,0,0,,
97040090,="---其他",6,50,,
</pre>