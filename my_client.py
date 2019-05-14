import socket
import os
from os.path import exists

HOST = '127.0.0.1' #localhost
PORT = 8100

class sendFile():
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.connect((HOST, PORT))
		print("Start")

	def send_file(self):
		filename = input('Input your file name: ')
		self.socket.sendto(filename.encode(), (HOST, PORT))
		#if don't have file then return
		if not exists(filename):
			return
	
		filesize = os.path.getsize(filename)
		print("send:", filename, filesize)
		self.socket.sendto(str(filesize).encode(), (HOST, PORT))
		data_transrate = 0	
		print("File Transmit start.....")
		with open(filename, 'rb') as f:
			try:
				data = f.read(1024) #buffer 1024byte
				while data:
					data_transrate += self.socket.sendto(data, (HOST, PORT))
					rate = (data_transrate / filesize) * 100
					data_rate = str(data_transrate) + "/" + str(filesize) + "," + str(rate) + "%"
					data = f.read(1024) 
					print("current size / total_size = ", data_rate)
			except Exception as e:
				print(e)
		print("ok")
		print("file_send_end")

	def main(self):
		self.send_file()
		self.socket.close()

client = sendFile()
client.main()
