# 用于将图片存入markdown文件内
# 使用python将图片转化为base64字符串
import base64
def png_to_bytes(png_path):
    rst=None
    with open(png_path,'rb') as f:#二进制方式打开图文件
        rst=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    return rst