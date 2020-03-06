def pr(arr):
  for R in arr:
    for C in R:
          print("{}".format(' ' if int(C*10) == 0 else int(C*10)), end='')
    print("")

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
