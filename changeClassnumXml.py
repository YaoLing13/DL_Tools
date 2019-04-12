import os
from xml.etree.ElementTree import parse, Element
import xml.etree.cElementTree as ET
from PIL import Image

# 美化xml文件
def prettyXml(element, indent, newline, level = 0): # element为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if element.text == None or element.text.isspace(): # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    #else:  # 此处两行如果把注释去掉，Element的text也会另起一行
        #element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element) # 将elemnt转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1): # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level = level + 1) # 对子元素进行递归操作


xml_path = '/media/yl/Elements/data/VOC_Pascal/VOCdevkit/Annotations_20'
xml_path_new = '/media/yl/Elements/data/VOC_Pascal/VOCdevkit/Annotations'
img_path = '/media/yl/Elements/data/VOC_Pascal/VOCdevkit/JPEGImages_20'
img_path_new = '/media/yl/Elements/data/VOC_Pascal/VOCdevkit/JPEGImages'
files = os.listdir(xml_path)
for file in files:
    print(file)
    idx = file[:-4]
    img_name_old = img_path + '/'+ idx +'.jpg'
    img_name_new = img_path_new + '/'+ idx +'.jpg'
    xml_name_old = xml_path + '/'+ idx +'.xml'
    xml_name_new = xml_path_new + '/'+ idx +'.xml'

    xml=parse(xml_name_old)
    root = xml.getroot()
    # create xml
    annotation = ET.Element("annotation")
    #创建annotation的子节点folder，并添加数据
    annotation.append(xml.getiterator('folder')[0])
    annotation.append(xml.getiterator('filename')[0])
    annotation.append(xml.getiterator('source')[0])
    if len(xml.getiterator('owner')) > 0:
        annotation.append(xml.getiterator('owner')[0])
    annotation.append(xml.getiterator('size')[0])
    annotation.append(xml.getiterator('segmented')[0])
    
    voc_class=['person', 'car', 'bus', 'truck']
    car_class = ['bus', 'truck']
    
    
    items =[]
    for item in xml.getiterator('object'):
        if item.findtext('name') in voc_class:
            if item.findtext('name') in car_class:
                # print('be:', item.findtext('name'))
                name = item.find("name")
                name.text = "car"
                # print('af:', item.findtext('name'))
            # print('for:',item.findtext('name'))
            annotation.append(item)
            items.append(item.text)
    
    if len(items) > 0:
        prettyXml(annotation, '\t', '\n')  # 执行美化方法
        tree = ET.ElementTree(annotation)
        tree.write(xml_name_new)
        img = Image.open(img_name_old)
        img.save(img_name_new)
