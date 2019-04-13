# create_data_kitti.sh

cur_dir=$(cd $( dirname ${BASH_SOURCE[0]} ) && pwd )
echo $cur_dir
root_dir=$cur_dir
echo $root_dir
cd $root_dir

redo=1
data_root_dir="/media/yl/Elements/data/VOC_Pascal/VOCdevkit" ## 自行修改

data_path="/"
dataset_name="VOC_Pascal" ## 自行修改
mapfile="$root_dir/VOC_Pascal/labelmap.prototxt" ## 自行修改
anno_type="detection"
db="lmdb"
min_dim=0
max_dim=0
width=0
height=0

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in test trainval
do
  python $root_dir/scripts/create_annoset.py --anno-type=$anno_type --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $data_path $root_dir/$subset.txt $data_root_dir/$db/$dataset_name"_"$subset"_"$db $dataset_name
done
