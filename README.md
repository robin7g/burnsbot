# burnsbot
# Robert Burns Poetry AI built using GPT2

I used OpenAI's GPT2 pre-trained models to create a poetry AI. In this case we try to make a  Robert Burns poet and all of this is done on an NVIDIA Jetson AGX Xavier

The data used to train the AI model was derived from the **Poems and Songs of Robert Burns** found at the Project Gutenberg
https://www.gutenberg.org/ebooks/author/583


This repository is to accompany a video I created about building a Poetry AI. This is the second generation Burns Bot. The first used much simpler RNN. This version is much beter at language generation. 

## Watch the video here

[![Burns Poetry AI Video](https://img.youtube.com/vi/LjkubM5IIos/0.jpg)](https://www.youtube.com/watch?v=LjkubM5IIos)

Feel free to comment on the video and ask questions. I will try to answer any questions on usage etc. 

## Instructions

**Install TensorFlow GPU**

When using this code GPU acceleration is highlight recommended.  If you are using Ubuntu or similar use pip to install tensorflow GPU , something like this. 

`pip install tensorflow-gpu==1.15`

**Usages:**

`python3 train.py`

Please note this will download a 3.1GB pre-trained GPT2 model, so that takes a while. The retraining process can also take a long time, between 30 minutes up to quite a few hours depending on your machine. 



