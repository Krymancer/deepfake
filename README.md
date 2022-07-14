# Deepfake detection

Project to test and implement models to detect deepfake videos or images

## Devlog

Entry point for this projet is the [DFGC-21 Dataset](https://github.com/bomb2peng/DFGC_starterkit/tree/master/DFGC-21%20dataset) 
and the [MesoNet](https://github.com/DariusAf/MesoNet) classifier.

The DFGC-21 dataset comes with a alrge variety of images created from [Celeb-DF](https://github.com/yuezunli/celeb-deepfakeforensics) 
dataset.
The DFGC-21 dataset contains the following sub-datasets:

|  Subset   | Method  |
|  ----  | ----  |
| real_fulls.zip |   original Celeb-DF real data |  
|fake_baseline.zip	|				 original Celeb-DF fake data|  
|DFGC_SYSU_852924.zip    |		 Adversarial Attacks with some post processing|  
|jerryHUST_853638.zip  		|	 FaceShifter + Adversarial Attacks; A self-trained faceswap model with some post processing|  
|miaotao_853000.zip  		|	 FaceShifter|  
|seanseattle_853068.zip  	|	 FaceController + Adversarial Attacks    |  
|yZzzzzz_849853.zip			|	 MegaFS on 256 resolution|  
|DFischerHDA_852673.zip  	|	 FaceMorpher + dlib landmarks +|  
|joshhu_853266.zip  		|		 Adversarial Attacks   |  
|nbhh_853436.zip     		|	 FaceShifter + Adversarial Attacks|  
|smartz_849705.zip       	|	 A face-anonymization algorithm generated data|  
|yangquanwei_852303.zip  	|	 Swap facial regions based on key points of the face|  
|zhaobh_852336.zip			|	 Using an adversarial model to generate noise to add on warp-based face swap results|  
|ctmiu_853213.zip   		|		 FaceShifter + Adversarial Attacks  |  
|lowtec_853184.zip   		|	 FacceShifter with some post processing      |  
|wany_853175.zip   			|	 face shifter      |  
|yuejiang_852934.zip    	|		 crop and paste |  
|zz110_853170.zip			|	 unkown| 

Frist we will try to implement a classifier to detect deepfake images using the real_fulls and fake_baseline subdatasets. 

The frist thing trid was to use the images at it is. no cropring or preprocessing and feed them in a mesoNet like model. 

The second try was to use opencv to extract faces, but the results are not good. much variantion and some images cant 
extract the face. So i use [MTCNN](https://github.com/ipazc/mtcnn) to extract all faces then fit into the model. As the 
results are no satisfatory either i tried to use another face detection method

The other model i use is [Face Recognition](https://github.com/ageitgey/face_recognition) to extract faces from images.
this has a cli interface and can be used to extract faces from images given a directtory and it will return the filename and 
the face location. 

With this info i was able to extract the faces to feed into the model