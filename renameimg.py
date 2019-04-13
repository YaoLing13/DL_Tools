import os

dir_path = "/media/yl/Elements/data/bit"
dirs = os.listdir(dir_path)

count = 0
for file in dirs:
    dir = dir_path + '/' + file
    if os.path.isdir(dir):
        for fs in os.listdir(dir):
            tail = ''.join(fs.split('.')[-1:])
            fname = "{:0>11d}".format(count) + '.' + tail
            os.renames(dir+'/'+fs, dir+'/'+fname)
            count += 1
            print(dir+'/'+fs)
