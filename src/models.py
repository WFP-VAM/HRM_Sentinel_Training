from tensorflow.python.keras.layers import Input, Conv2D, MaxPooling2D, Dropout, Activation, Dense, Flatten, BatchNormalization
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.optimizers import Adam


def netowrk(size):
    inputs = Input((size, size, 3))
    conv1 = Conv2D(8, (6, 6), activation='relu', padding='same', name='conv1')(inputs)
    conv1 = BatchNormalization(axis=3)(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(conv1)
    # pool1 = Dropout(0.25)(pool1)

    conv2 = Conv2D(16, (6, 6), activation='relu', padding='same', name='conv2')(pool1)
    conv2 = BatchNormalization(axis=3)(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(conv2)
    # pool2 = Dropout(0.25)(pool2)

    conv3 = Conv2D(32, (6, 6), activation='relu', padding='same', name='conv3')(pool2)
    conv3 = BatchNormalization(axis=3)(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(conv3)
    # pool3 = Dropout(0.25)(pool3)

    dense1 = Dense(32)(pool3)
    dense1 = Activation('relu')(dense1)
    dense1 = Dropout(0.25)(dense1)

    out = Flatten(name='flatten')(dense1)
    out = Dense(3)(out)
    out = Activation('softmax')(out)

    model = Model(inputs=[inputs], outputs=[out])

    # compile and train ----------------------------------------------
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=0.000001, decay=0.00000001),
                  metrics=['accuracy'])

    return model