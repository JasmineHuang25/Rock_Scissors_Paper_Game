# Rock_Scissors_Paper_Gmae

## Gaol and Purpose


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

### KNN: k-nearest neighbors

## Best Model: CNN


## Web App Deployment using Gradio

https://gradio.app/

(Host it on Streamlit or Hugging Face!!)

## Limitations and Next Steps
Due to the computer power and some technical issues, here are steps I would like to take but can't execute at this moment:
1. Feed more data: More images. Also try images with background removed along with color inverted.
2. More models: Would like to try out other models such as VGG16 or VGG19.
3. Live professional web app: Would love to upgrade my demo web app to a professional one. 

## Applied and Extend

Personalized sign language translator/AI


## Concusion



