from program import *

program = Program()
program.ImportData()

program.ShowData()

program.InitializePopulation(2,100)

program.ShowLengths()

for i in range(0,1):
	program.PlayRound()

program.ShowLengths()

program.ShowBest()