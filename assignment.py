import os
import sys
 

#Static objects
filename = "results.txt"
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


def loadMatrix(Matrix,operationId):
    file = read_file(filename)
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
            #print ("X AFTER",x)

            #EVALUATE TOP STUDENT

            if idx != 0 and idy != 0:
                if float(x) > 0:
                    averageTotals = averageTotals + float(x)

        
        #get average and optimize best value
        student_average = 0.0
        student_average = averageTotals/(len(Matrix[0]) - 1)
        if student_average > top_student_average:
            top_student_average = student_average
            top_student = str(Matrix[idy][0])
            
       

    
    return Matrix,top_student_average,top_student



#Parse result
def readResult(idval):
    COMPETITION = 0
    CHALLENGE = 1
    STUDENT = 2
    if idval != 5:
        #COMPETITION
        if idval == 0:
                file = read_file(filename)  # read file
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
                            if lineDisplayString == " -1":
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

                #LOAD MATIX
                MATRIX_RESULT = loadMatrix(Matrix,0)
                Matrix = MATRIX_RESULT[0]
                            #print(Matrix)

                num_students = len(Matrix) - 1
                num_challenges = len(Matrix[0]) - 1
                print ("There are",num_students,"Students and",num_challenges,"Challenges")
                print ("The top student is",MATRIX_RESULT[2],"with an average time of","{:.2f}".format(MATRIX_RESULT[1]),"minutes.")

                return MATRIX_RESULT

#
        elif idval == 1:
            file = read_file("challenges.txt")  # read file
            if(file != ''):
                    #print("\n\n--------------------------Start of DATA----------------------")
                print("\nCHALLENGE INFORMATION")
                itemList = file.read().split("\n")
                
                print("|---------------------------------------------------------------|")
                itemFields=""
                isFirstTime = True
                for item in itemList:
                    itemFields = item.split(",")

                        #print("Fields:",len(itemFields))
                        #print(itemFields)
                    string = '|\t'
                    for item in itemFields:
                        lineDisplayString = str(item)
                        string =string + lineDisplayString + "\t|\t"
           
                    print(string)
                    print("|---------------+---------------+---------------+---------------|")
        

                    w, h = len(itemFields), len(itemList)

                        #Initialize matrix
                Matrix = [[0 for x in range(w)] for y in range(h)]
                    #print("Records:",len(itemList))

    #DATA MAP
                #printData(Matrix)

                #LOAD MATIX
            MATRIX_RESULT = loadMatrix(Matrix,1)
            Matrix = MATRIX_RESULT[0]
                            #print(Matrix)

            num_students = len(Matrix) - 1
            num_challenges = len(Matrix[0]) - 1
            print ("The most difficult challenge is Vote (",most_difficult_challenge,"Students and",num_challenges,"Challenges")
            print ("The top student is",MATRIX_RESULT[2],"with an average time of","{:.2f}".format(MATRIX_RESULT[1]),"minutes.")

            return MATRIX_RESULT



class Competition():
    def __init__(self,id,Matrix):
        self.id = id
        self.Matrix= Matrix
        
        

class Student():
    def __init__(self,id,competitionResultArray):
        self.id = id
        self.competitionResultArray = competitionResultArray
        

class Challenge():

    pass


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

Matrix = readResult(0)[0]
competition = Competition(0,Matrix)

Matrix = readResult(1)[1]

#Matrix = readResult(0)[2]