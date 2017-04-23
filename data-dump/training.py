import csv
import cv2
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

lines = []
with open('./lab02/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)


images = []
measurements = []


for line in lines:
    source_path = line[0]
    filename = source_path.split('/')[-1]
    current_path = './lab02/IMG/' + filename
    
    image = cv2.imread(current_path)
    images.append(image) 
    images.append(cv2.flip(image,1))
    
    measurement = float(line[3])
    measurements.append(measurement)
    measurements.append((-1)*measurement)


X_train = np.array(images)
y_train = np.array(measurements)

print(X_train.shape)





from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.layers import Cropping2D, Lambda
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.core import Dropout



model = Sequential()
model.add( Lambda(lambda x: (x/255.) -0.5, input_shape=(160,320,3)) )
model.add( Cropping2D(cropping=((50,20), (0,0)), input_shape=(160,320,3)) )
# Shape=(90,320,3)
model.add( Convolution2D(24, (5,5), strides=(2,2), activation='relu') )
# Shape=(43,158,24)
model.add( Convolution2D(36, (5,5), strides=(2,2), activation='relu') )
# Shape=(20,77,36)
model.add( Convolution2D(48, (5,5), strides=(2,2), activation='relu') )
# Shape=(8,37,48)
model.add( Convolution2D(64, (3,3), strides=(2,2), activation='relu') )
# Shape=(3,18,64)
model.add( Convolution2D(64, (3,3), strides=(2,2), activation='relu') )
# Shape=(1,8,64)
model.add( Flatten() )
model.add( Dropout(0.1) )
model.add( Dense(600) )
model.add( Dense(100) )
model.add( Dense(50) )
model.add( Dense(10) )
model.add( Dense(1) )

model.compile(loss='mse', optimizer='adam')
model.load_weights('model_A.h5')
model.fit(X_train, y_train, validation_split=0.3, shuffle=True, epochs=15)
model.save('model_A.h5')

