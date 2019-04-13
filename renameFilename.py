import os

# dir_path = "/media/yl/Elements/data/bit"
dir_path = "/media/yl/Elements/data/yuanshi"
dirs = os.listdir(dir_path)

### only image
'''
count = 0
for file in dirs:
    dir = dir_path + '/' + file
    if os.path.isdir(dir):
        for fs in os.listdir(dir):
            tail = ''.join(fs.split('.')[-1:])
            fname = "{:0>10d}".format(count) + '.' + tail
            os.renames(dir+'/'+fs, dir+'/'+fname)
            count += 1
            print(dir+'/'+fs)
'''


### image + xml
count = 511
for file in dirs:
    dir = dir_path + '/' + file
    if os.path.isdir(dir):
        for fs in os.listdir(dir):
            if "jpg" in fs:
                idx = fs[:-4]
                # tail = ''.join(fs.split('.')[-1:])
                img_name = "{:0>11d}".format(count) + '.jpg'
                xml_name = "{:0>11d}".format(count) + '.xml'
                old_img = dir+'/'+ idx + '.jpg'
                old_xml = dir+'/'+ idx + '.xml'
                new_img = dir + '/' + img_name
                new_xml = dir + '/' + xml_name
                os.renames(old_img, new_img) # rename jpg
                os.renames(old_xml, new_xml) # rename xml
                count += 1
                print(old_img)
                print(old_xml)
