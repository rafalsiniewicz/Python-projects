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

	def Getn(self,n):
		return self.population[n]

	def GetSize(self):
		return len(self.population)


	def Check_if_correct(self):
		pass

	def AddStart(self,start,end):
		for i in self.population:
			for j in i.Get():
				j.Get().update(start)
				j.Get().move_to_end("START", last=False)
				j.Get().update(end)

	def RemoveStart(self):
		for i in self.population:
			for j in i.Get():
				j.Get().popitem(last=False)
				j.Get().popitem()

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

	def CrossingMerged(self):
		child = Individual()
		parent1 = randint(0,self.GetSize()-1)
		while True:
			parent2 = randint(0,self.GetSize()-1)
			if parent2 != parent1:
				break

		child_routes_length = []

		if self.population[parent1].GetSize() == 1:
			child_routes_length.append(len(self.population[parent1].Merge()))
		else:
			child_routes_length.append(randint(1,len(self.population[parent1].Merge())//2))
		#print(child_routes_length[0])
		def sum(child_routes_length):
			sum = 0
			for i in child_routes_length:
				sum += i 
			return sum
		
		for i in range(0,self.population[parent1].GetSize()-2):	# bo jedna dlugosc dodalismy wyzej i jedna dodamy nizej
			if sum(child_routes_length) + self.population[parent1].Getn(i).GetSize() < len(self.population[parent1].Merge()):
				child_routes_length.append(self.population[parent1].Getn(i).GetSize())
			elif sum(child_routes_length) + self.population[parent2].Getn(i).GetSize() < len(self.population[parent1].Merge()):
				child_routes_length.append(self.population[parent2].Getn(i).GetSize())
			else:
				child_routes_length.append(1)

		if self.population[parent1].GetSize() == 1:
			route = Route()
			wanted_items = list(self.population[parent1].Merge().items())[:child_routes_length[0]//2]
			for place, position in wanted_items:
				route.AddPlace(place,position)
			for place, position in self.population[parent2].Merge().items():
				#print(place,position)
				if child.Check_place(place) == False and route.Check_place(place) == False:
					route.AddPlace(place, position)
			child.AddRoute(route)

		else:
			child_routes_length.append(len(self.population[parent1].Merge())-sum(child_routes_length))

			for i in range(0,len(child_routes_length)):
				route = Route()
				if i == 0:
					wanted_items = list(self.population[parent1].Merge().items())[:child_routes_length[i]]
					for place, position in wanted_items:
						route.AddPlace(place,position)
				if i > 0:
					for j in range(0,child_routes_length[i]):
						#print(child_routes_length[i])
						for place, position in self.population[parent2].Merge().items():
							#print(place,position)
							if child.Check_place(place) == False and route.Check_place(place) == False:
								route.AddPlace(place, position)
								break
				child.AddRoute(route)


		#print(child_routes_length)
		#child.Show()
		return child


	def Mutation(self):	# zmienia ilosc punktow w poszczegolnych trasach
		parent = randint(0,self.GetSize()-1)

		def sum(new_routes_length):
			sum = 0
			for i in new_routes_length:
				sum += i 
			return sum

		new_routes_length = []
		new_routes_length.append(randint(1,len(self.population[parent].Merge())//2))
		for i in range(0,self.population[parent1].GetSize()-2):
			if sum(new_routes_length) < len(self.population[parent].Merge()):
				new_routes_length.append()

		self.population[parent].Merge()






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




