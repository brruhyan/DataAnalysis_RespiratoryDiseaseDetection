#test
import streamlit as st
import tensorflow as tf
import numpy as np

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('respiratory_trained.h5')
  return model
model=load_model()
st.write("""
# Respiratory Disease Detection"""
)
file=st.file_uploader("Upload Chest X-ray Image",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(150,150)
    image=ImageOps.fit(image_data,size, Image.Resampling.LANCZOS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Normal', 'Viral Pneumonia']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)
