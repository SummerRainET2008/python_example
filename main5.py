#!/usr/bin/env python3
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

import pa_nlp.common as nlp
import collections
import optparse
import os
import math
import tensorflow as tf

def main():
  sess = tf.Session()

  # data = tf.constant([1, 2, 3], tf.float32)
  # mean, var = tf.nn.moments(data, [0])
  # new_data = (data - mean) / tf.sqrt(var + 1e-8)
  # print(sess.run([mean, var, new_data]))

  data = tf.constant([[[1, 2, 3, 1], [2, 2.5, 3, 2], [3, 3.5, 4, 2]],
                      # [[3, 0, 6], [4, 5,   7], [5, 6, 1]],
                      [[2, 1, 2, 2], [3, 3,  3, 5], [4, 4, 4, 7]],
                      ]
                     , tf.float32)
  print(data.shape)
  # data = tf.transpose(data)

  mean_ts, var_ts = tf.nn.moments(data, [0, 1])
  print(sess.run([mean_ts, var_ts]))
  new_data = (data - mean_ts) / tf.sqrt(var_ts + 1e-8)
  print(sess.run([new_data]))

if __name__ == "__main__":
  parser = optparse.OptionParser(usage="cmd [optons] ..]")
  #parser.add_option("-q", "--quiet", action="store_true", dest="verbose",
  #default=False, help="")
  (options, args) = parser.parse_args()

  main()

