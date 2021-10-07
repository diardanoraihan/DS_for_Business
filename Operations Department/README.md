# Chest Diseases Diagnosis
__Operations Department Business Case__ 

Use Deep Learning to automate the process of detecting and classifying chest diseases in a hospital.
- Author: Diardano Raihan
- Email: diardano@gmail.com
- Social Media: [LinkedIn](https://www.linkedin.com/in/diardanoraihan/), [Medium](https://diardano.medium.com/)

## Project Summary
- Built a deep learning model to classify 4-class X-ray chest images in Python and TensorFlow for detecting diseases in a hospital.
- Modified and retrained a residual neural network (ResNet50) with a 96% accuracy on training data, 89% on validation, and 83% on the test set.
- Converted the model into JSON format using TensorFlow.js to be deployed into a browser.

## Case Study
Deep learning has been proven to be superior in detecting and classifying disease using imagery data. Skin cancer could be detected more accurately by Deep Learning by dermatologists (2018).
- Human dermatologists detection = 86.6%
- Deep Learning detection = 95%

_Rereference: "Computer learns to detect skin cancer more accurately than doctors". The Guardian, 29 May 2018._

In this case study, we will assume that you work as a __Deep Learning Consultant__. 
- You have been hired by a hospital in downtown Toronto and you have been tasked to automate the process of detecting and classifying chest disease and reduce the cost and time of detection.
- The team has collected extensive X-Ray Chest data and they approached you to develop a model that could detect and classify the diseases in less than 1 minute.
- You have been provided with 133 images that belong to 4 classes:
  - Healthy
  - Covid-19
  - Bacterial Pneumonia
  - Viral Pneumonia

## Datasets
This is a custom dataset that contains covid-19 x-ray images, viral pneumonia x-ray images, bacterial pneumonia x-ray images, and normal person x-ray images. Each class contains 133 images.
Source:
- https://github.com/ieee8023/covid-chestxray-dataset
- https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia
