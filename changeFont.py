import xibHelper
import argparse


def fontSet(root):
    for child in root.iter():
        fontDescription = child.find('fontDescription')
        if fontDescription is None:
            continue
        
        name = fontDescription.get('name')
        pointSize = fontDescription.get('pointSize')
        if name is None:
            continue
        weight = 'regular'
        if 'PingFangSC' in name:
            if 'Regular' in name:
                weight = 'regular'
            elif 'Medium' in name:
                weight = 'medium'
            elif 'Semibold' in name:
                weight = 'semibold'
            elif 'Thin' in name:
                weight = 'light'
            elif 'Light' in name:
                weight = 'light'
            #type="system" weight="semibold" pointSize="13"
            fontDescription.attrib.pop('name')
            fontDescription.attrib.pop('family')
            fontDescription.attrib.pop('pointSize')
            fontDescription.set('type', "system")
            fontDescription.set('weight', weight)
            fontDescription.set('pointSize', pointSize)
#            elem.attrib['fontDescription'] = elem.attrib['fontDescription'].replace('PingFang', 'System')
    




def main():
    """
    脚本执行代码
    """
    parser = argparse.ArgumentParser(description="SwiftFitSize")
    parser.add_argument("-p", "--path", help="文件路径", required=False)
    args = parser.parse_args()
    if args.path is None:
        xibHelper.readPandaXIB(fontSet)
        return
    
    xibHelper.read_file(args.path, fontSet)

if __name__ == "__main__":
    main()

