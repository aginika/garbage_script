#!/usr/bin/env python


import numpy as np

test_num = 50
nb_classes = 2

#put x_ok the OK Images
#put x_ng the NG Images

X_train = x_ok[:-test_num] + x_ng[:-test_num]
X_test = x_ok[-test_num:] + x_ng[-test_num:]

y_ok = np.ones(len(x_ok))
y_ng = np.zeros(len(x_ng))

y_train = y_ok[:-test_num] + y_ng[:-test_num]
y_test  = y_ok[-test_num:] + y_ng[-test_num:]

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

####
#Paste Convolution Here
####

x = Flattern()(x)
x = Dense(1000, activation="relu")(x)
x = Dropout(0.5)(x)
x = Dense(1000, activation="relu")(x)
x = Dropout(0.5)(x)
x = Dense(1000, activation="relu")(x)
x = Dense(50, activation="relu")(x)
x = Dense(nb_classes, activation="softmax")(x)


####Here put model Compile
model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch,
          verbose=1, validation_data=(X_test, Y_test))
