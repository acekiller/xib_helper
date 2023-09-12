import os
import xml.dom.minidom
import time
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

'''读取Panda项目的XIB'''
def readPandaXIB(callback, ignoreFiles):
    current_path = os.getcwd()
    print("当前路径：", current_path)
    parent_path = os.path.dirname(current_path)
    print("上一级文件夹路径：", parent_path)
    read_all_xib(parent_path+"/Panda", callback, ignoreFiles)

'''读取全部XIB'''
def read_all_xib(path, callback, ignoreFiles):
    read_all_files(path, ".xib", callback, ignoreFiles)

'''读取全部XML'''
def read_all_files(path, endswith, callback, ignoreFiles):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file in ignoreFiles:
                continue
            if file.endswith(endswith):
                read_file(os.path.join(root, file), callback)


'''读取单个XML'''
def read_file(file_path, callback):
    tree = ET.parse(file_path)
    root = tree.getroot()

    callback(root)

#    prettyXml(root, '\t', '\n')
    tree.write(file_path)
    print("File saved and overwritten successfully! path = ", file_path)




'''xml文档格式整理'''
def prettyXml(element, indent, newline, level = 0):
    # 判断element是否有子元素
    if element:
        # 如果element的text没有内容
        if element.text == None or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element) # 将elemnt转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level = level + 1)


'''获取Child，如果没有则添加'''
def getElement(child, element):
    elementChild = child.find(element)
    if elementChild is None:
        elementChild = ET.Element(element)
        child.append(elementChild)
    return elementChild
    
'''XIB写入userDefinedRuntimeAttributes属性'''
def appendRuntimeAttributes(child, type, keyPath, tagName, tagValue):
    user_defined_attributes = getElement(child, 'userDefinedRuntimeAttributes')
    user_defined_attribute = appendRuntimeAttribute(user_defined_attributes, type, keyPath)
    appendRuntimeAttributeChild(user_defined_attribute, tagName, tagValue)

    
def appendRuntimeAttribute(child, type, keyPath):

    userDefinedRuntimeAttribute = None
    user_defined_attribute = child.findall('userDefinedRuntimeAttribute')
    if user_defined_attribute is not None:
        for attribute in user_defined_attribute:
            targetKeyPath = attribute.get('keyPath')
            if targetKeyPath == keyPath:
                userDefinedRuntimeAttribute = attribute
    
    # userDefinedRuntimeAttribute为空，添加
    if userDefinedRuntimeAttribute is None:
        userDefinedRuntimeAttribute = ET.Element('userDefinedRuntimeAttribute')
        child.append(userDefinedRuntimeAttribute)

    userDefinedRuntimeAttribute.set("type", type)
    userDefinedRuntimeAttribute.set("keyPath", keyPath)
    if type == "boolean":
        userDefinedRuntimeAttribute.set("value", "YES")
        
    return userDefinedRuntimeAttribute
    
    
def appendRuntimeAttributeChild(user_defined_attribute, tagName, tagValue):
    if tagName is None:
        return

    childTag = getElement(user_defined_attribute, tagName)
    childTag.set("key", "value")
    childTag.set("value", tagValue)
    


