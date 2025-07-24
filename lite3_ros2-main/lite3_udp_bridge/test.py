#该脚本用于向机器狗发送指令码命令，可根据需要更改发送的指令码
#脚本将指令码以UDP形式发送给机器狗
#该脚本是由ai写的史山代码，本着能跑就行的原则没有进行过多修改

import socket
import struct
import time
from typing import Tuple

class UdpCommandSender:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_command(self, code: int, param_size: int, cmd_type: int):
        """
        发送UDP命令（小端格式）
        :param code: 指令码 (uint32)
        :param param_size: 参数大小 (int，负数自动转为2的补码形式)
        :param cmd_type: 指令类型 (uint32)
        """
        # 将参数转换为无符号32位整数（处理负值）
        # 负数会自动转换为2的补码形式
        u32_param_size = param_size & 0xFFFFFFFF
        
        # 打包为小端字节序 (<表示小端，3个I表示3个无符号int)
        data = struct.pack("<III", code, u32_param_size, cmd_type)
        
        # 发送UDP数据包
        self.sock.sendto(data, (self.ip, self.port))
        print(f"Sent: [0x{code:08X} {param_size} {cmd_type}]")
    
    def heartbeat(self):
        """发送心跳指令"""
        self.send_command(0x21040001, 0, 0)
    
    def move_forward(self, speed: int):
        """
        发送前进指令
        :param speed: 速度值（范围：-6553到6553）
        """
        # 确保速度在规定范围内
        speed = max(-6553, min(speed, 6553))
        self.send_command(0x21010130, speed, 0)
    
    def move_lateral(self, speed: int):
        """
        发送左右平移指令
        :param speed: 速度值（范围：-12553到12553）
        """
        speed = max(-12553, min(speed, 12553))
        self.send_command(0x21010131, speed, 0)
    
    def turn(self, speed: int):
        """
        发送转弯指令
        :param speed: 角速度（范围：-9553到9553）
        """
        speed = max(-9553, min(speed, 9553))
        self.send_command(0x21010135, speed, 0)
    
    def stop_all(self):
        """停止所有运动"""
        self.move_forward(0)
        self.move_lateral(0)
        self.turn(0)

    def up_down(self):    #自主模式指令码，请别在意为什么是up_down,把指令码改成其他的就会执行其他动作
        self.send_command(0x21010C03,0, 0)

    
def main():
    # 目标机器狗的IP和端口
    ROBOT_IP = "192.168.2.1"
    ROBOT_PORT = 43893
    
    # 创建发送器
    sender = UdpCommandSender(ROBOT_IP, ROBOT_PORT)
    
    try:
        # 心跳示例（2Hz）
        print("Starting heartbeat...")
        while True:
            sender.heartbeat()
            sender.up_down()
            time.sleep(0.5)  # 2Hz
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        # 停止所有运动
        sender.stop_all()

if __name__ == "__main__":
    main()