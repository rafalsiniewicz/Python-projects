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
		self.length+=route.GetLength()
	def Get(self):
		return self.individual
	def GetLength(self):
		return self.length
	def GetSize(self):
		return len(self.individual)
	def Show(self):
		for i in range(0,len(self.individual)):
			print(self.individual[i].Get(),end="")
		print()

	def CreateIndividual(self,data,n):
		#Routes =[]
		#self.individual=[]
		#self.length=0
		numbers=[]
		for i in range(0,len(data.Get())):
			numbers.append(i)
		for i in range(0,n):
			route = Route()
			if(len(numbers))>=(2*len(data.Get())//n):
				for j in range(0,len(data.Get())//n):
					if(len(numbers) != 0):
						random=sample(numbers,k=1)
						route.AddPlace(data.GetName(random[0]),data.GetValue(random[0]))
						numbers.remove(random[0])
			else:
				for j in range(0,ceil(len(data.Get())/n)):
					if(len(numbers) != 0):
						random=sample(numbers,k=1)
						route.AddPlace(data.GetName(random[0]),data.GetValue(random[0]))
						numbers.remove(random[0])
			#Routes.append(route.Get())
			self.AddRoute(route)
		#print(route.Get())
		#return Routes

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