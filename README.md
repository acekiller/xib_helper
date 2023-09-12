# xib_helper

1. xib_helper是针对iOS页面等比例缩放布局支持的xib自动化Python脚本。其中部分功能是基于Swift等比例缩放框架SwiftyFitsize所支持的xib特性的。
2. 该功能包含两个部分：
(1). 对字体的替换。主要用户采用系统字体布局下，后续对xib字体的动态替换。
(2). 对组件size大小的修改。用于修改组件的布局大小。

**使用方法**

1. 直接执行
```
swiftFitSize.py
```
将对所有xib文件进行修改操作

2. 针对特定的文件执行：
```
swiftFitSize.py -p file_path
```
将对指定的文件进行修改。




