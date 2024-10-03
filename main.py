import libfuzzy


### Input variables
gradesOfSemester1=libfuzzy.LinguisticVariable(variableName="Semester-1")
gradesOfSemester2=libfuzzy.LinguisticVariable(variableName="Semester-2")

# Populate the variables with the corresponding membership functions and names
triangleFunctionGenerator=libfuzzy.utils.createTriangularFunction
tags=["VL","L","A","H","VH"]
triangleMarks=[[0,0,25],[0,25,50],[25,50,75],[50,75,100],[75,100,100]]

for i in range(5):
    gradesOfSemester1.addFuzzySet(
        libfuzzy.FuzzySet(linguisticValue=tags[i],
                          membershipFunction=triangleFunctionGenerator(triangleMarks[i][0],triangleMarks[i][1],triangleMarks[i][2]))
    )
    gradesOfSemester2.addFuzzySet(
        libfuzzy.FuzzySet(linguisticValue=tags[i],
                          membershipFunction=triangleFunctionGenerator(triangleMarks[i][0],triangleMarks[i][1],triangleMarks[i][2]))
    )

### Output variable
finalPerformance=libfuzzy.LinguisticVariable(variableName="Performance")

tags=["VU","U","A","S","VS"]
triangleMarks=[[0,0,0.25],[0,0.25,0.50],[0.25,0.50,0.75],[0.50,0.75,1],[0.75,1,1]]


### Inference rules
