from collections import *
from route import *
from random import *

class Individual:
	def __init__(self):
		#self.individual=OrderedDict()
		self.individual=[]
		self.length = Geodesic_distance([0, 0],[0, 0])
	def AddRoute(self,route):
		#self.individual.update(route.Get())
		self.individual.append(route)
		#self.length+=route.GetLength()
		#self.AddLength(route)
	def Get(self):
		return self.individual
	def Getn(self,n):
		return self.individual[n]
	def GetLength(self):
		return self.length
	def GetSize(self):
		return len(self.individual)
	def Show(self):
		for i in range(0,len(self.individual)):
			print(self.individual[i].Get(),end="")
		print()
	def AddLength(self, route):
		self.length += route.GetLength()
	def ResetLength(self):
		self.length = Geodesic_distance([0, 0],[0, 0])


	def CreateIndividual(self,data,n):
		#Routes =[]
		#self.individual=[]
		#self.length=0
		numbers=[]
		for i in range(0,len(data.Get())):
			numbers.append(i)

		def sum(routes_length):
			sum = 0
			for i in routes_length:
				sum += i 
			return sum

		routes_length = []

		if n == 1:
			routes_length.append(len(data.Get()))
		else:
			routes_length.append(randint(1,len(data.Get())//2))
			for i in range(0,n-2):
				route_length = randint(1,len(data.Get()) - sum(routes_length) - 1)
				routes_length.append(route_length)

			routes_length.append(len(data.Get())-sum(routes_length))

		
		for i in range(0,n):
			route = Route()
			for j in range(0,routes_length[i]):
				random=sample(numbers,k=1)
				route.AddPlace(data.GetName(random[0]),data.GetValue(random[0]))
				numbers.remove(random[0])
			self.AddRoute(route)
		'''for i in range(0,n):
			route = Route()
			#route.AddPlace("START",START.get("START"))
			if(len(numbers))>=(2*len(data.Get())//n):
				for j in range(0,len(data.Get())//n):
					if(len(numbers) != 0):
						random=sample(numbers,k=1)
						route.AddPlace(data.GetName(random[0]),data.GetValue(random[0]))
						numbers.remove(random[0])
				#route.AddPlace("START",START.get("START"))
			else:
				for j in range(0,ceil(len(data.Get())/n)):
					if(len(numbers) != 0):
						random=sample(numbers,k=1)
						route.AddPlace(data.GetName(random[0]),data.GetValue(random[0]))
						numbers.remove(random[0])
				#route.AddPlace("START",START.get("START"))
			#Routes.append(route.Get())
			route.Show()
			self.AddRoute(route)
		'''

		#print(route.Get())
		#return Routes

	def Merge(self):
		merged = OrderedDict()
		for i in self.individual:
			merged.update(i.Get())

		return merged

	def Check_if_correct(self):
		for i in self.individual:
			for j in self.individual:
				if i != j:
					for i_keys in i.Get():
						for j_keys in j.Get():
							if i_keys == j_keys:
								return False

		return True


	def Check_place(self,name):
		for i in self.individual:
			for j in i.Get():
				if j == name:
					return True
		return False