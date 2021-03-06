from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout


# def model_architecture():
def model_architecture_1conv_1max_pool():
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
    model.add(MaxPooling2D(pool_size=2))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.summary()
    return model


# def model_architecture():
def model_architecture_2conv_1max_pool():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.summary()
    return model


# def model_architecture():
def model_architecture_3conv_1max_pool():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(132, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.summary()
    return model


# def model_architecture():
def model_architecture_1conv_1max_pool_dropout():
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=2, padding='same', activation='relu', input_shape=(32, 32, 3)))
    model.add(MaxPooling2D(pool_size=2))

    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(10, activation='softmax'))

    model.summary()
    return model


def model_architecture():
# def model_architecture_alternate_1conv_1max_pool():
    # def model_architecture():
    # build the model object
    model = Sequential()

    # CONV_1: add CONV layer with
    # RELU activation and depth = 32 of kernels (Feature extractor), each kernel of size 3*3
    # padding as same means we the output image size of this layer will be same as Input layer
    model.add(Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
    # Output: 32 * 32 * 32

    # POOL_1: down sample the image to choose the best features
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Output: 14 * 14 * 32

    # CONV_2: here we increase the depth to 64
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    # Output: 14 * 14 * 64

    # POOL_2: more down sampling
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Output: 7 * 7 * 64

    # flatten since too many dimensions, we only want a classification output
    # Flatten layer is introduced after we are done with the Feature extraction
    model.add(Flatten())

    # FC_1: fully connected to get all relevant data
    model.add(Dense(64, activation='relu'))

    # FC_2: output a softmax to squash the matrix into output probabilities for the 10 classes
    model.add(Dense(10, activation='softmax'))

    model.summary()
    return model
