from individual import *

class Population:
	def __init__(self):
		self.population = []

	def AddIndividual(self,individual):
		self.population.append(individual)

	def Show(self):
		for i in range(0,len(self.population)):
			for j in range(0,len(self.population[i].Get())):
				print(self.population[i].Get()[j].Get(),end="")
			print()

	def Get(self):
		return self.population

	def Get(self,n):
		return self.population[n]

	def GetSize(self):
		return len(self.population)


	def Check_if_correct(self):
		pass


	def Crossing(self):
		child = Individual()
		parent1 = randint(0,self.GetSize()-1)
		while True:
			parent2 = randint(0,self.GetSize()-1)
			if parent2 != parent1:
				break

		#dla Individuala majacego co najmniej 3 Routy
		parent1_route = self.population[parent1].Get()[1]	#drugi Route z parent1
		#print(self.population[parent1].GetSize())
		for i in range(0,self.population[parent1].GetSize()):
			route = Route()
			if i == 1:
				child.AddRoute(self.population[parent1].Get()[1])
			if i != 1:
				for j in range(0,self.population[parent2].GetSize()):
					for place, position in self.population[parent2].Get()[j].Get().items():
						if parent1_route.Check_place(place) == False and child.Check_place(place) == False and route.GetSize() < self.population[parent1].Get()[i].GetSize():
							route.AddPlace(place,position)
						#print(place,position,end="")
				child.AddRoute(route)
				#print()
		
		return child
		'''print(child.Check_if_correct())
		self.population[parent1].Show()
		print()
		self.population[parent2].Show()
		print()
		child.Show()'''
		#print(self.population[parent1].Get()[0].Get())

	def SortPopulation(self):
		def GetIndividualLength(individual):
			return individual.GetLength()
		self.population.sort(key=GetIndividualLength)
		

	def BestIndividual(self):
		min_length = self.population[0].GetLength()
		best = self.population[0]
		for i in range(1,len(self.population)):
			if self.population[i].GetLength() < min_length:
				min_length = self.population[i].GetLength()
				best = self.population[i]
		return best


	def LeavenBest(self,n):
		for i in range(n,self.GetSize()):
			self.population.pop()




