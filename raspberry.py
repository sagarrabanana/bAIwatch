
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras import layers, callbacks, optimizers
from tensorflow.keras.models import Sequential, save_model, load_model
import numpy as np
print(tf.__version__)


import time
import datetime
import urllib.request
import socket
socket.setdefaulttimeout(30)

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)



model = load_model(
    'path to he ".h5" file',
    custom_objects=None,
    compile=True
)

GPIO.setup(21, GPIO.OUT)
for i in range(3): #lets me know that the script is runing
    GPIO.output(21,True)
    time.sleep(0.02)
    GPIO.output(21,False)
    time.sleep(0.02)
GPIO.cleanup()


while True:
  if (int(datetime.datetime.now().strftime("%H"))>5 and int(datetime.datetime.now().strftime("%H"))<17): #todo este jaleo para quedarme con la hora en formato integer del datatime...
  # setting filename and image URL
  try:
    print('dentro del try')
    name=str(datetime.datetime.now())
    filename = '/content/gdrive/MyDrive/Dataset/'+name+'.jpg' #here goes the path to your dataset folder on your google drive
    image_url = "http://212.8.113.121:8081/jpg/1/image.jpg"
    urllib.request.urlretrieve(image_url, filename)
    print('imagen '+name+' descargada.')

    #####
    img = image.load_img(filename, target_size=(150, 150))
    img = np.expand_dims(img, axis=0)
    result_c=model.predict_classes(img)
    print(result_c)
    if result_c==2:
      print('Buenas')
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(21, GPIO.OUT)
      for i in range(3):
        GPIO.output(21,True)
        time.sleep(0.02)
        GPIO.output(21,False)
        time.sleep(0.02)
      GPIO.cleanup()
    elif result_c==1:
      print('Descarte')
    elif result_c==0:
      print('Malas')
    result=model.predict(img)
    print(result)
    print('esperamos...')
    time.sleep(30)
  except:
    print('hay algun problemilla, esperamos medio minuto y reintentamos...')
    time.sleep(30)
  else:
    time sleep(60)
