# 机器狗ros运动控制

## 介绍
目前使用的运动控制代码来自云深处官方github（ros）和第三方可视化库（ros2）

云深处官方github：   [GitHub - DeepRoboticsLab/Lite3_ROS](https://github.com/DeepRoboticsLab/Lite3_ROS)                     （提供ros1和ros2代码，使用了ros1）

legubiao的可视化库：[GitHub - legubiao/lite3_ros2: ROS2 UDP bridge for Deep Robotics Lite3](https://github.com/legubiao/lite3_ros2) （该库主要功能是动态模型和雷达可视化，但由于使用较便利，故使用了它的ros2）


## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## ssh连接机器狗方式
shh连接可以登录机器狗主机，在机器狗上进行必要的操作，如：更改网络配置文件（感知主机的地址，狗向这个ip发送自身信息）、重启运动程序等。

首先连上机器狗热点  password见保修单

机器狗IP：192.168.2.1   用户名：ysc

 password见GitHub - DeepRoboticsLab/Lite3_MotionSDK 4.2

更改网络配置文件方式见GitHub - DeepRoboticsLab/Lite3_MotionSDK  5.配置数据上报地址和型号参数

重启运动程序方式见GitHub - DeepRoboticsLab/Lite3_MotionSDK   7.2 通讯问题排查

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
