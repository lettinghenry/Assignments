import os
from pickletools import dis
import sys
from unittest import result
 

#Static objects
global top_student_average
global top_student 


#static methods
# Method to read file
def read_file(filename):
    if os.path.exists(filename):
        file = open(filename)
        return file
    else:
        print("The file '", filename, " does NOT exist")
        return ''


def printData(dataMatrix):
    for idy, y in enumerate(dataMatrix):
        print(idy,y)
        for idx, x in enumerate(y):
            print(idx, x)


def loadResultsMatrix(Matrix):
    
    file = read_file("results.txt") #TODO globalize
    itemList=""
    top_student_average = 0.0
    top_student = ""
    if(file != ''):
        itemList = file.read().split("\n")
        itemFields=""
        for item in itemList:
            itemFields = item.split(",")

    for idy, item in enumerate(itemList):
        #print(idy,item)
        itemFields = item.split(",")

        most_difficult_challenge=''
        averageTotals = 0.0
        for idx, x in enumerate(itemFields):
            #print(idx, x)
            #Store in 2D Array
            Matrix[idy][idx] = x
            #print ("X BEFORE",x)
            x = x.strip()
            # print ("X AFTER",x)
            # print(Matrix)

            #EVALUATE TOP STUDENT
            if idx != 0 and idy != 0:
                if float(x) > 0 and not float(x) > 443:
                    averageTotals = averageTotals + float(x)
        
        #get average and optimize best value
        student_average = 0.0
        student_average = averageTotals/(len(Matrix[0]) - 1)
        if student_average > top_student_average:
            top_student_average = student_average
            top_student = str(Matrix[idy][0])
            
    
    return Matrix,top_student_average,top_student

def loadChallengesMatrix(Matrix):
    
    file = read_file("challenges.txt")
    itemList=""
    if(file != ''):
        itemList = file.read().split("\n")
        itemFields=""
        for item in itemList:
            itemFields = item.split(",")

    challengesList = []
    for idy, item in enumerate(itemList):
        #print(idy,item)
        itemFields = item.split(",")
        challengeFields = []
        most_difficult_challenge=''
        difficult_average_time = 0.0
        for idx, x in enumerate(itemFields):
            #print(idx, x)
            #Store in 2D Array
            Matrix[idy][idx] = x
            #print ("X BEFORE",x)
            x = x.strip()
            # print ("X AFTER",x)
            # print(Matrix)
            challengeFields.append(x)
        
        #create challenge object from the data fields
        challenge = Challenge(challengeFields[0],challengeFields[1],challengeFields[2],challengeFields[3])
        #add to the collection of challenges
        challengesList.append(challenge)


    return Matrix,challengesList


def loadStudentMatrix(Matrix):
    
    file = read_file("students.txt")
    itemList=""
    if(file != ''):
        itemList = file.read().split("\n")
        itemFields=""
        for item in itemList:
            itemFields = item.split(",")

    studentsList = []
    for idy, item in enumerate(itemList):
        #print(idy,item)
        itemFields = item.split(",")
        studentFields = []
        most_difficult_challenge=''
        averageTotals = 0.0
        for idx, x in enumerate(itemFields):
            #print(idx, x)
            #Store in 2D Array
            Matrix[idy][idx] = x
            #print ("X BEFORE",x)
            x = x.strip()
            studentFields.append(x)
        
        #create challenge object from the data fields
        student = Student(studentFields[0],studentFields[1],studentFields[2])
        
    #create a collection of challenges
    studentsList.append(student)

    return Matrix,studentsList

#Parse result
def readResult(idval,previousResult):
    COMPETITION = 0
    CHALLENGE = 1
    STUDENT = 2
    if idval != 5:
        #COMPETITION
        if idval == 0:
                file = read_file("results.txt")  # read file
                if(file != ''):
                    #print("\n\n--------------------------Start of DATA----------------------")
                    print("\nCOMPETITION DASHBOARD")
                    itemList = file.read().split("\n")
                    print("|-----------------------------------------------------------------------------------------------|")
                    itemFields=""
                    isFirstTime = True
                    for item in itemList:
                        itemFields = item.split(",")

                        #print("Fields:",len(itemFields))
                        #print(itemFields)
                        string = '|\t'
                        for item in itemFields:
                            lineDisplayString = str(item)
                            if isFirstTime :
                                lineDisplayString = "Results"
                                isFirstTime = False
                            if lineDisplayString.strip() == "-1":
                                lineDisplayString = "  "
                            if lineDisplayString.strip() == "444":
                                lineDisplayString = "--"
                            string =string +  lineDisplayString + "\t|\t"
           
                        print(string)
                        print("|---------------+---------------+---------------+---------------+---------------+---------------|")
        

                        w, h = len(itemFields), len(itemList)

                        #Initialize matrix
                    Matrix = [[0 for x in range(w)] for y in range(h)]
                    #print("Records:",len(itemList))

                #DATA MAP
                #printData(Matrix)
                #print("Matrix 1: " ,Matrix)
                #LOAD MATIX
                MATRIX_RESULT = loadResultsMatrix(Matrix)
                Matrix = MATRIX_RESULT[0]
                #print(Matrix)
                num_students = len(Matrix) - 1
                num_challenges = len(Matrix[0]) - 1
                print ("There are",num_students,"Students and",num_challenges,"Challenges")
                print ("The top student is",MATRIX_RESULT[2],"with an average time of","{:.2f}".format(MATRIX_RESULT[1]),"minutes.")

                return MATRIX_RESULT


        elif idval == 1:
            Matrix = []
            file = read_file("challenges.txt")  # read file
            if(file != ''):

                itemList = file.read().split("\n")
                itemFields=""
                isFirstTime = True
                for item in itemList:
                    itemFields = item.split(",")

                    w, h = len(itemFields), len(itemList)

                #Initialize matrix
                Matrix = [[0 for x in range(w)] for y in range(h)]
                # print("Matrix 2: " ,Matrix)

                #DATA MAP
                #printData(Matrix)
                #LOAD MATIX
            MATRIX_RESULT = loadChallengesMatrix(Matrix)
            Matrix = MATRIX_RESULT[0]
            challengesList = MATRIX_RESULT[1]
            competitionMatrix = previousResult
            updatedChallengesList = updateChallengeInfo(challengesList,competitionMatrix)
            challengeOutput = generateChallengeReport(updatedChallengesList)


            #print(Matrix)
            most_difficult_challenge =challengeOutput[0]
            difficult_avg_time = challengeOutput[1]
            num_students = len(Matrix) - 1
            num_challenges = len(Matrix[0]) - 1
            print ("The most difficult challenge is ", most_difficult_challenge.name ,"(",most_difficult_challenge.id,") with an average time of","{:.2f}".format(difficult_avg_time),"minutes.")
            print ("Report competition_report.txt generated!")

            return MATRIX_RESULT


def updateChallengeInfo(challengesList,competitionMatrix):
    #Loop through all the competitions and do a challenges summary
    nOngoingDict = {}
    nFinishDict = {}
    totalTimeDict = {}

    for idy, item in enumerate(competitionMatrix):
        for idx, x in enumerate(item):
            if idy != 0  and idx != 0:#not column or row header (labels)
                competitionLabel = competitionMatrix[0][idx].strip() #to be used as dictionary label
                if float(x.strip()) > 443:
                    if competitionLabel not in nOngoingDict:
                        nOngoingDict[competitionLabel] = 0#create new value to avoid issues
                    newValue = nOngoingDict[competitionLabel] + 1
                    nOngoingDict[competitionLabel] = newValue#replace value
                elif float(x.strip()) > 0 and float(x.strip()) < 444 :
                    if competitionLabel not in nFinishDict:
                        nFinishDict[competitionLabel] = 0#create new value to avoid issues
                    newValue = nFinishDict[competitionLabel] + 1
                    nFinishDict[competitionLabel] = newValue#replace value

                    #average time
                    if competitionLabel not in totalTimeDict:
                        totalTimeDict[competitionLabel] = 0
                    newTotal = totalTimeDict[competitionLabel] + float(x.strip())
                    totalTimeDict[competitionLabel] = newTotal
                    

    #create new challenges list to store for updates
    updatedChallengesList= []
    for challenge in challengesList:

        label = challenge.id.strip()

        #FINISH
        if label in nFinishDict:
            challenge.setNfinish(str(nFinishDict[label]))
            challenge.setTotalTime(str(totalTimeDict[label]))
        else:
            challenge.setNfinish("0")

        #ONGOING
        if label in nOngoingDict:
            challenge.setNongoing(str(nFinishDict[label]))
        else:
            challenge.setNongoing("0")

        updatedChallengesList.append(challenge)# new list

    return updatedChallengesList

def generateChallengeReport(updatedChallengesList):

    most_difficult_challenge=""
    difficult_avg_time =0
    displayString = "\nCHALLENGE INFORMATION\n"
    displayString = displayString + "+-----------------"*6 + "+\n"
    displayString = displayString + "|\t{0:10}|\t{1:15}|\t{2:10}|\t{3:10}|\t{4:10}|\t{5:10}|\n".format("Challenge","Name","Weight","Nfinish","Nongoing","AverageTime")
    displayString = displayString + "+-----------------"*6 + "+\n"
    for chl in updatedChallengesList:
        avg = float(chl.totalTime)/float(chl.nfinish)

        if avg>difficult_avg_time:#record most difficult
            difficult_avg_time = avg
            most_difficult_challenge = chl

        averageTime = "{:.2f}".format(avg)
        weight = "{:.1f}".format(float(chl.weight.strip()))
        displayString = displayString + "|\t{0:10}|\t{1:12}({2})|\t{3:10}|\t{4:10}|\t{5:10}|\t{6:10}|\n".format(chl.id,chl.name,chl.type,weight,chl.nfinish,chl.nongoing,averageTime)
    
    displayString = displayString + "+-----------------"*6 + "+\n"
    print(displayString)

    #WRITE TO FILE
    with open('competition_report.txt', 'w+') as f:
        f.write(displayString)

    return most_difficult_challenge ,difficult_avg_time 
    



class Competition():
    def __init__(self,Matrix):
        self.Matrix= Matrix
        
        
class Student():
    def __init__(self,id,name,val3):
        self.id = id
        self.name = name
        self.val3 = val3    

        

class Challenge():

    nongoing = ""
    nfinish = ""
    totalTime = ""

    def __init__(self,id,type,name,weight):
        self.id = id
        self.name = name
        self.type = type
        self.weight = weight

    def setNongoing(self,nongoing):
        self.nongoing = nongoing

    def setNfinish(self,nfinish):
        self.nfinish = nfinish

    def setTotalTime(self,totalTime):
        self.totalTime = totalTime



# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

if __name__ == '__main__':
	if n != 2:
		print ("[Usage:] assignment.py <result file>")
		sys.exit(1)

f = read_file(sys.argv[1])
if f=='':
    sys.exit(1)


#start the file reading as per the passed files
competition_matrix = readResult(0,"")
challenges_matrix = readResult(1,competition_matrix[0])
#Matrix = readResult(0)[2]