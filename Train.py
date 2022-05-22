from convert_data_to_array import conv_images_to_array_train
import numpy as np
from keras import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout
import os

def train(x_values):
    xtr = x_values.reshape(x_values.shape[0],-1).astype('float32')/255
    ytr = np.loadtxt("lables.txt")
    xtr = xtr.reshape(1894, 28, 28, 1)
    model = Sequential()
    model.add(Conv2D(16, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
    model.add(Conv2D(32, kernel_size=3, activation='relu'))
    model.add(Conv2D(64, kernel_size=3, activation='relu'))
    model.add(Conv2D(128, kernel_size=3, activation='relu'))
    model.add(Flatten())
    model.add(Dense(6, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    model.fit(xtr, ytr, batch_size=30, epochs=10, shuffle=True,validation_split=0.3)
    return model

def save_model(model):
    save_dir = os.getcwd()
    model_name = 'keras_model.h5'
    model_path = os.path.join(save_dir, model_name)
    model.save(model_path)
    print('Saved trained model at %s ' % model_path)

def main():
    """Main function"""
    x_values = conv_images_to_array_train()
    model = train(x_values)
    save_model(model)

if __name__ == '__main__':
    main()

