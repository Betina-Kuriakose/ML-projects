import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Flatten, Dense
import cv2
#opencs.python
virat_images=[]
for i in range(1,11):
    filepath=f'images1/virat{i}.jpg'
    img=cv2.imread(filepath)
    if img is not None:
        img=cv2.resize(img,(150,150))
        img=img.astype('float32')/255.0
        virat_images.append(img)
    else:
        print(f'Error loading image:{filepath}')
virat_images=np.array(virat_images)

model=Sequential([
    Flatten(input_shape=(150,150,3)),
    Dense(128, activation="relu"),
    Dense(1,activation="sigmoid")
])



model.compile(optimizer ='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
#training
labels=np.ones((len(virat_images),))
model.fit(virat_images,labels,epochs=10)

#processing
test_image=cv2.imread(f'images1/test1.jpg')
if test_image is not None:
    test_image=cv2.resize(test_image,(150,150))
    test_image=test_image.astype("float32")/255.0
    test_image=np.expand_dims(test_image,axis=0)
#prediction part(of the test image)
    prediction=model.predict(test_image)
    if prediction[0] >=0.5:
        print("Virat kholi")
    else:
        print("other Player")
else:
    print("error loading test image")