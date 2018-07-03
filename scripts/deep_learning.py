import copy
import sys

import keras

import numpy as np

# Add local setting
sys.path.append('/home/forno/ws/prog/location_predict')
import location_predict

org_prefectures_data   = np.genfromtxt('../prefectures_onlydata.csv',   delimiter = ',')
org_prefectures_vector = np.genfromtxt('../prefectures_onlyvector.csv', delimiter = ',')
org_dicomo_data        = np.genfromtxt('../dicomo_onlydata.csv',        delimiter = ',')
org_human_vector       = np.genfromtxt('../human_onlyvector.csv',       delimiter = ',')

next_prefectures_data   = org_prefectures_data[0:1]
next_dicomo_data        = org_dicomo_data     [0:1]
next_human_data         = org_human_vector    [0:1]

org_prefectures_data   = np.delete(org_prefectures_data,    0, 0)
org_dicomo_data        = np.delete(org_dicomo_data,         0, 0)
org_human_data         = np.delete(org_human_vector,        0, 0) # correct variable name
org_prefectures_vector = np.delete(org_prefectures_vector, -1, 0)
org_human_vector       = np.delete(org_human_vector,       -1, 0) # correct over assigin

# make train data
prefectures_data   = org_prefectures_data  [1:]
dicomo_data        = org_dicomo_data       [1:]
human_data         = org_human_vector      [1:]
prefectures_vector = org_prefectures_vector[1:]
human_vector       = org_human_vector      [1:]

if len(sys.argv) == 1 or sys.argv[1] != '-t':
  model = keras.models.load_model('model')
else:
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

prefectures_test_data = org_prefectures_data  [0:1]
dicomo_test_data      = org_dicomo_data       [0:1]
human_test_data       = org_human_data        [0:1]
prefectures_answer    = org_prefectures_vector[0:1]
human_answer          = org_human_vector      [0:1]

print(location_predict.test(model, prefectures_test_data, dicomo_test_data, human_test_data, prefectures_answer, human_answer))

predict_values = model.predict([next_prefectures_data, next_dicomo_data, next_human_data])

pp = predict_values[0]
ph = predict_values[1]

for pip, pih in zip(pp, ph):
  print(pip, pih)
