#!/usr/bin/env python2.7
#coding: utf-8

import pylab
from pylab import *
from optparse import OptionParser

# make a square figure and axes
def draw1():
  #figure(1, figsize=(6,4))
  ax = axes([0.1, 0.1, 0.8, 0.8])

  labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
  fracs = [15,30,45, 10]

  explode=(0, 0.05, 0, 0)
  pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
  title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

  savefig('foo1.pdf')
  show() # actually, don't show, just save to foo.png

def draw2():
  pylab.plot(range(1, 10), label = "number of weak learners")
  pylab.legend()
  pylab.grid()
  #savefig('foo2.pdf')
  pylab.show()

draw2()
