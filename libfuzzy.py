class FuzzySet:
    def __init__(self,linguisticValue,membershipFunction):
        self.linguisticValue=linguisticValue
        self.membershipFunction=membershipFunction

class LinguisticVariable:

    def __init__(self,variableName):
        self.variableName=variableName
        self.fuzzySets=[]

    def addFuzzySet(self,fuzzySet: FuzzySet):
        self.fuzzySets.append(fuzzySet)

class Logic:

    def fuzzyOr(membershipFunction1,membershipFunction2):

        return lambda x,y:min(membershipFunction1(x),membershipFunction2(y))

    def fuzzyAnd(membershipFunction1,membershipFunction2):

        return lambda x,y:max(membershipFunction1(x),membershipFunction2(y))

    def fuzzyNot(membershipFunction):

        return lambda x:1-membershipFunction(x)

    def fuzzyImplication(antecedentMF,consequentMF):

        return Logic.fuzzyOr(Logic.fuzzyNot(antecedentMF),consequentMF)

    def aggregate_madmani(funcArray):

        return lambda x:max([f(x) for f in funcArray])

def madmaniMethod(inputLinguisticVariable1,inputLinguisticVariable2,outputLinguisticVariable,inferenceRules):
    # Suppose inputLinguisticVariable1.membershipFunction is a function of a
    #         inputLinguisticVariable2.membershipFunction is a function of b
    #     and outputLinguisticVariable.membershipFunction is a function of x

    ruleOutputs=[inferenceRule(inputLinguisticVariable1,inputLinguisticVariable2,outputLinguisticVariable) for inferenceRule in inferenceRules]

    # This is a function of ((a,b),x)
    aggregatedFunction=Logic.aggregate_madmani(ruleOutputs)

    pass

class utils:

    def createTriangularFunction(leftBasepoint,tipPoint,rightBasepoint):
        def triangularFunction(x):
            outputValue=0

            if (leftBasepoint<x<tipPoint):
                outputValue=(x-leftBasepoint)/(tipPoint-leftBasepoint)
            elif (x==tipPoint):
                outputValue=1
            elif (tipPoint<x<rightBasepoint):
                outputValue=(rightBasepoint-x)/(rightBasepoint-tipPoint)

            return outputValue
        return triangularFunction
