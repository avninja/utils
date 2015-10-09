#import udp
from processhandler import *
import socket, time
from multiprocessing import Process, Queue, freeze_support

def server_start(port, event_q):
	# Create socket and bind to address
	UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	UDPSock.bind(('', port))
	try:
		print 'starting server on port', port
		while True:
			data, addr = UDPSock.recvfrom(1024)
			event_q.put(data)
	except(KeyboardInterrupt):
		UDPSock.close()
		print 'Server stopped.'
		sys.exit(0)

if __name__ == "__main__":
	freeze_support()
	event_q = Queue()
	p = Process(target=server_start, name='udpserver', args=(33333, event_q,))
	p.start()

	#functions = [server.server_start]
	#p = ProcessHandler(functions)
	#p.start()

	try:
		while True:
			#p.watchDog()
			if not event_q.empty():
				print event_q.get()
			time.sleep(0.01)
	except(KeyboardInterrupt):
		p.join()
		sys.exit(0)