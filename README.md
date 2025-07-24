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
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## 作者及致谢
Show your appreciation to those who have contributed to the project.

## 项目状态
完
