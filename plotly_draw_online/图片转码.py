# 用于将图片存入markdown文件内
# 使用python将图片转化为base64字符串
import base64
f=open('生成KEY.PNG','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print('{0}'.format(str(ls_f)[1:]))

# base64字符串转化为图片
# import base64
# bs='iVBORw0KGgoAAAANSUhEUg....' # 太长了省略
# imgdata=base64.b64decode(bs)
# file=open('2.jpg','wb')
# file.write(imgdata)
# file.close()