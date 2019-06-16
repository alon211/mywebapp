import user_module.fig_converter as u_fg
import user_module.MarkDownGenerate as u_mg
Option_fig=u_fg.png_to_bytes('dropdown_option_style.PNG')
Multi_fig=u_fg.png_to_bytes('dropdown_multi_style.PNG')
print(Option_fig)
markdown_text='''
# DropDown
---
官网[example](https://dash.plot.ly/dash-core-components)

---

## 参数
---
### options
下拉列表 格式:```{1}```
![option效果图](data:PNG;base64,{0})

### multi
多选 ```multi=True```

![option效果图](data:PNG;base64,{2})


'''.format(eval(str(Option_fig)[1:]),
           eval(str([{"label":"optionA","value":0},{"label":"optionB","value":1},{"label":"optionC","value":2}])),
           eval(str(Multi_fig)[1:]))
u_mg.run_markdown(markdown_text)