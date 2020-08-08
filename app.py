from flask import render_template, jsonify, Flask, redirect, url_for, request
import random
import os
import numpy as np
from keras.applications.mobilenet import MobileNet 
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input, decode_predictions
from keras.models import model_from_json
import keras
from keras import backend as K

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

app = Flask(__name__)

SKIN_CLASSES = {
  0: 'Actinic Keratoses (Solar Keratoses) or intraepithelial Carcinoma (Bowen’s disease)', #Viêm giác mạc
  1: 'Basal Cell Carcinoma', # Ung thư gia
  2: 'Benign Keratosis',  #Viêm giac mạc bã nhờn
  3: 'Dermatofibroma', # Viêm gia cơ địa
  4: 'Melanoma',      # Khối u ác tính
  5: 'Melanocytic Nevi',
  6: 'Vascular skin lesion' # Tổn thương mạch máu ở da
}

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        path='static/data/'+f.filename
        f.save(path)
        print('f',f)
        j_file = open('modelnew.json', 'r')
        loaded_json_model = j_file.read()
        j_file.close()
        model = model_from_json(loaded_json_model)
        model.load_weights('modelnew.h5')
        img1 = image.load_img(f, target_size=(224,224))
        img1 = np.array(img1)
        img1 = img1.reshape((1,224,224,3))
        img1 = img1/255
        prediction = model.predict(img1)
        pred = np.argmax(prediction)
        disease = SKIN_CLASSES[pred]
        accuracy = prediction[0][pred]
        K.clear_session()
    return render_template('uploaded.html', title='Success', predictions=disease, acc=accuracy*100, img_file=f.filename)

if __name__ == "__main__":
    app.run(debug=True)