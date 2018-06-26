# KITTI Odometry to ROSbag

This python tool is aimed to solve the problem that convert kitti odometry to rosbag.Although there is some tool to convert kitti raw data to rosbag. And this tool is developing.we can convert point cloud and pose information to rosbag and pose is convert to tf message.

​     这个python工具用来将下载的Kitti数据集中的Velodyne Points 转为rosbag，并且可以将其中的位姿信息通过tf的形式发布出来。

## run

 

~~~

python wjx_kitti.py -s '00'
~~~
'00' present the point cloud sequences you want to convert.And it exits ground truth information if the sequences between '00' to '11'。

-s 参数代表你要用其中的哪个包  从00-11之间是有groundtruth的.

If you want to change the topic, you may modifiy the code in wjx_kitti.py .


# kitti_odom_to_bag
