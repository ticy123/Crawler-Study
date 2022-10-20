import re
s= """
<div class='周杰伦'><span id='1'>满城尽带黄金甲</span></div>
<div class='周星驰'><span id='2'>大话西游</span></div>
<div class='吴京'><span id='3'>战狼</span></div>
<div class='成龙'><span id='4'>宝贝计划</span></div>
"""
# 获取数据格式：(?P<分组名字>正则)
# obj=re.compile("<div class='.*?'><span id='.*?'>.*?</span></div>")
obj = re.compile("<div class='.*?'><span id='(?P<id>.*?)'>(?P<movie_name>.*?)</span></div>",
                 re.S)  # re.S （让. 可以匹配换行，避免中间断了）
ret = obj.finditer(s)
for it in ret:
# print(it.group("id"))
    print(it.group("id"))