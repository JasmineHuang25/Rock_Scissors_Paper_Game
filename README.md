# Rock_Scissors_Paper_Gmae

## Gaol and Purpose

This is the final project to showcase everything I've learned within 15 weeks joining the Data Science Bootcamp at Flatiron School.  Thus, I would like to 
demonstrate my capabilities and skills that I can condut a project from A to Z solely.  In my previous projects and blogs, I have done several business
related topics, such as [comapny bankruptcy prediction](https://github.com/JasmineHuang25/Blog4_bankruptcy_prediction) or [vehicle damage prediction](https://github.com/JasmineHuang25/Phase3_project-Vehicle-damage-prediction-for-auto-insurance-use).  I kept asking myself what would be better?  Should I 
choose another business related topic or do something else as my capstone project?
It is definitely not easy to finally graduate from the bootcamp.  However, it is also one of the most wonderful and meaningful journey that I have ever taken.
Before stepping into the real world, this might be the best timing and opportunity for me to do a FUN project.  And this will finalize my journey to Data Science
with a fun and also professional ending.
Finally I camp up with this idea of my capstone project.  Fist of all, I will train and find the best model to identify "rock", "scissors", and "paper" using
Convolutional Neural Network algorithm.  After my model is trained, it will generate a prediction taking in a new input/image.  And the result of its prediction
will be the gamer to play the classic rock-scissors-paper game with a computer.  Finally, I will need to deploy a web app allows the gamer to join game via a 
webcam for signing their moves.


## Dataset and EDA
#### First dataset:
[Resource](https://laurencemoroney.com/datasets.html#rock-paper-scissors-dataset)

This dataset contains a total of 2892 images.
 - Train set: 2520 images (840 in each class)
 - Test set: 372 images (214 in each class)
 - Validation set: 33 images
All images are RGB images of 300 pixels wide by 300 pixels high in .png format. The images are separated in three sub-folders named 'rock', 'paper' and 'scissors'
according to their respective class.

 ![Alt Image text](png-------/dataset1_ex)


#### Second dataset:
[Resource](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)

The dataset contains a total of 2188 images corresponding to the 'Rock' (726 images), 'Paper' (710 images) and 'Scissors' (752 images) hand gestures of the
Rock-Paper-Scissors game. All image are taken on a green background with relatively consistent ligithing and white balance.
All images are RGB images of 300 pixels wide by 200 pixels high in .png format. The images are separated in three sub-folders named 'rock', 'paper' and 'scissors'
according to their respective class.

![Alt Image text](png-------/dataset2_ex)

#### Third and final dataset:
[Resource to gather your own images as dataset](https://github.com/CircuitDigest/Rock-Paper-Scissors-with-Pi)

My web app will be capture the image from the webcam as the input to my model's prediciton.  It will be better to train my model with the real images captured by
a webcam.  Therefore, I have created a total of 17550 images captured by a webcam as my final dataset.
All images are RGB images of 252 pixels wide by 188 pixels high in .jpg format. The images are separated in three sub-folders named 'rock', 'paper' and 'scissors'
according to their respective class.
 - Train set: 13500 images (4500 in each class)
 - Test set: 4350 images (1450 in each class)
 - 
![Alt Image text](png-------/dataset3_ex)

In order to get a better result for the model and prediction, I have trained the model with color-inverted images and will also invert color for the new images
for prediction. 

![Alt Image text](png-------/dataset3_ex_invert)

This the input image captured from the web app

![Alt Image text](png-------/webapp_input_img)


## Models

### CNN: Convolutional Neural Network

#### Baseline model

![Alt Image text](png-------/basline_model_summary)

### Best Model

![Alt Image text](png-------/best_model_summary)

## Web App Deployment using Gradio

[Resource](https://gradio.app/)

(Host it on Streamlit or Hugging Face!!)

## Limitations and Next Steps
Due to the computer power and some technical issues, here are steps I would like to take but can't execute at this moment:
1. Feed more data: More images. Also try images with background removed along with color inverted.
2. More models: Would like to try out other models such as VGG16 or VGG19.
3. Live professional web app: Would love to upgrade my demo web app to a professional one. 

## Applied and Extend

Personalized sign language translator/AI


## Concusion



