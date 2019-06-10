import dash
import dash_html_components as html
import dash_core_components as dcc

# 用于将图片存入markdown文件内
# 使用python将图片转化为base64字符串
import base64
生成KEY=None
生成KEY2=None
with open('生成KEY.PNG','rb') as f:#二进制方式打开图文件
    生成KEY=base64.b64encode(f.read()) #读取文件内容，转换为base64编码

with open('生成KEY2.PNG','rb') as f:#二进制方式打开图文件
    生成KEY2=base64.b64encode(f.read()) #读取文件内容，转换为base64编码

markdown_text='''
# plotly在线绘图

---
## 1.注册plotly在线服务
去[plotly个人中心](https://plot.ly/settings/api)
## 2.获取Key Gen
![点击生成KEYGEN](data:PNG;base64,{0})
![获取KEYGEN](data:PNG;base64,{1})
## 3.创建生成文件
运行init.py生成本地的.plotly/.credentials
## 4.credentials路径位置:
C://Users//admin//.plotly
# 附录
---
## 图片存储方式说明
由于可能需要在github上下载，如果直接引用的话需要每台电脑的图片的绝对路径，
这显然不是个好办法。但是由于相对路径是确定的，但MarkDown中貌似没有相对路径
这一说法，所以我们只能用另一种方法来存储图片，就是将图片转为base64格式的字符串
放入markdown的文件中。
### 使用python将图片转为base64
```Python
import os
def tef(*args):
return None
print(1)
```


''' .format(eval(str(生成KEY)[1:]),eval(str(生成KEY2)[1:]))


app=dash.Dash(__name__)
app.layout=html.Div(
dcc.Markdown(markdown_text)
)
if __name__=='__main__':
    app.run_server(debug=True)