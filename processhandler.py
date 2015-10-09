from multiprocessing import Process, Queue

class ProcessHandler(object):
	def __init__(self, functions):
		self.processes = []
		self.num_of_processes = len(functions)
		self.functions = functions
		self.event_q = Queue()

	def start(self):
		# create/start processes and event queue
		for i in range(self.num_of_processes):
			function = self.functions[i]
			name = self.functions[i].__name__
			print function
			self.processes.append(Process(target=function, name=name, args=(self.event_q,)))
			
			self.processes[i].start()
			while not self.processes[i].is_alive():
				time.sleep(0.01)
			print self.processes[i]

	def close(self):
		for i in range(self.num_of_processes):
			self.event_q.close()
			self.event_q.join_thread()
			self.processes[i].join()
			print self.processes[i]

	def watchDog(self):
		for i in range(self.num_of_processes):
			if not self.processes[i].is_alive():
				print self.processes[i]
				function = self.functions[i]
				name = self.functions[i].__name__
				q = self.event_q
				self.processes[i] = Process(target=function, name=name, args=(q,))
				self.processes[i].start()
				while not self.processes[i].is_alive():
					time.sleep(0.1)
				print self.processes[i]