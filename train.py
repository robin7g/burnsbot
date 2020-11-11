# Python Code to demonstrate builing a Scottish Poet AI
# uses gpt_2_simple and a 774M node GPT2 model
# Author: Robin Grosset April 2020
# 
# Feel free to use and build your own Poet AI!
# Code provided under the MIT License



import gpt_2_simple as gpt2
import os
import requests
import tensorflow as tf
from tensorflow.core.protobuf import rewriter_config_pb2
from tensorflow.python.client import device_lib

model_name = "774M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/774M/


file_name = "burns.txt"

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction=0.875
config.graph_options.rewrite_options.layout_optimizer = rewriter_config_pb2.RewriterConfig.OFF
sess = tf.compat.v1.Session(config=config)

gpt2.finetune(sess,
              file_name,
              model_name=model_name,	   
              steps=1000)   # steps is max number of training steps

gpt2.generate(sess)
