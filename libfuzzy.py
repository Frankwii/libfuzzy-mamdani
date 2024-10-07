class LinguisticVariable:

    def __init__(self,name):
        self.name=name
        self.fuzzySets=[]

    class FuzzySet:
        def __init__(self,linguisticVariable,linguisticValue,membershipFunction,nparams=1):
            self.linguisticVariable=linguisticVariable
            self.linguisticValue=linguisticVariable.name+" is "+linguisticValue
            self.membershipFunction=membershipFunction

    def addFuzzySet(self,linguisticValue,membershipFunction):
        fuzzySet=LinguisticVariable.FuzzySet(
            linguisticVariable=self, linguisticValue=linguisticValue, membershipFunction=membershipFunction
            )
        self.fuzzySets.append(fuzzySet)

    class FuzzyLogic:
        @staticmethod
        def Or(fuzzySet1,fuzzySet2):
            def membershipFunction(x,y):

                return max(fuzzySet1.membershipFunction(x),fuzzySet2.membershipFunction(y))

            fuzzySet=LinguisticVariable.FuzzySet(
                linguisticVariable=LinguisticVariable(
                    name=fuzzySet1.linguisticVariable.name+" or "+fuzzySet2.linguisticVariable.name
                ),
                linguisticValue=fuzzySet1.linguisticValue+" or "+fuzzySet2.linguisticValue,
                membershipFunction=membershipFunction
            )

            return fuzzySet

        @staticmethod
        def And(fuzzySet1,fuzzySet2):
            def membershipFunction(x,y):

                return min(fuzzySet1.membershipFunction(x),fuzzySet2.membershipFunction(y))

            fuzzySet=LinguisticVariable.FuzzySet(
                linguisticVariable=LinguisticVariable(
                    name=fuzzySet1.linguisticVariable.name+" and "+fuzzySet2.linguisticVariable.name
                ),
                linguisticValue=fuzzySet1.linguisticValue+" and "+fuzzySet2.linguisticValue,
                membershipFunction=membershipFunction
            )

            return fuzzySet

        @staticmethod
        def IfThen(fuzzySetOfAntecedent,fuzzySetOfConsequent):
            def membershipFunction(x,y):

                return max(1-fuzzySetOfAntecedent.membershipFunction(x),fuzzySetOfConsequent.membershipFunction(y))


            fuzzySet=LinguisticVariable.FuzzySet(
                linguisticVariable=LinguisticVariable(
                    name="If "+fuzzySetOfAntecedent.linguisticVariable.name+" then "+fuzzySetOfConsequent.linguisticVariable.name
                ),
                linguisticValue="If "+fuzzySetOfAntecedent.linguisticValue+" then "+fuzzySetOfConsequent.linguisticValue,
                membershipFunction=membershipFunction
            )

            return fuzzySet

        @staticmethod
        def IfAndThen(fuzzySetOfAntecedent1,fuzzySetOfAntecedent2,fuzzySetOfConsequent):
            def membershipFunction(x,y,z):

                return max(1-min(fuzzySetOfAntecedent1.membershipFunction(x),fuzzySetOfAntecedent2.membershipFunction(y)),fuzzySetOfConsequent.membershipFunction(y))


            fuzzySet=LinguisticVariable.FuzzySet(
                linguisticVariable=LinguisticVariable(
                    name="If "+fuzzySetOfAntecedent1.linguisticVariable.name+
                    " and "+fuzzySetOfAntecedent2.linguisticVariable.name+" then "+fuzzySetOfConsequent.linguisticVariable.name
                ),
                linguisticValue="If "+fuzzySetOfAntecedent1.linguisticValue+" and "+fuzzySetOfAntecedent2.linguisticValue+" then "+fuzzySetOfConsequent.linguisticValue,
                membershipFunction=membershipFunction
            )

            return fuzzySet


class Mamdani:
    def __init__(self,inferenceRules,outputDomain):
        self.inferenceRules=inferenceRules
        self.outputDomain=outputDomain

    def aggregate(self):
        return lambda x,y,z:max([inferenceRule(x,y,z) for inferenceRule in self.inferenceRules])

    def method(self):
        aggregatedFunction=self.aggregate()

        startOfOutputDomain,endOfOutputDomain=self.outputDomain
        def numerator(x,y):
            fNum=lambda z:aggregatedFunction(x,y,z)*z
            return utils.integrate(fNum,startOfOutputDomain,endOfOutputDomain)

        def denominator(x,y):
            fDenom=lambda z:aggregatedFunction(x,y,z)*z
            return utils.integrate(fDenom,startOfOutputDomain,endOfOutputDomain)

        return lambda x,y:numerator(x,y)/denominator(x,y)

class utils:

    def createTriangularFunction(pointArray):
        leftBasepoint,tipPoint,rightBasepoint = pointArray
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


    def integrate(f,a,b):
        # Integrate a function f over a domain [a,b].
        n=10000
        h=(b-a)/n
        int=0

        for i in range(n):
            int+=(h*f(a+i*h))

        return int
