#!/usr/bin/env python3
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

from pa_nlp import *
import matplotlib

if __name__ == "__main__":
  os.system("clear")

  parser = optparse.OptionParser(usage="cmd [optons] ..]")
  #parser.add_option("-q", "--quiet", action="store_true", dest="verbose",
                     #default=False, help="")
  (options, args) = parser.parse_args()

  #sometimes it is required.
  matplotlib.use('Agg')
  from pylab import figure, axes, pie, title, show, savefig

  figure(1, figsize=(6, 6))
  ax = axes([0.1, 0.1, 0.8, 0.8])
  labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
  fracs = [15, 30, 45, 10]
  explode = (0, 0.05, 0, 0)
  pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
  savefig('foo.png')

