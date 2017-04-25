#Behavioral Cloning Project

The goals / steps of this project are the following:
Use the simulator to collect data of good driving behavior
Build, a convolution neural network in Keras that predicts steering angles from images
Train and validate the model with a training and validation set
Test that the model successfully drives around track one without leaving the road
Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/architecture.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
###Files Submitted & Code Quality

####1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
**model.py** containing the script to create and train the model
**drive.py** for driving the car in autonomous mode
**model.h5** containing a trained convolution neural network 
**writeup_project03.md** for summarizing the results

####2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

####3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

###Model Architecture and Training Strategy

####1. Model Architecture

My model consists of a convolution neural network with *three* 5x5 filter sizes and *two* 2x2 filter sized and depths between 24 and 64 (**lines 55-63**).

The data is normalized in the model using a Keras lambda layer (code **line 52**). 

####2. Reduction of Ooverfitting

The model contains dropout layers in order to reduce overfitting (model.py line 66). 

The model was trained and validated on different data sets to ensure that the model was not overfitting **(code line 73-76)**. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Tuning of Model Parameters

The model used an Adam optimizer, so the learning rate was not tuned manually **(model.py line 73)**.

####4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I essentially created **four sets**:

  1. Two normal labs around the track ("counter clock-wise"),
  2. two labs ("clock-wise"),
  3. one lab with several recovery situations,
  4. one set with several situations avoiding entering the pit lane right after the bridge.



For details about how I created the training data, see the next section. 

###Model Architecture and Training Strategy

####1. Solution Design Approach

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

The final step was to run the simulator to see how well the car was driving around track one. 

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

####2. Final Model Architecture

The final model architecture **(model.py lines 51-71)** consisted of a convolution neural network with the following layers and layer sizes:

![alt text][image1]

*Legend:*

  * conv5-n: Convolutional layer of depth **n** and filter size 5,
  * conv3-n: Convolutional layer of depth **n** and filter size 3,
  * fc**k**: fully connected layer of width **k**.
  
  
####3. Creation of the Training Set & Training Process

In order to teach the network good driving behavious, I have created two data sets:
  1. Two labs of center lane driving around track 1.
  2. Two labs of center lane driving into the opposite direction.
  3. Approx. 1:30 minutes of recovery drinving, etc. allowing the car to take a road mitigating trajectory and recovering before leaving the road.

Although the car behaved well after training the neural net with these two sets, there was one particular siutation just after leaving the bridge:  Namely the entry to the dusty pit land in the mid of a left curve.
**The car kept leaving the road for the pit lane.**  In order to prevent this kind of behaviour, we have created a seperate training set, training exactly this situation.  Therefore:

4. One data set focusing onto the entry to the pit lane right after leaving the bridge.

It would be very interesting to figure out if this focused training generalizes to other similar situations.


As was suggested in the lectures, I augmented the training set by flipping images and angles.  Of course, this is kind of redundant when considering our second training set, i.e. completing the lab in the other direction.

I did try to incorporate the left and right camera images into the training set, but achieved only mixed results.  While I believe that 

After the collection process, I had approx. 6000 data points. I then preprocessed this data on-the-fly by cropping both the upper and the lower boundaries by 50px and 20px, respectively.

I finally randomly shuffled the data set and put 30% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. 

I used an *Adam optimizer* so that manually training the learning rate wasn't necessary.  Learning the theory of the Adam optimizer (the concept seems to be very young), augmented my learning of this lecture.
