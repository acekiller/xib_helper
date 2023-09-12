import xibHelper
import argparse

def fontSet(root):
    for child in root.iter():
        fontDescription = child.find('fontDescription')
        if fontDescription is None:
            continue
        
        fontWeight = '1'
        pointSize = fontDescription.get('pointSize')
        if pointSize is None:
            continue
        weight = fontDescription.get('weight')
        if weight is None:
            # 没有Weight情况，看下Type
            type = fontDescription.get('type')
            if type is None:
                continue
            else:
                if 'semibold' in type:
                    fontWeight = '3'
                elif 'bold' in type:
                    fontWeight = '4'
                elif 'medium' in type:
                    fontWeight = '2'
                elif 'regular' in type:
                    fontWeight = '1'
                elif 'light' in type:
                    fontWeight = '0'
                elif 'heavy' in type:
                    fontWeight = '5'
                elif 'black' in type:
                    fontWeight = '6'
        else:
            if weight == 'light':
                fontWeight = '0'
            elif weight == 'regular':
                fontWeight = '1'
            elif weight == 'medium':
                fontWeight = '2'
            elif weight == 'semibold':
                fontWeight = '3'
            elif weight == 'bold':
                fontWeight = '4'
            elif weight == 'heavy':
                fontWeight = '5'
            elif weight == 'black':
                fontWeight = '6'
        
        user_defined_attributes = xibHelper.getElement(child, 'userDefinedRuntimeAttributes')
        
        
        fontSize_attribute = xibHelper.appendRuntimeAttribute(user_defined_attributes, 'number', 'fontSize')
        xibHelper.appendRuntimeAttributeChild(fontSize_attribute, 'real', pointSize)

        fontWeight_attribute = xibHelper.appendRuntimeAttribute(user_defined_attributes, 'number', 'fontWeight')
        xibHelper.appendRuntimeAttributeChild(fontWeight_attribute, 'integer', fontWeight)


#xibHelper.read_file('/Users/macmini/pandanew/Panda/Panda/Pages/Trade/Trade/View/YLTradeTooBar.xib',fontSet)
def main():
    """
    脚本执行代码
    """
    parser = argparse.ArgumentParser(description="SwiftFitSize")
    parser.add_argument("-p", "--path", help="文件路径", required=False)
    args = parser.parse_args()
    if args.path is None:
        xibHelper.readPandaXIB(fontSet,[])
        return
    
    xibHelper.read_file(args.path, fontSet)

if __name__ == "__main__":
    main()
