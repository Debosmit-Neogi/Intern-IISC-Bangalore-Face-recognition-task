# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F_3ed06tVLE9QXXaF3OJdQhhMulWTTJ9
"""

!git clone https://github.com/ZhaoJ9014/face.evoLVe.PyTorch.git

dataset='/content/drive/My Drive/lfw.zip'

# Commented out IPython magic to ensure Python compatibility.
# % cd ./face.evoLVe.PyTorch/

# Commented out IPython magic to ensure Python compatibility.
# % cd ./applications/
# % cd ./align/

from PIL import Image
from detector import detect_faces
from visualization_utils import show_results

img = Image.open('/content/drive/My Drive/image.jpeg') # modify the image path to yours
bounding_boxes, landmarks = detect_faces(img) # detect bboxes and landmarks for all faces in the image
show_results(img, bounding_boxes, landmarks)

# Commented out IPython magic to ensure Python compatibility.
# %cd-

# Commented out IPython magic to ensure Python compatibility.
# %cd /root/face.evoLVe.PyTorch/

mkdir data

# Commented out IPython magic to ensure Python compatibility.
# %cd data

!unzip '/content/drive/My Drive/lfw.zip'

# Commented out IPython magic to ensure Python compatibility.
# %cd /root/face.evoLVe.PyTorch/applications/align

!python face_align.py -source_root '/root/face.evoLVe.PyTorch/data/lfw' -dest_root '/content/drive/My Drive/Lfw face recognition' -crop_size 112

!python face_resize.py

# Commented out IPython magic to ensure Python compatibility.
# %cd /root/face.evoLVe.PyTorch/balance

!python remove_lowshot.py -root '/root/face.evoLVe.PyTorch/data/lfw' -min_num 10

# Commented out IPython magic to ensure Python compatibility.
# %cd ./

import torch

configurations = {
    1: dict(
        SEED = 1337, # random seed for reproduce results

        DATA_ROOT = '/media/pc/6T/jasonjzhao/data/faces_emore', # the parent root where your train/val/test data are stored
        MODEL_ROOT = '/media/pc/6T/jasonjzhao/buffer/model', # the root to buffer your checkpoints
        LOG_ROOT = '/media/pc/6T/jasonjzhao/buffer/log', # the root to log your train/val status
        BACKBONE_RESUME_ROOT = './', # the root to resume training from a saved checkpoint
        HEAD_RESUME_ROOT = './', # the root to resume training from a saved checkpoint

        BACKBONE_NAME = 'IR_SE_50', # support: ['ResNet_50', 'ResNet_101', 'ResNet_152', 'IR_50', 'IR_101', 'IR_152', 'IR_SE_50', 'IR_SE_101', 'IR_SE_152']
        HEAD_NAME = 'ArcFace', # support:  ['Softmax', 'ArcFace', 'CosFace', 'SphereFace', 'Am_softmax']
        LOSS_NAME = 'Focal', # support: ['Focal', 'Softmax']

        INPUT_SIZE = [112, 112], # support: [112, 112] and [224, 224]
        RGB_MEAN = [0.5, 0.5, 0.5], # for normalize inputs to [-1, 1]
        RGB_STD = [0.5, 0.5, 0.5],
        EMBEDDING_SIZE = 512, # feature dimension
        BATCH_SIZE = 512,
        DROP_LAST = True, # whether drop the last batch to ensure consistent batch_norm statistics
        LR = 0.1, # initial LR
        NUM_EPOCH = 125, # total epoch number (use the firt 1/25 epochs to warm up)
        WEIGHT_DECAY = 5e-4, # do not apply to batch_norm parameters
        MOMENTUM = 0.9,
        STAGES = [35, 65, 95], # epoch stages to decay learning rate

        DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
        MULTI_GPU = True, # flag to use multiple GPUs; if you choose to train with single GPU, you should first run "export CUDA_VISILE_DEVICES=device_id" to specify the GPU card you want to use
        GPU_ID = [0, 1, 2, 3], # specify your GPU ids
        PIN_MEMORY = True,
        NUM_WORKERS = 0,
),
}

