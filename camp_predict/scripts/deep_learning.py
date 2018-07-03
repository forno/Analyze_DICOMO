import copy
import sys

import keras

import numpy as np

# Add local setting
sys.path.append('/home/forno/ws/prog/location_predict')
import location_predict

org_prefectures_data   = np.genfromtxt('../camp_timethink_data.csv',  delimiter = ',')
org_prefectures_vector = np.genfromtxt('../prefectures_vector.csv',   delimiter = ',')
org_camp_data          = np.genfromtxt('../camp_additional_data.csv', delimiter = ',')

next_prefectures_data   = org_prefectures_data[0:1]
next_camp_data          = org_camp_data       [0:1]

org_prefectures_data   = np.delete(org_prefectures_data,    0, 0)
org_camp_data          = np.delete(org_camp_data,           0, 0)
org_prefectures_vector = np.delete(org_prefectures_vector, -1, 0)

# make train data
prefectures_data   = org_prefectures_data  #[1:]
camp_data          = org_camp_data         #[1:]
prefectures_vector = org_prefectures_vector#[1:]

if len(sys.argv) == 1 or sys.argv[1] != '-t':
  model = keras.models.load_model('model')
else:
  print(3)                          # LSTM deep 3 years
  print(prefectures_vector[0].size) # prefectures are 48 kinds
  print(camp_data[0].size)          # numeric_dim is directory size

  model = location_predict.create_model_light(
    time_deep    = 3,                          # feature are 2 kinds in a year
    locale_kinds = prefectures_vector[0].size, # prefectures are 48 kinds
    numeric_dim  = camp_data[0].size)          # numeric_dim is directory size

  location_predict.train_light(model, prefectures_data, camp_data, prefectures_vector)
  model.save('model')

prefectures_test_data = org_prefectures_data  [0:1]
camp_test_data        = org_camp_data         [0:1]
prefectures_answer    = org_prefectures_vector[0:1]

print(location_predict.test_light(model, prefectures_test_data, camp_test_data, prefectures_answer))

predict_values = model.predict([next_prefectures_data, next_camp_data])


for pv in predict_values:
  print(pv)
