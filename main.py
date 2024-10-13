import libfuzzy
import visualize

### Declare linguistic variables
## Input variables
gradesOfSemester1=libfuzzy.LinguisticVariable(name="Semester-1")
gradesOfSemester2=libfuzzy.LinguisticVariable(name="Semester-2")

# Populate the variables with the corresponding membership functions and names
triangleFunctionGenerator=libfuzzy.utils.createTriangularFunction
tags=["VL","L","A","H","VH"]
triangleMarks=[[0,0,25],[0,25,50],[25,50,75],[50,75,100],[75,100,100]]

for i in range(5):
    gradesOfSemester1.addFuzzySet(
        linguisticValue=tags[i],
        membershipFunction=triangleFunctionGenerator(triangleMarks[i])
    )
    gradesOfSemester2.addFuzzySet(
        linguisticValue=tags[i],
        membershipFunction=triangleFunctionGenerator(triangleMarks[i])
    )

## Output variable
finalPerformance=libfuzzy.LinguisticVariable(name="Performance")

tags=["VU","U","A","S","VS"]
triangleMarks=[[0,0,0.25],[0,0.25,0.50],[0.25,0.50,0.75],[0.50,0.75,1],[0.75,1,1]]

for i in range(5):
    finalPerformance.addFuzzySet(
        linguisticValue=tags[i],
        membershipFunction=triangleFunctionGenerator(triangleMarks[i])
    )

### Inference rules

inferenceRules=[0]*25

for i in range(5):
    for j in range(5):
        if i<2 or (i==2 and j<=2):
            inferenceRules[5*i+j]=\
                    libfuzzy.LinguisticVariable.FuzzyLogic.IfAndThen(
                            gradesOfSemester1.fuzzySets[i],
                            gradesOfSemester2.fuzzySets[j],
                            finalPerformance.fuzzySets[(i+j)//2]
            )
        else:
            inferenceRules[5*i+j]=\
                    libfuzzy.LinguisticVariable.FuzzyLogic.IfAndThen(
                            gradesOfSemester1.fuzzySets[i],
                            gradesOfSemester2.fuzzySets[j],
                            finalPerformance.fuzzySets[(i+j)//2+(i+j)%2]
            )
    else:
        inferenceRules[5*i+j]=\
            libfuzzy.LinguisticVariable.FuzzyLogic.IfAndThen(
                    gradesOfSemester1.fuzzySets[i],
                    gradesOfSemester2.fuzzySets[j],
                    finalPerformance.fuzzySets[(i+j)//2+(i+j)%2]
        )

## Debugging
for i in range(5):
    for j in range(5):
        print(inferenceRules[5*i+j].linguisticValue)
        inferenceRules[5*i+j]=inferenceRules[5*i+j].membershipFunction

finalFunction=libfuzzy.Mamdani(
    inferenceRules=inferenceRules,
    outputDomain=[0,1]
    ).method()

def diffFunction(x,y):

    return finalFunction(x,y)-(x+y)/200

visualize.visualize_surface(functionToPlot=diffFunction,domainOfInput1=[0,100],domainOfInput2=[0,100],numberOfPoints1=15,numberOfPoints2=15)

# values of the function depending on differents inputs
for i in range(0,101,25):
    for j in range(0,101,25):
        print(f"Semester 1: {i}, Semester 2: {j}, fuzzy: {finalFunction(i,j)} ")

