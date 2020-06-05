from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.optimizers import SGD


def create_model():
	model = Sequential()
 
    # Convolutional stack
	model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(rate=0.2))
 
	model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))

	model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(rate=0.2))
 
    # Fully-connected stage
	model.add(Flatten())
	model.add(Dense(units=128, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dropout(0.5))
	model.add(Dense(units=1, activation='sigmoid'))
	
    # Model compiling
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
 
	return model
