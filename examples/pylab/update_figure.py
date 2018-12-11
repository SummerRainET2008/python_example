try:
  import pylab

  fg = pylab.figure(1)
  fg.clear()
  probs = [1, 2, 3, 4]
  pylab.plot(probs, label="log likelihood")
  pylab.legend()
  pylab.grid()
  pylab.savefig("loglikelihood.pdf")
except:
  print("can not import pylab")