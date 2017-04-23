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
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md for summarizing the results

####2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

####3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

###Model Architecture and Training Strategy

####1. An appropriate model architecture has been employed

My model consists of a convolution neural network with 3x3 filter sizes and depths between 32 and 128 (model.py lines 18-24) 

The model includes RELU layers to introduce nonlinearity (code line 20), and the data is normalized in the model using a Keras lambda layer (code line 18). 

####2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting (model.py line 66). 

The model was trained and validated on different data sets to ensure that the model was not overfitting **(code line 73-76)**. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Model parameter tuning

The model used an Adam optimizer, so the learning rate was not tuned manually **(model.py line 73)**.

####4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I essentially created three sets:
1. dfsdf
  * sdf
2. ds
  * sdf



For details about how I created the training data, see the next section. 

###Model Architecture and Training Strategy

####1. Solution Design Approach

The overall strategy for deriving a model architecture was to ...

My first step was to use a convolution neural network model similar to the ... I thought this model might be appropriate because ...

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model so that ...

Then I ... 

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track... to improve the driving behavior in these cases, I ....

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

####2. Final Model Architecture

The final model architecture **(model.py lines 51-71)** consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

####3. Creation of the Training Set & Training Process

In order to teach the network good driving behavious, I have created two data sets:
1. Two labs of center lane driving around track 1.
2. Two labs of center lane driving into the opposite direction.
2. Approx. 1:30 minutes of recovery drinving, etc. allowing the car to take a road mitigating trajectory and recovering before leaving the road.

Although the car behaved well after training the neural net with these two sets, there was one particular siutation just after leaving the bridge:  Namely the entry to the dusty pit land in the mid of a left curve.
The car kept leaving the road for the pit.
In order to prevent this kind of behaviour, we have created a seperate training set, training exactly this situation.  Therefore:

3. One data set focusing onto the entry to the pit lane right after leaving the bridge.

It would be very interesting to figure out if this focused training generalizes to other similar situations.


As was suggested in the lectures, I augmented the training set by flipping images and angles.  Of course, this is kind of redundant when considering our second training set, i.e. completing the lab in the other direction.

I did try to incorporate the left and right camera images into the training set, but achieved only mixed results.  While I believe that 

After the collection process, I had **???** number of data points. I then preprocessed this data on-the-fly by cropping both the upper and the lower boundaries by px, respectively.


I finally randomly shuffled the data set and put 30% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. 

I used an *Adam optimizer* so that manually training the learning rate wasn't necessary.  Learning the theory of the Adam optimizer (the concept seems to be very young), augmented my learning of this lecture.
