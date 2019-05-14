import socket

HOST = '127.0.0.1' #Host call my computer - localhost
PORT = 8100

class receiver():
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.bind((HOST, PORT))
		print("file recv start from", HOST)

	def receive_file(self):
		data_transrate = 0		
		filename = self.socket.recvfrom(1024)
		filename = str(filename[0].decode())
		
		filesize = self.socket.recvfrom(1024)
		filesize = int(filesize[0].decode())

		print('file Name: ', filename)
		print('file Size: ', filesize)


		data = self.socket.recvfrom(1024)
		#If have none. then exception
		if not data:
			print("Error, Can't search file")
			reutrn
	
		with open(filename, 'wb') as f:
			try:
				while data:
					data = data[0]
					f.write(data)
					data_transrate += len(data)
					rate = (data_transrate / filesize) * 100
					data_rate = str(data_transrate) + "/" + str(filesize) + ", " + str(rate)+"%"
					print("current size / total size = ", data_rate)
					if rate >= 100:
						break
					data = self.socket.recvfrom(1024)
			except Exception as e:
				print(e)
	def main(self):
		self.receive_file()
		self.socket.close()

start = receiver()
start.main()
