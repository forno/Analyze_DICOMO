import copy
import sys

import keras

import numpy as np

# Add local setting
sys.path.append('/home/forno/ws/prog/location_predict')
import location_predict

if len(sys.argv) == 1 or sys.argv[1] != '-t':
  model = keras.models.load_model('model')
else:
  prefectures_data   = np.genfromtxt('../prefectures_onlydata.csv',   delimiter = ',')
  prefectures_vector = np.genfromtxt('../prefectures_onlyvector.csv', delimiter = ',')
  dicomo_data        = np.genfromtxt('../dicomo_onlydata.csv',        delimiter = ',')
  human_vector       = np.genfromtxt('../human_onlyvector.csv',       delimiter = ',')

  prefectures_data   = np.delete(prefectures_data,    0, 0)
  dicomo_data        = np.delete(dicomo_data,         0, 0)
  human_data         = np.delete(human_vector,        0, 0) # correct variable name
  prefectures_vector = np.delete(prefectures_vector, -1, 0)
  human_vector       = np.delete(human_vector,       -1, 0) # correct over assigin

  print(int(dicomo_data[0].size / 2)) # feature are 2 kinds in a year
  print(prefectures_vector[0].size)   # prefectures are 48 kinds
  print(dicomo_data[0].size)          # numeric_dim is directory size
  print(human_vector[0].size)         # human_vector size is dimention

  model = location_predict.create_model(
    time_deep    = int(dicomo_data[0].size / 2), # feature are 2 kinds in a year
    locale_kinds = prefectures_vector[0].size,   # prefectures are 48 kinds
    numeric_dim  = dicomo_data[0].size,          # numeric_dim is directory size
    n_hot_dim    = human_vector[0].size)         # human_vector size is dimention

  location_predict.train(model, prefectures_data, dicomo_data, human_data, prefectures_vector, human_vector)
  model.save('model')

location_predict.test(model, prefectures_data, dicomo_data, human_data, prefectures_vector, human_vector)
