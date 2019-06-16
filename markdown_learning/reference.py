import user_module.fig_converter as fc
import user_module.MarkDownGenerate as md

png1=fc.png_to_bytes('生成KEY.PNG')
png2=fc.png_to_bytes('生成KEY2.PNG')
if (png1 or png2) ==None:
    print('图片转换错误')
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
* 调用user_module模块内的fig_converter中的png_to_bytes方法
* 由于生成的是b'....'我们需要将b和单引号去掉在放入markdown字符串内
* 所以需要用到```eval(str(png)[1:])```让后用formate格式去加入到markdown_text里去
* 具体参见reference.py的代码
## 附录
dash的markdown使用方法[详见](https://dash.plot.ly/dash-core-components/markdown)


''' .format(eval(str(png1)[1:]),eval(str(png2)[1:]))


md.run_markdown(markdown_text)