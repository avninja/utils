import socket, time, sys

class UDPServer(socket):
	def __init__(self, port):
		super(UDPServer, self).__init__()
		self.port = port
		# Create socket and bind to address
		self.UDPSock = socket(AF_INET, SOCK_DGRAM)
		self.UDPSock.bind(('', port))

	def server_start(self, event_q):
		try:
			print 'starting server on port', self.port
			while True:
				data, addr = self.UDPSock.recvfrom(1024)
				print data
				event_q.put(data)
		except(KeyboardInterrupt):
			self.UDPSock.close()
			print 'Server stopped.'
			sys.exit(0)

class UDPClient(object):
	def __init__(self, port):
		self.addr = ('<broadcast>', port)  
		self.UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.UDPSock.bind(('', 0))
		self.UDPSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	def sendMessage(self, message):
		try:
			if len(message):
				message = str(message)
				print "Sending Message:", message
				self.UDPSock.sendto(message, self.addr)
		except:
			self.UDPSock.close()
			sys.exit(0)