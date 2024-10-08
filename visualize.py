import matplotlib.pyplot
import numpy

def visualize_surface(mamdaniResult,domainOfInput1,domainOfInput2,numberOfPoints1=5,numberOfPoints2=5):

  domainOfInput1Start,domainOfInput1End=domainOfInput1
  step1=(domainOfInput1End-domainOfInput1Start)/numberOfPoints1

  domainOfInput2Start,domainOfInput2End=domainOfInput2
  step2=(domainOfInput2End-domainOfInput2Start)/numberOfPoints2

  X=numpy.arange(domainOfInput1Start,domainOfInput1End,step1)
  Y=numpy.arange(domainOfInput2Start,domainOfInput2End,step2)
  X,Y=numpy.meshgrid(X,Y)

  Z = numpy.zeros_like(X)
  for i in range(X.shape[0]):
      for j in range(X.shape[1]):
          Z[i, j] = mamdaniResult(X[i, j], Y[i, j])

  figure = matplotlib.pyplot.figure()
  surface = figure.add_subplot(111, projection='3d')
  surface.plot_surface(X, Y, Z, cmap='viridis')

  matplotlib.pyplot.show()
