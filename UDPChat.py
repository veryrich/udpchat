import threading
import time
import socket


def recver(_socket, listen):
	"""
	接收消息
	:param _socket:
	:param listen: 监听端口
	:return:
	"""
	serverSocket.bind(("", listen))
	while True:
		get_msg, sender_ip = _socket.recvfrom(1024)

		print("\n\n发送人:%s\n消息内容:%s\n" % (sender_ip[0], get_msg.decode("utf-8")))

		time.sleep(0.1)


def sender(_socket, dest_addr, dest_port):
	"""
	发送消息
	:param _socket:
	:param dest_addr: 目标IP地址
	:param dest_port: 目标端口
	:return:
	"""
	while True:
		send_msg = input("输入消息内容")
		serverSocket.sendto(send_msg.encode(), (dest_addr, dest_port))


if __name__ == '__main__':
	listen_port = int(input("要监听本机哪个端口："))
	send_to_addr = input("对方的IP：")
	send_to_port = int(input("对方的端口："))

	# 创建socket
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

	# 创建收 线程
	t_recv = threading.Thread(target=recver, args=(serverSocket, listen_port))
	t_recv.start()

	# 创建 发线程
	t_send = threading.Thread(target=sender, args=(serverSocket, send_to_addr, send_to_port))
	t_send.start()
