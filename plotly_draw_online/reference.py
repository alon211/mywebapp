import user_module.fig_converter as fc
import user_module.MarkDownGenerate as md

markdown_txt='''
# api_key生成在以下地址：
# https://plot.ly/settings/api#/
# 文件生成位置:
# C://Users//admin//.plotly

'''
import plotly
# api_key生成在以下地址：
# https://plot.ly/settings/api#/
# 文件生成位置:
# C:\Users\admin\.plotly
plotly.tools.set_credentials_file(username='alon211', api_key='xja8LkZz8jmzFT2kYKHe')