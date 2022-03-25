import tensorflow as tf
import numpy as np

# Load model and data (MobileNetV2, CIFAR-10)
model = tf.keras.applications.MobileNetV2((32, 32, 3), classes=10, weights=None)
model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

for r in range(1,51):
    model.load_weights('global_models/round_%d.h5'%r)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=2)
    print('ROUND',r,' : ',accuracy)
