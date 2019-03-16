import matplotlib.pyplot as plt
from graphics import *
import numpy as np
import random
import copy
import time


fig = plt.figure() 
plt.ion()

start_time = time.time()

def inside(point, rectangle):

        ll = rectangle.getP1()  
        ur = rectangle.getP2()  

        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


def main():
    win = GraphWin("Generowanie planu zajęć",600,500)
    win.setBackground(color_rgb(255,255,200))

    button = Rectangle(Point(100,440),Point(200,490))
    button.setFill("green")
    button.draw(win)

    button2 = Rectangle(Point(300,440),Point(400,490))
    button2.setFill("red")
    button2.draw(win)

    description =[Text(Point(100,30),"|NUMBER_OF_STUDENTS|"),Text(Point(300,30),"|MAX_MAIN_ALG_ITER|"),Text(Point(500,30),"|START_WORK_TIME|"),
    Text(Point(100,80),"|END_WORK_TIME|"), Text(Point(300,80),"|MAX_SOLUTION_FAILS|"), Text(Point(500,80),"|POPULATION_SIZE|"), 
    Text(Point(100,130),"|MATRICES_TO_NEXT_GEN|"), Text(Point(300,130),"|MUTATION_PROBABLITY|"), Text(Point(500,130),"|ATTEMPTS_TO_MUTATE|"),
    Text(Point(100,180),"|STUDENTS_TO_MUTATE|"), Text(Point(300,180),"|ATTEMPTS_TO_COMB_PAIR|"), Text(Point(500,180),"|COMBINE_PAIRS_STOP|"),
    Text(Point(100,230),"|MAX_GEN_WOUT_IMPROVE|"),Text(Point(300,230),"|SUBJECT_FAIL_FLAG|"), Text(Point(500,230),"|POSSIBILITY_FACTOR|"),
    Text(Point(100,280),"|COMB_ROWS_TO_REPLACE|")]

    input_box = []
    for i in range(0,len(description)):
        input_box.append(Entry(Point(description[i].getAnchor().getX(),description[i].getAnchor().getY()+20),10))
        input_box[i].draw(win)

    input_box[0].setText("40")
    input_box[1].setText("10")
    input_box[2].setText("08:00")
    input_box[3].setText("18:00")
    input_box[4].setText("1000")
    input_box[5].setText("30")
    input_box[6].setText("10")
    input_box[7].setText("50")
    input_box[8].setText("100")
    input_box[9].setText("4")
    input_box[10].setText("40")
    input_box[11].setText("200")
    input_box[12].setText("200")
    input_box[13].setText("5")
    input_box[14].setText("2")
    input_box[15].setText("5")


    for i in description:
        i.setSize(10)
        i.draw(win)
    
    time_str = Text(Point(200,380),"TIME:")
    time_str.draw(win)
    TIME = Text(Point(time_str.getAnchor().getX()+150,time_str.getAnchor().getY()),"")
    TIME.draw(win)

    max_val = Text(Point(200,350),"MAX. VALUE:")
    max_val.draw(win)
    MAX_VAL = Text(Point(max_val.getAnchor().getX()+150,max_val.getAnchor().getY()),"")
    MAX_VAL.draw(win)

    iter_str = Text(Point(200,410),"ITERATION:")
    iter_str.draw(win)
    ITER = Text(Point(iter_str.getAnchor().getX()+150,iter_str.getAnchor().getY()),"")
    ITER.draw(win)
    
    enter = Text(button.getCenter(),"ENTER")
    enter.draw(win)
    reset = Text(button2.getCenter(),"RESET")
    reset.draw(win)


    while True:
        clickPoint = win.getMouse()

        if clickPoint is None: 
            None
        elif inside(clickPoint, button):
            
            error_flag = 0

            error = [Text(Point(300,320),"Write valid value of NUMBER_OF_STUDENTS"), Text(Point(300,320),"Write valid value of MAX_MAIN_ALG_ITER"),
            Text(Point(300,320),"Write valid value of MAX_SOLUTION_FAILS"), Text(Point(300,320),"Write valid value of POPULATION_SIZE"),
            Text(Point(300,320),"Write valid value of MATRICES_TO_NEXT_GEN "),Text(Point(300,320),"Write valid value of MUTATION_PROBABLITY"),
            Text(Point(300,320),"Write valid value of ATTEMPTS_TO_MUTATE"),Text(Point(300,320),"Write valid value of STUDENTS_TO_MUTATE"),
            Text(Point(300,320),"Write valid value of ATTEMPTS_TO_COMB_PAIR"),Text(Point(300,320),"Write valid value of COMBINE_PAIRS_STOP"),
            Text(Point(300,320),"Write valid value of MAX_GEN_WOUT_IMPROVE"),Text(Point(300,320),"Write valid value of SUBJECT_FAIL_FLAG"),
            Text(Point(300,320),"Write valid value of POSSIBILITY_FACTOR"),Text(Point(300,320),"Write valid value of COMB_ROWS_TO_REPLACE")]

            if input_box[0].getText().isdigit() and int(input_box[0].getText()) > 0:
                NUMBER_OF_STUDENTS = int(input_box[0].getText())
            else:
                error[0].draw(win)
                continue
            if input_box[1].getText().isdigit() and int(input_box[1].getText()) > 0:
                MAX_MAIN_ALG_ITER = int(input_box[1].getText())
            else:
                error[1].draw(win)
                continue
            if input_box[4].getText().isdigit() and int(input_box[4].getText()) > 0:
                MAX_SOLUTION_FAILS = int(input_box[4].getText())
            else:
                error[2].draw(win)
                continue
            if input_box[5].getText().isdigit() and int(input_box[5].getText()) > 0:
                POPULATION_SIZE = int(input_box[5].getText())
            else:
                error[3].draw(win)
                continue
            if input_box[6].getText().isdigit() and int(input_box[6].getText()) > 0:
                MATRICES_TO_NEXT_GEN = int(input_box[6].getText())
            else:
                error[4].draw(win)
                continue
            if input_box[7].getText().isdigit() and int(input_box[7].getText()) > 0 and int(input_box[7].getText()) <= 100:
                MUTATION_PROBABLITY = int(input_box[7].getText())
            else:
                error[5].draw(win)
                continue
            if input_box[8].getText().isdigit() and int(input_box[8].getText()) > 0:
                ATTEMPTS_TO_MUTATE = int(input_box[8].getText())
            else:
                error[6].draw(win)
                continue
            if input_box[9].getText().isdigit() and int(input_box[9].getText()) > 0:
                STUDENTS_TO_MUTATE = int(input_box[9].getText())
            else:
                error[7].draw(win)
                continue
            if input_box[10].getText().isdigit() and int(input_box[10].getText()) > 0:
                ATTEMPTS_TO_COMB_PAIR = int(input_box[10].getText())
            else:
                error[8].draw(win)
                continue
            if input_box[11].getText().isdigit() and int(input_box[11].getText()) > 0:
                COMBINE_PAIRS_STOP = int(input_box[11].getText())
            else:
                error[9].draw(win)
                continue
            if input_box[12].getText().isdigit() and int(input_box[12].getText()) > 0:
                MAX_GEN_WOUT_IMPROVE = int(input_box[12].getText())
            else:
                error[10].draw(win)
                continue
            if input_box[13].getText().isdigit() and int(input_box[13].getText()) > 0:
                SUBJECT_FAIL_FLAG = int(input_box[13].getText())
            else:
                error[11].draw(win)
                continue
            if input_box[14].getText().isdigit() and int(input_box[14].getText()) > 0:
                POSSIBILITY_FACTOR= int(input_box[14].getText())
            else:
                error[12].draw(win)
                continue
            if input_box[15].getText().isdigit() and int(input_box[15].getText()) > 0:
                COMB_ROWS_TO_REPLACE= int(input_box[15].getText())
            else:
                error[13].draw(win)
                continue



            START_WORK_TIME = input_box[2].getText()
            END_WORK_TIME = input_box[3].getText()
            file = open("output.txt","w+")
            plt.cla()      

            #NUMBER_OF_STUDENTS = 40
            #MAXIT = 100
            #MAXIT2 = 500
            #SUBJECT_FAIL_FLAG = 5
            #START_WORK_TIME = '08:00'
            #END_WORK_TIME = '18:00'  
            MINIMAL_BREAK = np.timedelta64(6*60,'m')
            #POSSIBILITY_FACTOR = 2
            #MAX_SOLUTION_FAILS = 1000

            #POPULATION_SIZE = 30
            #MATRICES_TO_NEXT_GEN = 10
            #MUTATION_PROBABLITY = 50 #in percentage, must be >0.0
            #ATTEMPTS_TO_MUTATE = 100
            #STUDENTS_TO_MUTATE = 4

            #ATTEMPTS_TO_COMB_PAIR = 40
            #COMBINE_PAIRS_STOP = 200
            #MAX_GEN_WOUT_IMPROVE = 200
            #MAX_MAIN_ALG_ITER = 1000
            #COMB_ROWS_TO_REPLACE = 5

            endRandIntRange = int((100/MUTATION_PROBABLITY)*POPULATION_SIZE)
            numberOfGroups = 0
            deansGroupsSizes = [16, 12]

            workMinPerFreeDay = np.datetime64('2000-01-01T' + END_WORK_TIME) - np.datetime64('2000-01-01T' + START_WORK_TIME)



            ####### Program Diagnostic ########
            filledSubjectsInMatrix = 0
            filledGroupsInSubject = 0

            #Jeden przedmiot w jednym wierszu, kazda kolumna to grupa danego przedmiotu, np. 1a, 1b, itd.

            schedule    =  [[np.timedelta64(90,'m'), [np.datetime64('2000-01-01T12:30'), np.datetime64('2000-01-01T14:00'), np.datetime64('2000-01-04T20:30')]],
                            [np.timedelta64(135,'m'), [np.datetime64('2000-01-02T00:30'), np.datetime64('2000-01-03T18:00'), np.datetime64('2000-01-03T15:00'),  np.datetime64('2000-01-05T21:45')]],
                            [np.timedelta64(90,'m'), [np.datetime64('2000-01-05T06:00'), np.datetime64('2000-01-05T08:00'), np.datetime64('2000-01-04T16:30')]],
                            [np.timedelta64(90,'m'), [np.datetime64('2000-01-01T11:30'), np.datetime64('2000-01-04T07:00'), np.datetime64('2000-01-02T12:30')]]]

            # będziemy uzywac tylko w ograniczeniach i liczeniu okienek
            deanSchedule    =  [[np.timedelta64(90,'m'),[np.datetime64('2000-01-01T00:30'),np.datetime64('2000-01-01T19:15'),np.datetime64('2000-01-02T14:00')]],
                            [np.timedelta64(90,'m'), [np.datetime64('2000-01-02T16:00'), np.datetime64('2000-01-03T05:00'), np.datetime64('2000-01-03T02:00')]],
                            [np.timedelta64(90,'m'), [np.datetime64('2000-01-04T11:00'), np.datetime64('2000-01-04T08:00'),np.datetime64('2000-01-01T10:00')]]]


            groupLimits = [[8, 16],     #Minimal and maximal number of students in groups
                        [5, 14],
                        [8, 16],
                        [8, 16]]
                         


            deansGroup = np.zeros((NUMBER_OF_STUDENTS,1), dtype = 'i2')

            deansGroupsSizes.append(NUMBER_OF_STUDENTS - np.sum(deansGroupsSizes))


            licznik = 0
            licznik2 = 1
            for Size in deansGroupsSizes:
                for number in range(1,Size + 1):
                    deansGroup[licznik] = licznik2
                    licznik+=1
                licznik2+=1

                 
            for subject in schedule:
                numberOfGroups = numberOfGroups + len(subject[1])

            Matrix = np.zeros((NUMBER_OF_STUDENTS, numberOfGroups),dtype = '?')


            def doClassesCover ( time1: np.datetime64, delay1: np.timedelta64, time2: np.datetime64, delay2: np.timedelta64 ):
                
                if time1 == time2:
                    return True
                elif (time1 > time2) and (time1 < time2 + delay2):
                    return True
                elif (time1 + delay1 > time2) and (time1 + delay1 < time2 + delay2):
                    return True
                elif (time2 > time1) and (time2 < time1 + delay1):
                    return True
                elif (time2 + delay2 > time1) and (time2 + delay2 < time1 + delay1):
                    return True    
                else:
                    return False

            def localScheduleTrimmer (timesList,vector):
                newTimesList = []
                if len(timesList) != len(vector):
                    return False
                for i in range ( 0, len(timesList) ):
                    if vector[i] == True:
                        newTimesList.append(timesList[i])
                if len(newTimesList) == 1:
                    return newTimesList
                else:
                    return []
             
            def checkLocalSchedule( local_schedule ):
                for i in range( 0, len(local_schedule )):
                    if local_schedule[i][1] != []:
                        for j in range( 0, len(local_schedule) ):
                            if i != j and local_schedule[j][1] != [] :
                                if doClassesCover( local_schedule[i][1][0],
                                                local_schedule[i][0],
                                                local_schedule[j][1][0],
                                                local_schedule[j][0] ) == True:
                                    return False
                return True

                
            def checkLocalDeansSchedule( local_schedule, localDeansSchedule, thisStudentDeansGroup: int ):
                for i in range(0, len(local_schedule)):
                    if local_schedule[i][1] != []:
                        for j in range(0, len(localDeansSchedule)):
                            if doClassesCover( local_schedule[i][1][0], local_schedule[i][0], localDeansSchedule[j][1][int(thisStudentDeansGroup)], localDeansSchedule[j][0] ) == True:
                                return False
                return True

            def ograniczenia(Rozw, schedule):
                
                
                #sprawdzanie liczebnosci grup
                licznik2 = 0
                for i in range(0,len(schedule)):
                    licznik = 0
                    for j in range(0,len((schedule[i])[1])):        #zmiana28.12 Rafal
                        if ( ( np.sum(Rozw[:,licznik + licznik2]) < groupLimits[i][0] ) or ( np.sum(Rozw[:,licznik+licznik2]) > groupLimits[i][1] ) ):
                            print('Blad sprawdzenia liczebnosci grup przedmiot: ', i,' grupa: ', j)
                            return False
                        licznik += 1                 
                        if(j == len((schedule[i])[1])-1):       #zmiana 28.12 Rafal - dodanie zmiennej licznik2
                            licznik2 += licznik
                     
                #sprawdzanie czy kazdy student ma dokladnie po jednej grupie z przedmiotu
                for student in range(0,len(Rozw[:,0])):
                    last_known_position = 0
                    for przedmiot in range(0,len(schedule)):
                        if ( np.sum(Rozw[ student, last_known_position : ( last_known_position + len(schedule[przedmiot][1]) ) ]) != 1 ):
                            print('Blad sprawdzenia czy kazdy student ma dokladnie po jednej grupie z przedmiotu student: ', student)
                            return False
                        last_known_position += len(schedule[przedmiot][1])
                     
                #sprawdzanie kolizji zajec
                #mnożenie odpowiednich częsci wektora studenta przez odpowiednie częsci tablicy godzin "schedule" i sprawdzanie pokryć
                for student in range(0,len(Rozw[:,0])):
                    local_schedule = copy.deepcopy(schedule)
                    last_known_position = 0
                    for przedmiot in range( 0, (len(schedule)) ):
                        local_schedule[przedmiot][1] = localScheduleTrimmer(local_schedule[przedmiot][1],Rozw[ student, last_known_position : last_known_position + len(schedule[przedmiot][1])])
                        last_known_position += len(schedule[przedmiot][1])
                    if checkLocalSchedule( local_schedule ) == False:
                        print( 'Dobrane przez program grupy nachodza miedzy soba student: ', student )
                        return False
                    if checkLocalDeansSchedule(local_schedule, deanSchedule, deansGroup[student]-1) == False:
                        print( 'Dobrane przez program grupy nachodza na zajecia dziekanskie, student: ', student )
                        return False
                return True

            def ShowMatrix(ShownMatrix, character, beginingPosVector):
                matrix = ""
                for row in ShownMatrix:
                    for col in range(0,len(row)):
                        matrix += str(row[col])
                        #print(row[col],end=' ')
                        for elem in beginingPosVector:
                            if col == elem - 1:
                                matrix += " "
                                #print(character, end=' ')
                    matrix += "\n"
                    #print() # przejscie do kolejnego wiersza
                return matrix
                 
            # getStudentSchedule zwraca posortowaną chronologicznie listę list postaci
            # [czas rozpoczecia zajec1, czas zakonczenia zajec1, symbol przedmiotu]
            # gdzie symbol przedmiotu np: 's0' - zerowy(pierwszy w kolejnosci) przedmiot na liscie schedule
            # 'd2' - drugi(trzeci w kolejnosci) przedmiot na liscie deanSchedule
            def getStudentSchedule(studentID, deanSchedule, deansGroup, Matrix, schedule, subjectsLocations):
                deanGroupNumber = deansGroup[studentID]
                studentSchedule = []
                numberOfDeansGroup = len(deanSchedule)
                for deanCounter in range(0, numberOfDeansGroup):
                    studentSchedule.append([])
                    studentSchedule[deanCounter].append(deanSchedule[deanCounter][1][int(deanGroupNumber) - 1])
                    studentSchedule[deanCounter].append(deanSchedule[deanCounter][1][int(deanGroupNumber) - 1] + deanSchedule[deanCounter][0])
                    studentSchedule[deanCounter].append("d"+str(deanCounter))
                subjectNumber = -1
                rangeBegin = 0
                subjectsLocationsMod = subjectsLocations #+ [subjectsLocations[-1] + len(schedule[-1][1])]
                for rangeEnd in subjectsLocationsMod[1:]:
                    studentSchedule.append([])
                    subjectNumber +=1
                    for matrixIndex in range(rangeBegin, rangeEnd):
                        if Matrix[studentID][matrixIndex] == True:
                            studentSchedule[subjectNumber + numberOfDeansGroup].append(schedule[subjectNumber][1][matrixIndex - rangeBegin])
                            studentSchedule[subjectNumber + numberOfDeansGroup].append(schedule[subjectNumber][1][matrixIndex - rangeBegin] + schedule[subjectNumber][0])
                            studentSchedule[subjectNumber + numberOfDeansGroup].append("s"+str(subjectNumber))
                    rangeBegin = rangeEnd
                studentSchedule.sort()
                return studentSchedule





            def studentWorkHours(studentSchedule, workMinPerFreeDay, startWorkTime, endWorkTime, minimalBreak):
                WorkTime = np.timedelta64(0,'m')
                for cnt in range(1, len(studentSchedule)):
                    prevClass = studentSchedule[cnt-1]
                    nextClass = studentSchedule[cnt]
                    prevClassDay = str(prevClass[0])[9]
                    nextClassDay = str(nextClass[0])[9]
                    # od ktorej i do ktorejgodz mozna pracowac w tym dniu
                    startWorkTimePrev = np.datetime64('2000-01-0' + prevClassDay + 'T' + startWorkTime)
                    endWorkTimePrev = np.datetime64('2000-01-0' + prevClassDay + 'T' + endWorkTime)
                    startWorkTimeNext = np.datetime64('2000-01-0' + nextClassDay + 'T' + startWorkTime)
                    endWorkTimeNext = np.datetime64('2000-01-0' + nextClassDay + 'T' + endWorkTime)
                    #pierwsze zajecia w tygodniu
                    if(cnt == 1):
                        WorkTime += workMinPerFreeDay*(int(prevClassDay)-1)
                        if(prevClass[0] - startWorkTimePrev > minimalBreak):
                            WorkTime += prevClass[0]-startWorkTimePrev
                    if(cnt == len(studentSchedule)-1):
                        WorkTime += workMinPerFreeDay*(5-int(nextClassDay))
                        if(nextClass[1] < startWorkTimeNext):
                            WorkTime += workMinPerFreeDay  
                        if(nextClass[1] > startWorkTimeNext and endWorkTimeNext - nextClass[1] >= minimalBreak):
                            WorkTime += endWorkTimeNext - nextClass[1]
                    if(nextClassDay == prevClassDay):
                        if(nextClass[0] - prevClass[1] >= minimalBreak):
                            if(prevClass[1] < startWorkTimePrev and nextClass[0] > startWorkTimePrev and nextClass[0] <= endWorkTimePrev):
                                if(nextClass[0] - startWorkTimePrev >= minimalBreak):
                                    WorkTime += nextClass[0] - startWorkTimePrev
                            if(prevClass[1] >= startWorkTimePrev and nextClass[0] <= endWorkTimePrev):
                                WorkTime += nextClass[0] - prevClass[1]
                            if(prevClass[1] <= endWorkTimePrev and prevClass[1] >= startWorkTimePrev and nextClass[0] > endWorkTimePrev):
                                if(endWorkTimePrev - prevClass[1] >= minimalBreak):
                                    WorkTime += endWorkTimePrev - prevClass[1]
                            if(prevClass[1] < startWorkTimePrev and nextClass[0] > endWorkTimePrev):
                                WorkTime += workMinPerFreeDay
                    else:
                        WorkTime += workMinPerFreeDay*(int(nextClassDay)- int(prevClassDay)-1)
                        if(prevClass[1] < startWorkTimePrev):
                            WorkTime += workMinPerFreeDay   
                        if(prevClass[1] > startWorkTimePrev and endWorkTimePrev - prevClass[1] >= minimalBreak):
                            WorkTime += endWorkTimePrev - prevClass[1]
                        if(nextClass[0] - startWorkTimeNext >= minimalBreak and nextClass[0] < endWorkTimeNext):
                            WorkTime += nextClass[0] - startWorkTimeNext
                        if(nextClass[0] >= endWorkTimeNext):
                            WorkTime += workMinPerFreeDay
                         
                return WorkTime

            def AverageTimePerStudent(deanSchedule, deansGroup, Matrix, schedule, subjectsLocations,
                                    workMinPerFreeDay, startWorkTime, endWorkTime, minimalBreak):
                WorkTimeSum = np.timedelta64(0,'m')
                numberOfStudents = len(Matrix)
                for studentID in range(0,numberOfStudents):
                    plan = getStudentSchedule(studentID, deanSchedule, deansGroup, Matrix, schedule, subjectsLocations)
                    WorkTimeSum += studentWorkHours(plan, workMinPerFreeDay, startWorkTime, endWorkTime, minimalBreak)
                return WorkTimeSum/numberOfStudents


            def CountStudentsInGroup(Matrix):
                tab = []
                for index in range(0, len(Matrix[0])):
                    tab.append(np.sum(Matrix[:,index]))
                return tab

            # MutateMatrix tylko podmienia jedynki dla n studentow - nie sprawdza czy wynik zgodny z ograniczeniami
            # studentsNumber - maksymalnie 3 - im wiecej tym mniejsze prawdopodobienstwo
            # ze funkcja zwroci macierz spelniajaca ograniczenia
            def MutateMatrix(matrix, subjectsLocations, studentsToMutation, printPos):
                Matrix = copy.deepcopy(matrix)
                studentsNumbers = random.sample(range(0, len(Matrix)), studentsToMutation)
                for studentNumber in studentsNumbers:    
                    #losowanie przedmiotu w ktorym bedzie zmiana
                    subjectNumber = random.randint(0, len(subjectsLocations)-2)
                    oldOnepos = 0
                    for i in range(subjectsLocations[subjectNumber], subjectsLocations[subjectNumber + 1]):
                        if Matrix[studentNumber][i] == True:
                            oldOnepos = i
                    Matrix[studentNumber][oldOnepos] = False
                    if(printPos):
                        print(studentNumber, oldOnepos)
                    direction = random.choice([True, False])
                    if direction == True:
                        if oldOnepos + 1 < subjectsLocations[subjectNumber + 1]:
                            Matrix[studentNumber][oldOnepos + 1] = True
                        else:
                            Matrix[studentNumber][oldOnepos - 1] = True
                    else:
                        if oldOnepos - 1 >= subjectsLocations[subjectNumber]:
                            Matrix[studentNumber][oldOnepos - 1] = True
                        else:
                            Matrix[studentNumber][oldOnepos + 1] = True
                return Matrix
                         
                 

            def CombineMatrices(mainMatrix, secondaryMatrix, rowsToReplace, printRowNumbers):
                MainMatrix = copy.deepcopy(mainMatrix)
                rowsNumbers = random.sample(range(0, len(MainMatrix)), rowsToReplace)
                for rowNumber in rowsNumbers:
                    if(printRowNumbers):
                        print(rowNumber)
                    MainMatrix[rowNumber] = secondaryMatrix[rowNumber]   
                return MainMatrix
                
            blabla = lambda argument: argument[0]
            ###############################Generowanie pierwszego rozwiazania##########################
                

            def SolveMatrix(schedule, deanSchedule, groupLimits):
                Matrix = np.zeros((NUMBER_OF_STUDENTS, numberOfGroups),dtype = '?')
                numberOfSubjects = len(schedule)
                subjectsLocations=[]
                for subject in range(numberOfSubjects-1):
                    if subject > 0:
                        subjectsLocations.append(subjectsLocations[subject-1] + len(schedule[subject][1]))
                    else:
                        subjectsLocations.append(len(schedule[subject][1]))
                subjectsLocations.append(len(Matrix[0]))
                subjectsLocations.insert(0,0)
                emptySchedule = copy.deepcopy(schedule)
                for subject in range(numberOfSubjects):
                    emptySchedule[subject][1] = []
                emptySchedule [0][1] = []
                
                subject = 0
                student = 0
                group = 0
                solutionFailFlag = MAX_SOLUTION_FAILS
                subjectFailFlag = SUBJECT_FAIL_FLAG

                while subject < numberOfSubjects and solutionFailFlag > 0:
                    numberOfGroupsInSubject = len(schedule[subject][1])
                    placesLeft = np.ones((numberOfGroupsInSubject,))*groupLimits[subject][1]
                 
                    student = 0
                    while student < NUMBER_OF_STUDENTS:
                        availableGroups = []
                        groupPossibilities = []
                        group = 0
                        while group < numberOfGroupsInSubject:
                            Matrix[student][group+subjectsLocations[subject]] = True
                            #tworzymy schedule dla danego studenta
                            studentsSchedule = copy.deepcopy(emptySchedule)
                            studentsSchedule[subject][1] = []
                            for subject_2 in range(numberOfSubjects):
                                studentsSchedule[subject_2][1] = localScheduleTrimmer(schedule[subject_2][1], Matrix[student, subjectsLocations[subject_2]:subjectsLocations[subject_2+1]])
                            if checkLocalSchedule(studentsSchedule) and checkLocalDeansSchedule(studentsSchedule,deanSchedule,deansGroup[student]-1):
                                availableGroups.append(group)
                                if groupLimits[subject][1] - placesLeft[group] < groupLimits[subject][0]:
                                    groupPossibilities.append(POSSIBILITY_FACTOR*placesLeft[group])
                                else:
                                    groupPossibilities.append(placesLeft[group])
                            Matrix[student][group+subjectsLocations[subject]] = False
                            group += 1
                     
                        if availableGroups == [] or sum(groupPossibilities) == 0:
                            #jesli student nie ma mozliwych grup wtedy zerujemy przedmiot
                            subjectMatrix = np.zeros((NUMBER_OF_STUDENTS,numberOfGroupsInSubject))
                            #przypisujemy macierz zer do aktualnie sprawdzanego przedmiotu
                            Matrix[:,subjectsLocations[subject]:subjectsLocations[subject]+numberOfGroupsInSubject] = subjectMatrix
                            subjectFailFlag -= 1
                            subject -= 1
                            if subjectFailFlag == 0:
                                if subject != 0:
                             
                                    #jesli nie udalo sie wygenerowac danego przedmiotu zbyt duzo razy zerujemy ten przedmiot i poprzedni i cofamy sie o przedmiot
                                    subjectMatrix = np.zeros((NUMBER_OF_STUDENTS, subjectsLocations[subject] - subjectsLocations[subject-1]))
                                    Matrix[:,subjectsLocations[subject-1]:subjectsLocations[subject]] = subjectMatrix
                                    subject -= 1
                                    subjectFailFlag=SUBJECT_FAIL_FLAG
                                else:
                                    solutionFailFlag -= 1
                                 
                            student = NUMBER_OF_STUDENTS
                         
                        else:
                            groupPossibilities /= np.sum(np.array(groupPossibilities))
                            chosenGroup = np.random.choice(availableGroups, p = groupPossibilities)          
                            Matrix[student][subjectsLocations[subject]+chosenGroup] = True
                            placesLeft[chosenGroup] -= 1
                            student += 1
                    subject += 1
                return (Matrix, subjectsLocations)


            ########################### - Populacja - ###########################
            Matrix, subjectsLocations = SolveMatrix(schedule, deanSchedule, groupLimits)   
            Matrix2, subjectsLocations = SolveMatrix(schedule, deanSchedule, groupLimits)


            ###############################----MAIN-PROGRAMME----#####################################
            #################### init ##############################
            Population = []
            for cnt in range(0,POPULATION_SIZE):
                Matrix, subjectsLocations = SolveMatrix(schedule, deanSchedule, groupLimits)
                objFuncValue = AverageTimePerStudent(deanSchedule, deansGroup, Matrix, schedule, subjectsLocations,
                                    workMinPerFreeDay, START_WORK_TIME, END_WORK_TIME, MINIMAL_BREAK)
                Population.append([objFuncValue, copy.deepcopy(Matrix)])
                
            Population.sort(reverse = True, key = blabla)
            BestMatrix, bestObjectFunc = copy.deepcopy(Population[0][1]), Population[0][0]

            genIterCnt = genWoutImproveCnt = 0

            while(genIterCnt < MAX_MAIN_ALG_ITER and genWoutImproveCnt < MAX_GEN_WOUT_IMPROVE):
                del Population[MATRICES_TO_NEXT_GEN:]
                ########### Mutating #########
                toMutate = random.randint(0, endRandIntRange)
                mutationCounter = 0
                if(toMutate < MATRICES_TO_NEXT_GEN):    #sprawdzamy czy mutacja w tej iteracji ma sie odbyc i na którym osobniku
                    while(mutationCounter < ATTEMPTS_TO_MUTATE):
                        mutMatrix = MutateMatrix(Population[toMutate][1], subjectsLocations, STUDENTS_TO_MUTATE, printPos = False)
                        if(ograniczenia(mutMatrix, schedule) == True):
                            #print(mutationCounter)
                            Population[toMutate][0] = AverageTimePerStudent(deanSchedule, deansGroup, mutMatrix, schedule, subjectsLocations,
                                        workMinPerFreeDay, START_WORK_TIME, END_WORK_TIME, MINIMAL_BREAK)
                            Population[toMutate][1] = copy.deepcopy(mutMatrix)
                            mutationCounter = ATTEMPTS_TO_MUTATE
                        mutationCounter += 1
                
                ########### Combining #############
                combiningCounter = 0
                while(combiningCounter < COMBINE_PAIRS_STOP):
                    matricesNumbers = random.sample(range(0, MATRICES_TO_NEXT_GEN), 2)
                    mainNumber, secondaryNumber = matricesNumbers[0], matricesNumbers[1]
                    combPairCounter = 0
                    while(combPairCounter < ATTEMPTS_TO_COMB_PAIR):
                        combMatrix = CombineMatrices(Population[mainNumber][1], Population[secondaryNumber][1],
                                            COMB_ROWS_TO_REPLACE, printRowNumbers= False)
                        if(ograniczenia(combMatrix, schedule) == True):
                            #print(nrIteracji, combPairCounter)
                            objFuncValue = AverageTimePerStudent(deanSchedule, deansGroup, combMatrix, schedule, subjectsLocations,
                                        workMinPerFreeDay, START_WORK_TIME, END_WORK_TIME, MINIMAL_BREAK)
                            Population.append([objFuncValue, copy.deepcopy(combMatrix)])
                            combPairCounter = ATTEMPTS_TO_MUTATE
                        combPairCounter += 1
                    combiningCounter += 1
                    if(len(Population) >= POPULATION_SIZE):
                        combiningCounter = COMBINE_PAIRS_STOP
                        #print(nrIteracji, combiningCounter)  
                 
                Population.sort(reverse = True, key = blabla)
                if(Population[0][0] > bestObjectFunc):
                    BestMatrix, bestObjectFunc = copy.deepcopy(Population[0][1]), Population[0][0]
                    genWoutImproveCnt = 0
                else:
                    genWoutImproveCnt += 1
                print(genIterCnt, "XXXX", bestObjectFunc,"XXXX")
                plt.scatter(genIterCnt, bestObjectFunc.astype(int), color='k')
                plt.xlabel('iterations')
                plt.ylabel('objective function value')
                plt.show()
                #plt.show()
                MAX_VAL.setText("")
                MAX_VAL.setText(bestObjectFunc)
                ITER.setText(genIterCnt)
                genIterCnt +=1



                





                
            ShownMatrix2 = np.ones((NUMBER_OF_STUDENTS, numberOfGroups),dtype = 'i2')
            ShownMatrix2 = Matrix*ShownMatrix2

            matrix = ShowMatrix(ShownMatrix2, " ", subjectsLocations)
            TIME.setText("")
            TIME.setText(" %s seconds" % (time.time() - start_time))
            file.write("Maximal value of objective function: %s\n" %(str(MAX_VAL.getText())))
            file.write("Time table: \n%s" %matrix)
            file.close() 
            

        elif inside(clickPoint, button2):
            input_box[0].setText("40")
            input_box[1].setText("10")
            input_box[2].setText("08:00")
            input_box[3].setText("18:00")
            input_box[4].setText("1000")
            input_box[5].setText("30")
            input_box[6].setText("10")
            input_box[7].setText("50")
            input_box[8].setText("100")
            input_box[9].setText("4")
            input_box[10].setText("40")
            input_box[11].setText("200")
            input_box[12].setText("200")
            input_box[13].setText("5")
            input_box[14].setText("2")
            input_box[15].setText("5")
            for i in error:
                i.setText("")
            TIME.setText("")
            MAX_VAL.setText("")
            ITER.setText("")
            plt.cla()

        else:
            None


    win.getMouse()
    win.close()


main()

