import math
from keras.callbacks import LearningRateScheduler
from datetime import datetime
# from keras.optimizers import adam
from src.core.data_preparation import *
from src.convnet_mnist.model_architectures import model_architecture


def build_model():
    model = model_architecture()
    return model


# Creating the "scheduler" function
def scheduler(epoch):
    # Learning rate = Learning rate * 1/(1 + decay * epoch)
    initial_learning_rate = 0.01
    drop = 0.96  # decay
    epochs_drop = 8
    learning_rate = initial_learning_rate * math.pow(drop, math.floor((1 + epoch) / epochs_drop))
    return learning_rate


def start_training(model, X_train, y_train, X_validation, y_validation):
    # optimizer = adam(lr=0.003, decay=1e-6)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    start = datetime.now()
    model.fit(X_train, y_train,
              validation_data=(X_validation, y_validation),
              batch_size=128,
              epochs=1,
              verbose=1,
              callbacks=[LearningRateScheduler(scheduler, verbose=1)])

    duration = datetime.now() - start
    print("Training completed in time: ", duration)
    model.save("artifacts/model/convnet_mnist/model.h5")
    print("Model saved to disk")


def model_preparation():
    train_features, train_labels, validation_features, validation_labels = data_preparation_mnist()
    model = build_model()
    start_training(model, train_features, train_labels, validation_features, validation_labels)


if __name__ == '__main__':
    model_preparation()

