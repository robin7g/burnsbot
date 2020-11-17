# burnsbot
# Robert Burns Poetry AI built using GPT2

I used OpenAI's GPT2 pre-trained models to create a poetry AI. In this case we try to make a  Robert Burns poet and all of this is done on an NVIDIA Jetson AGX Xavier

The data used to train the AI model was derived from the **Poems and Songs of Robert Burns** found at the Gutenberg Project 
https://www.gutenberg.org/ebooks/author/583


This repository is to accompany a video I created about building a Poetry AI. This is the second generation Burns Bot. The first used a much simpler RNN. This version is much better at language generation. 

## Watch the video here

[![Burns Poetry AI Video](https://img.youtube.com/vi/LjkubM5IIos/0.jpg)](https://www.youtube.com/watch?v=LjkubM5IIos)

Feel free to comment on the video and ask questions. I will try to answer any questions on usage etc. 

## Instructions

Make sure you have tensorflow install on an NVIDIA Jetson platform machine follow these instructions. Make sure you get the version before v2 of TensorFlow as this code only is known to work with earlier versions. The instructions tell you how to do this. The version I used is 1.15.4

https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html

**Install TensorFlow GPU**

When using this code GPU acceleration is highlight recommended.  If you are using Ubuntu or similar use pip to install tensorflow GPU , something like this. 

`pip3 install tensorflow-gpu==1.15`

**Install GPT2 Simple**

The library mentioned in the video which makes finetuning really simple is called GPT2 Simple. Here is a link to the GitHub repo for those interested

https://github.com/minimaxir/gpt-2-simple

Installing this library is as easy as 

`pip3 install gpt_2_simple`

**Usage**

`python3 train.py`

Please note this will download a 3.1GB pre-trained GPT2 model, so that takes a while. The retraining, finetune process can also take a long time, between 30 minutes up to quite a few hours depending on your machine. An AGX Xavier takes about 170 minutes to run this which includes the time for me to download the 3GB model. 

**License**

MIT


