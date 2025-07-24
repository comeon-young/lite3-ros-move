# 机器狗ros运动控制

## 介绍
目前使用的运动控制代码来自云深处官方github（ros）和第三方可视化库（ros2）

云深处官方github：   [GitHub - DeepRoboticsLab/Lite3_ROS](https://github.com/DeepRoboticsLab/Lite3_ROS)                     （提供ros1和ros2代码，使用了ros1）

legubiao的可视化库：[GitHub - legubiao/lite3_ros2: ROS2 UDP bridge for Deep Robotics Lite3](https://github.com/legubiao/lite3_ros2) （该库主要功能是动态模型和雷达可视化，但由于使用较便利，故使用了它的ros2）


## 1.配置Ubuntu环境 下载ros
我的ros1和ros2分别安装在不同的虚拟机里Ubuntu20.04和Ubuntu22.04，下载ros和运动程序时请注意虚拟机差异

下载Ubuntu和VWware Tools参考  [VMware 安装配置 Ubuntu（最新版、超详细）_vmware-workstation-full-17.5.1-23298084.exe-CSDN博客](https://blog.csdn.net/m0_70885101/article/details/137694608)

ros2下载参考   [ROS2安装方法 - 图书资源](https://book.guyuehome.com/ROS2/1.%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84/1.3_ROS2%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95/)

ros1参考  [【ROS】在 Ubuntu 20.04 安装 ROS 的详细教程_ubuntu20.04安装ros-CSDN博客](https://blog.csdn.net/PlutooRx/article/details/127558240)

## 2.ssh连接机器狗方式
shh连接可以登录机器狗主机，在机器狗上进行必要的操作，如：更改网络配置文件（感知主机的地址，狗向这个ip发送自身信息）、重启运动程序等。

首先连上机器狗热点  password：12345678  详细信息见保修单

机器狗IP：192.168.2.1   用户名：ysc

 password见[GitHub - DeepRoboticsLab/Lite3_MotionSDK](https://github.com/DeepRoboticsLab/Lite3_MotionSDK) 4.2部分

更改网络配置文件方式见[GitHub - DeepRoboticsLab/Lite3_MotionSDK](https://github.com/DeepRoboticsLab/Lite3_MotionSDK)  5.配置数据上报地址和型号参数

重启运动程序方式见[GitHub - DeepRoboticsLab/Lite3_MotionSDK](https://github.com/DeepRoboticsLab/Lite3_MotionSDK)   7.2 通讯问题排查

## 使用方法
[GitHub - DeepRoboticsLab/Lite3_ROS](https://github.com/DeepRoboticsLab/Lite3_ROS)官方的这个运动通信库是为高级版的狗准备的，那些狗主机内自带ros程序，但是我们开发的体验版是没有的，所以代码需要下载到开发主机上

## 3.配置ros1运动控制程序（ubuntu20.04）      使用ros2请直接看第5部分
**（1）. 创建工作空间**

mkdir -p ~/message_transformer_ws/src

cd ~/message_transformer_ws/src

**（2）初始化工作空间**

catkin_init_workspace

**（3）克隆代码库**

git clone https://public-gitlab.cloudglab.cn/gzy/move.git

**（4）编译工作空间**

cd ~/message_transformer_ws

catkin_make   #每次更改代码记得再编译一次，相当于ros2的colcon build

**（5）更改机器狗主机ip（两处，在gitlab上我已改好）**
分别前往launch文件和/message_transformer/src/ros2qnx.cpp，把其中默认的机器狗IP192.168.1.120改成实际的192.168.2.1

再编译一次工作空间

## 4.使用ros1控制机器狗
**（1）ssh连接机器狗**
连上后

查看网络配置文件，把ip改成自己开发主机的，使用虚拟机的注意把网络设置为桥接模式，nat模式虚拟机获得的IP是假的

 cd ~/jy_exe/conf

 vim network.toml

重启运动程序。其他人的控制中断或一些意外原因会致使jy_exe不工作，通常重启下就好了，但切记先让狗处于趴下状态，否则狗将重重摔在地上

 cd ~/jy_exe

 sudo ./stop.sh
 
 sudo ./restart.sh

**（2）启动通信节点**

cd message_transformer_ws/                                    #进入功能包工作空间
source devel/setup.bash                                       #添加工作空间环境变量
roslaunch message_transformer message_transformer.launch      #启动通信功能包节点

**（3）发布速度指令  第3到第5步不分前后顺序，可按需调整**


 使用/cmd_vel话题向运动主机下发速度指令，话题消息类型geometry_msgs/Twist定义如下：
geometry_msgs/Vector3 linear                # 线速度(m/s)
    float64 x                    # 前向速度，向前为正
    float64 y                    # 侧向速度，向左为正
    float64 z                    # 无效参数
geometry_msgs/Vector3 angular                # 角速度(rad/s)
    float64 x                    # 无效参数
    float64 y                    # 无效参数
    float64 z                    # 转向角速度，左转为正


在新终端输入

 rostopic pub /cmd_vel geometry_msgs/Twist

按空格+tab，自动补全消息格式，再在速度值前加上 -r 10 使其一秒发十次，如下：

rostopic pub /cmd_vel geometry_msgs/Twist -r 10 "linear: 
x: 0.2 
y: 0.1 
z: 0.0 
angular: 
x: 0.0 
y: 0.0 
z: 0.3 

**（4）机器狗需要在起立状态下被控制**
使用云深处app使狗起立

**（5）进入自主模式**
控制模式决定机器人响应的速度指令来源，自主模式下机器人响应由感知主机下发的速度指
令，手动模式下机器人响应由手柄下发的速度指令。
为了使用ros控制机器狗，我们需要让狗进入自主模式。但我们体验版的狗是不能像官方文档里一样从app切换为自主模式的，所以我使用python脚本持续发送指令码确保狗处于自主模式。

屏幕截图 2025-07-01 160748.png

**总之，要做的事是：运行test.py**

一切顺利的话，机器狗将开始按速度指令运动

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## 作者及致谢
Show your appreciation to those who have contributed to the project.

## 项目状态
完
