import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense
from keras.layers import LeakyReLU, BatchNormalization, Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.datasets import cifar10

(X_train_raw, Y_train_raw), (X_test_raw, Y_test_raw) = cifar10.load_data()
X_train = X_train_raw / 255
X_test_all = X_test_raw / 255
X_validation, X_test = np.split(X_test_all, 2)
Y_train = to_categorical(Y_train_raw)
Y_validation, Y_test = np.split(to_categorical(Y_test_raw), 2)

model = Sequential()

model.add(Conv2D(16, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.33))

model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.33))

model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.33))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.33))

model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

history = model.fit(X_train, Y_train,
                    validation_data=(X_validation, Y_validation),
                    epochs=2, batch_size=16)

model.summary()

from keras.models import Model
import matplotlib.pyplot as plt

IMAGE_NUMBER = 31679
example = X_train[IMAGE_NUMBER:IMAGE_NUMBER + 1, :, :, :]

plt.ion()
plt.imshow(example)
plt.show()
input("Enter to continue...")

for layer_number, layer in enumerate(model.layers):
    model = Model(inputs=model.inputs, outputs=layer.output)
    feature_maps = model.predict(example)
    for filter in range(16):
        ax = plt.subplot(4, 4, filter + 1)
        ax.set_title(layer_number, fontsize="15")
        ax.axis('off')
        plt.imshow(feature_maps[0, :, :, filter])
    plt.ion()
    plt.show()
    input("Enter to continue...")
