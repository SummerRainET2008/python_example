try:
  import pylab
  data = [1, 2, 3, 4]
  pylab.plot(data, label = "number of weak learners")
  pylab.legend()
  pylab.grid()
  pylab.show()
except:
  pass