import os
import numpy as np
import json

dir_data='./dataset'


with open(dir_data+"/label_test.json") as f:
  data_train = json.load(f)

data_train['categories'] = [{'id': 1, 'name': 'Normal'}]

print(data_train.keys())

with open(dir_data+'/test.json', 'w') as f:
    json.dump(data_train, f)

print(data_train)

# 데이터 설정
# data_root='dataset/'
# classes = ('Normal',)
# data = dict(
#     samples_per_gpu=1,
#     workers_per_gpu=0,
#     train=dict(
#       img_prefix=data_root + "train/",
#       classes = classes,
#       ann_file=data_root + "label(polygon)_train.json"
# ),
#     val=dict(
#         img_prefix=data_root + "train/",
#         classes = classes,
#         ann_file=data_root + "label(polygon)_train.json"
# ),
#     test=dict(
#         img_prefix=data_root + "test/",
#         classes = classes,
#         ann_file=data_root + "test.json"
# )
# )