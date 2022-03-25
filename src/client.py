import client
import tensorflow as tf
import sys
import random
import numpy as np

client_id = sys.argv[1]

# Load model and data (MobileNetV2, CIFAR-10)
model = tf.keras.applications.MobileNetV2((32, 32, 3), classes=10, weights=None)
model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

def sampling_data():
    num_of_each_dataset = 100
    # num_of_each_dataset = int(config['learning']['data_per_epoch'])
    split_data_index = []
    while len(split_data_index) < num_of_each_dataset:
        item = random.choice(range(x_train.shape[0]))
        if item not in split_data_index:
            split_data_index.append(item)
    new_x_train = np.asarray([x_train[k] for k in split_data_index])
    new_y_train = np.asarray([y_train[k] for k in split_data_index])
    return new_x_train, new_y_train

# Define Flower client
class CifarClient(client.NumPyClient):

  def __init__(self, rnd):
    self.round = rnd

  def get_parameters(self):
    return model.get_weights()

  def fit(self, parameters, config):
    self.round = self.round + 1
    model.set_weights(parameters)
    model.save_weights('local_models/client_'+client_id+'_round'+str(self.round)+'_before.h5')
    x_train, y_train = sampling_data()
    model.fit(x_train, y_train, epochs=5, batch_size=4, verbose=2)
    model.save_weights('local_models/client_'+client_id+'_round'+str(self.round)+'_after.h5')
    return model.get_weights(), len(x_train), {}

  def evaluate(self, parameters, config):
    model.set_weights(parameters)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=2)
    return loss, len(x_test), {"accuracy": accuracy}

# Start Flower client
client.start_numpy_client("localhost:8080", client=CifarClient(0))