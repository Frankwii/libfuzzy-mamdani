import matplotlib.pyplot as plot
import numpy
from matplotlib import cm

def visualize_surface(functionToPlot,domainOfInput1,domainOfInput2,numberOfPoints1=10,numberOfPoints2=10):

  domainOfInput1Start,domainOfInput1End=domainOfInput1
  domainOfInput2Start,domainOfInput2End=domainOfInput2

  X=numpy.linspace(domainOfInput1Start,domainOfInput1End,num=numberOfPoints1)
  Y=numpy.linspace(domainOfInput2Start,domainOfInput2End,num=numberOfPoints2)
  X,Y=numpy.meshgrid(X,Y)

  Z = numpy.zeros_like(X)
  for i in range(X.shape[0]):
      for j in range(X.shape[1]):
          Z[i, j] = functionToPlot(X[i, j], Y[i, j])

    # Plot the surface
  fig, ax = plot.subplots(subplot_kw={"projection": "3d"})
  ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

  plot.show()

  # figure = matplotlib.pyplot.figure()
  # surface = figure.add_subplot(111, projection='3d')
  # surface.plot_surface(X, Y, Z, cmap='viridis')

  # plot.show()
