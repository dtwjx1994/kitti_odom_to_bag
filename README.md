# KITTI Odometry to ROSbag

​     这个python工具用来将下载的Kitti数据集中的Velodyne Points 转为rosbag，并且可以将其中的位姿信息通过tf的形式发布出来。

## run

 

~~~

python wjx_kitti.py -s '00'
~~~

-s 参数代表你要用其中的哪个包  从00-11之间是有groundtruth的.

# kitti_odom_to_bag
