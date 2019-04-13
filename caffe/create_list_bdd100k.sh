# create_list_kitti.sh
#!/bin/bash

cp /media/yl/Elements/data/BDD100k/bdd100k/ImageSets/Main/trainval.txt trainval_img.txt
cp /media/yl/Elements/data/BDD100k/bdd100k/ImageSets/Main/trainval.txt trainval_label.txt
sed -i "s/^/\/media\/yl\/Elements\/data\/BDD100k\/bdd100k\/JPEGImages\//g" trainval_img.txt 
sed -i "s/$/.jpg/g" trainval_img.txt

sed -i "s/^/\/media\/yl\/Elements\/data\/BDD100k\/bdd100k\/Annotations\//g" trainval_label.txt 
sed -i "s/$/.xml/g" trainval_label.txt

paste -d' ' trainval_img.txt trainval_label.txt >> trainval.txt

rm -f trainval_img.txt
rm -f trainval_label.txt

cp /media/yl/Elements/data/BDD100k/bdd100k/ImageSets/Main/test.txt test_img.txt
cp /media/yl/Elements/data/BDD100k/bdd100k/ImageSets/Main/test.txt test_label.txt

sed -i "s/^/\/media\/yl\/Elements\/data\/BDD100k\/bdd100k\/JPEGImages\//g" test_img.txt 
sed -i "s/$/.jpg/g" test_img.txt 

sed -i "s/^/\/media\/yl\/Elements\/data\/BDD100k\/bdd100k\/Annotations\//g" test_label.txt 
sed -i "s/$/.xml/g" test_label.txt

paste -d' ' test_img.txt test_label.txt >> test.txt

rm -f test_label.txt
rm -f test_img.txt 

cp /media/yl/Elements/data/BDD100k/bdd100k/ImageSets/Main/test.txt test_img.txt
cp /media/yl/Elements/data/BDD100k/bdd100k/ImageSets/Main/test.txt test_label.txt
sed -i "s/^/JPEGImages\//g" test_img.txt 
sed -i "s/$/.jpg/g" test_img.txt 
sed -i "s/^/BDD100k\/bdd100k\/Annotations\//g" test_label.txt 
sed -i "s/$/.xml/g" test_label.txt
paste -d' ' test_img.txt test_label.txt >> test_imglabel.txt
build/tools/get_image_size /media/yl/Elements/data/BDD100k/bdd100k test_imglabel.txt test_name_size.txt
rm -f test_label.txt
rm -f test_img.txt 
