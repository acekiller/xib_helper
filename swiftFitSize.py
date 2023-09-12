
import xibHelper
import argparse

ignore_xibs = ["YLHomeToolBar.xib"]

# 设置FitSize
def onFitSize(root):
    
    for child in root.iter():
    
        placeholder = child.get('placeholder')
        if placeholder is not None and placeholder == 'YES':
            user_defined_attribute = child.find('userDefinedRuntimeAttributes')
            if user_defined_attribute is not None:
                child.remove(user_defined_attribute)
                print("移除placeHodler下的Runtime属性")
            continue
        
        if child.tag == "stackView":
            appendSpacingFitTypeAttribute(child)
#        if child.tag == "button" or child.tag == "label" or child.tag == "textField" or child.tag == "textView":
#            appendFontFitTypeAttribute(child)
        if child.tag == "constraint":
            appendConstraintAttribute(child)


# 写入fontFitType属性
def appendFontFitTypeAttribute(child):
    xibHelper.appendRuntimeAttributes(child, "number", "fontFitType", "integer", "1")
    
def appendConstraintAttribute(child):
    xibHelper.appendRuntimeAttributes(child, "number", "swiftyFitType", "integer", "1")
    
def appendSpacingFitTypeAttribute(child):
    xibHelper.appendRuntimeAttributes(child, "boolean", "spacingFitType", None, None)

def main():
    """
    脚本执行代码
    """
    parser = argparse.ArgumentParser(description="字体替换")
    parser.add_argument("-p", "--path", help="文件路径", required=False)
    args = parser.parse_args()
    if args.path is None:
        xibHelper.readPandaXIB(onFitSize, ignore_xibs)
        return
    
    xibHelper.read_file(args.path, onFitSize)

if __name__ == "__main__":
    main()
