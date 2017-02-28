import keras
from keras.models import Sequential
model = Sequential()

from keras.layers import Input, Dense
from keras.models import Model
import numpy as np
import random
import ast
import os
# this returns a tensor
# inputs = Input(shape=(784,))

# a layer instance is callable on a tensor, and returns a tensor
# x = Dense(64, activation='relu')(inputs)
# x = Dense(64, activation='relu')(x)
# predictions = Dense(10, activation='softmax')(x)
#
# # this creates a model that includes
# # the Input layer and three Dense layers
# model = Model(input=inputs, output=predictions)
# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
# data = np.transpose(np.random.rand(784,2))
# labels = np.transpose(np.random.rand(10,2))
# model.fit(data, labels)  # starts training
# print(model.input_shape)
# print(model.output_shape)
# x = np.random.rand(1,784)
# print(x.tolist())
from keras.layers import Merge

left_branch = Sequential()
left_branch.add(Dense(2, input_dim=2, init='uniform'))

right_branch = Sequential()
right_branch.add(Dense(4, input_dim=4, init='uniform'))

merged = Merge([left_branch, right_branch], mode='concat')

final_model = Sequential()
final_model.add(merged)
advance_activation = keras.layers.advanced_activations.LeakyReLU(alpha=0.3)
final_model.add(Dense(1, activation=advance_activation, init='uniform'))
final_model.compile(loss='mean_squared_error', optimizer='Adam', metrics=['mean_squared_error'])

model_weights_file_exists = os.path.exists('./model_weights.h5')
if (model_weights_file_exists):
    final_model.load_weights('./model_weights.h5')
else:
    file = open('./data.txt', 'r').read()
    file_list = ast.literal_eval(file)
    left_records = []
    right_records = []
    labels = []
    for records in file_list:
        left_records.append(records[0])
        right_records.append(records[1])
        labels.append(records[2])
    left_data = np.array(left_records)
    right_data = np.array(right_records)
    label_data = np.array(labels)
    final_model.fit([left_data, right_data], label_data, nb_epoch=10000, batch_size=30)
    # final_model.fit(left_data, label_data, nb_epoch=300, batch_size=30)
    final_model.save_weights('./model_weights.h5')

test_data_1 = np.array([3, 30])
test_data_2 = np.array([7.450007952622267, 3281, 0.8575577233670555, 1])
test_data_1.shape = (1, 2)
test_data_2.shape = (1, 4)
# test_data = np.array([3, 37, 7.450007952622267, 3281, 0.8575577233670555, 1])
# test_data.shape = (1,6)
result = final_model.predict([test_data_1, test_data_2])
# result = final_model.predict(test_data)
print(result[0, 0])
print('Complete.')

def generateTrainingData(worker_num, history_num):
    frame = []
    for worker_id in range(worker_num):
        experience = random.uniform(1, 10)
        level = random.randint(0, 3)
        accuracy = random.uniform(0.7, 0.95)
        task_amount_base = int(experience * 400)
        task_amount = 0
        for task_id in range(history_num):
            if (task_amount == 0):
                task_amount = task_amount_base + random.randint(1, 400)
            else:
                task_amount += 1
            task_type = random.randint(0, 4)
            task_base_sla = 10 + task_type * 9
            task_sla = task_base_sla + random.randint(0, 20)
            real_time = task_sla + int(0.2 * random.uniform(-24, -16) + 0.5 * random.uniform(-15, -8) + 0.3 * random.uniform(-7, 0))
            record = [[task_type, task_sla], [experience, task_amount, accuracy, level], real_time]
            frame.append(record)
    print(frame)
    t = np.array(frame)
    file = open('./data.txt', 'w')
    file.write(str(frame))
    file.close()


# generateTrainingData(1, 100)