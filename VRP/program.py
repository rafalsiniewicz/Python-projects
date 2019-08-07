from numpy import *
from population import * 
from data_import import *

class Program:
	def __init__(self):
		self.population = Population()
		self.data = Data()
		self.size = 300

	def ImportData(self, name = "data.json"):
		self.data.Import(name)

	def ShowData(self):
		self.data.Show()
		print()

	def InitializePopulation(self, number_of_vehicles = 3, number_of_individuals_to_leave = 100):
		for i in range(0,self.size):
			ind=Individual()
			ind.CreateIndividual(self.data,number_of_vehicles)
			self.population.AddIndividual(ind)
		self.population.SortPopulation()
		self.population.LeavenBest(number_of_individuals_to_leave)
		self.size = number_of_individuals_to_leave



	def PlayRound(self, number_of_cycles = 50, number_of_crossings = 40, number_of_individuals_to_leave = 100):
		self.population.AddStart(START,END)
		self.population.SortPopulation()
		for j in range(0,number_of_cycles):
			self.population.RemoveStart()
			for i in range(0,number_of_crossings):
				self.population.AddIndividual(self.population.CrossingMerged())

			self.population.AddStart(START,END)
			self.population.SortPopulation()
			self.population.LeavenBest(number_of_individuals_to_leave)

		self.population.SortPopulation()


	def ShowPopulation(self):
		self.population.SortPopulation()
		self.population.Show()
		print()

	def ShowLengths(self):
		self.population.SortPopulation()
		for i in range(0,self.size):
			print(self.population.Getn(i).GetLength())
		print()


	def ShowBest(self):
		self.population.BestIndividual().Show()
		print()




