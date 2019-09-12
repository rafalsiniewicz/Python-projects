from program import *

program = Program()
program.ImportData()

#program.ShowData()

names = ["A", "B","C"]
program.SelectData(names)

program.ShowData()

program.InitializePopulation(1,100)

program.ShowLengths()

for i in range(0,1):
	program.PlayRound()

program.ShowLengths()

program.ShowBest()
