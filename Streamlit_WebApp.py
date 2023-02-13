import streamlit as st

from tensorflow import keras
import numpy as np
import random

import matplotlib.pyplot as plt
import seaborn as sns

import os
import cv2
from keras.preprocessing import image
from keras import utils
from PIL import Image

# Title
st.write('<h2 style="text-align:center; font-family:sans-serif; color:Black; font-size: 36px;">Rock-Scissors-Paper Game!</h2', unsafe_allow_html=True)

sub_title = '<p style="text-align:center; font-family:sans-serif; color:Blue; font-size: 18px;">Play Rock-Scissors-Paper game with a trained machine</p>'
st.markdown(sub_title, unsafe_allow_html=True)

st.image('./Data_and_img/sn-rockpaper.jpg', use_column_width='always')

model = keras.models.load_model('./OtherNotebook_and_Files/Saved_model.h5')

camera_label = '<p style="text-align:center; font-family:sans-serif; color:Blue; font-size: 18px;">Please make your move(hand gesture) CLOSE and CLEAR!</p>'
st.markdown(camera_label, unsafe_allow_html=True)
inp = st.camera_input('Please make your hand gesture CLOSE and CLEAR!', label_visibility="collapsed")
c1, c2, c3 = st.columns(3)

if inp is not None:
    image = Image.open(inp).convert('RGB')
    np_img = np.asarray(image)
    reshaped_image = cv2.resize(np_img,(150, 150))
    image_i = cv2.bitwise_not(reshaped_image)    #invert color
    
    c1_header = '<p style="text-align:left; font-family:sans-serif; color:Black; font-size: 20px;">Your Move</p>'
    c1.markdown(c1_header, unsafe_allow_html=True)
    c1.image(image_i)
    
        
    cap_img = image_i.reshape((-1, 150, 150, 3))
    prediction = model.predict(cap_img, batch_size=10)
    
    for i in prediction:
        if i[0] == 1:
            label = "Paper"
        elif i[1] == 1:
            label = "Rock"
        else:
            label = "Scissors"
    
    #   Being in Rock-Scissors-Paper game
    choices = ['Rock', 'Paper', 'Scissors']
    user_move = label
    computer_move = random.choice(choices)
    guess_dict = {'Rock': 0, 'Paper': 1, 'Scissors':2}
    guess_idx = guess_dict.get(user_move, 3)
    computer_idx = guess_dict.get(computer_move)
    result_matrix = [[0,2,1], [1,0,2], [2,1,0]]
    result_idx = result_matrix[guess_idx][computer_idx]
    result_messages = ['It is a tie', 'You win!!! Congrats!', 'Sorry, you lose :(']
    result = result_messages[result_idx]
    predict_text = f"The model recognizes your move as {user_move}."
    
  
    if computer_move == 'Rock':
        img_path = './Data_and_img/ROCK.png'
        cp_img = Image.open(img_path)
        computer_move_img = np.asarray(cp_img)
    elif computer_move == 'Paper':
        img_path = './Data_and_img/PAPER.png'
        cp_img = Image.open(img_path)
        computer_move_img = np.asarray(cp_img)
    else:
        img_path = './Data_and_img/SCISSORS.png'
        cp_img = Image.open(img_path)
        computer_move_img = np.asarray(cp_img)

    
    c2_header = '<p style="text-align:center; font-family:sans-serif; color:Black; font-size: 20px;">Computers Move</p>'
    c2.markdown(c2_header, unsafe_allow_html=True)
    c2.image(computer_move_img)
    

    # c3.header(':red[Result]')
    c3_header = '<p style="text-align:center; font-family:sans-serif; color:Red; font-size: 22px;">Result</p>'
    c3.markdown(c3_header, unsafe_allow_html=True)
    c3.write(predict_text)
    c3.write(result)
    


