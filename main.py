import libfuzzy

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
        # inferenceRules[5*i+j]=libfuzzy.Logic.fuzzyIfAndThen(
        #     gradesOfSemester1.fuzzySets[i].membershipFunction,
        #     gradesOfSemester2.fuzzySets[j].membershipFunction,
        #     finalPerformance.fuzzySets[(i+j)//2].membershipFunction
        # )
        inferenceRules[5*i+j]=\
        libfuzzy.LinguisticVariable.FuzzyLogic.IfAndThen(
            gradesOfSemester1.fuzzySets[i],
            gradesOfSemester2.fuzzySets[j],
            finalPerformance.fuzzySets[(i+j)//2]
        ).membershipFunction

def madmaniMethod(inputLinguisticVariable1,inputLinguisticVariable2,outputLinguisticVariable,inferenceRules,outputDomain):
    # Suppose inputLinguisticVariable1.membershipFunction is a function of a
    #         inputLinguisticVariable2.membershipFunction is a function of b
    #     and outputLinguisticVariable.membershipFunction is a function of x

    # ruleOutputs=[inferenceRule(inputLinguisticVariable1,inputLinguisticVariable2,outputLinguisticVariable) for inferenceRule in inferenceRules]

    # This is a function of (a,b,x)
    aggregatedFunction=lambda a,b,x: max([f(a,b,x) for f in inferenceRules])

    def numeratorFunction(a,b):

        return lambda x: x*aggregatedFunction(a,b,x)

    def denominatorFunction(a,b):

        return lambda x: aggregatedFunction(a,b,x)

    domain_a,domain_b=outputDomain

    return lambda a,b:(libfuzzy.utils.integrate(numeratorFunction(a,b),domain_a,domain_b))/(libfuzzy.utils.integrate(denominatorFunction(a,b),domain_a,domain_b))

currentMamdani=libfuzzy.Mamdani(
    inferenceRules=inferenceRules,
    outputDomain=[0,1]
    )

finalFunction=currentMamdani.method()

print(finalFunction(50,50))