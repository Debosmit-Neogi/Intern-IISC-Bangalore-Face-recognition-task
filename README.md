# Face-recognition-task-code-base-using-LFW-dataset

This repository contains all the code and results of the experiments conducted during my research internship at **Visual Computing Lab, IISC Bangalore**. My objective was to implement various face recognition algorithms on the **LFW Dataset** (http://vis-www.cs.umass.edu/lfw/) and perform comparative studies on the result metrics obtained.

 * I started my experiments by using the most popular light weight face recognition library **Deep Face** (https://github.com/serengil/deepface). 

 The models used were VGG-Face and Arc-Face 
      
  The F1 score obtained after training 1000 pairs are:
  
                    1. Arc-Face model: 94.5945945945946
                    
                    2. VGG-Face model: 87.24353256021409
  The metrics used/obtained:
           
          [{'verified': True, 'distance': 0.21600544769726582, 'max_threshold_to_verify': 0.4, 'model': 'VGG-Face', 'similarity_metric': 'cosine'},
                     
          {'verified': True, 'distance': 1.0554645896609927e-05, 'max_threshold_to_verify': 0.68, 'model': 'ArcFace', 'similarity_metric': 'cosine'},
                     
          {'verified': True, 'distance': 0.21600544769726582, 'max_threshold_to_verify': 0.4, 'model': 'VGG-Face', 'similarity_metric': 'cosine'}]
            
                    
   For details regarding results obtained, check **Results** directory.

* The second approach was using **face.evoLVe** (https://github.com/ZhaoJ9014/face.evoLVe). face.evoLVe is a high performance Face Recognition library. For the most part, I was able to implement the algorithm to perform face detection task on various images. You can check the **Results** section.


## PRE-REQUISITES
 * Python >= 3.6 (for Training & Validation) and Python 2.7 (For visualization using Tensorboard)

## INSTALL
* Clone the repo
  ```
  git clone https://github.com/Debosmit-Neogi/Face-recognition-task-code-base-using-LFW-dataset.git
  ```

* Install the dependencies
  ```
  pip install -r requirements.txt
  ```

         
P.S:
The code available in this directory are not the complete work. The code is for just the parts of the project that are open sourced.
