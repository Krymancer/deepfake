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


The first try, consist of a implementation of a simple classifier to detect deepfake images using the real_fulls and fake_baseline subdatasets. 
For now we are justing trying to use the images at it is. no cropring or preprocessing and feed them in a mesoNet like model. 
But as expected the classifier is not very accurate and unpredictable.

The second approach is to crop the faces to feed into the same model.
I use three tools to extract the faces:

- [OpenCV](https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html)
- [MTCNN](https://github.com/ipazc/mtcnn)
- [Face Recognition](https://github.com/ageitgey/face_recognition) 

Use a script for each tool to extract the faces. then save the images at a separate folder, then feed into the model, with a Keras ImageGenerator.

But the results are not good. Neither opencv, mtcnn or face_detection made much a difference in the results. Getting arround 0.6 accuracy, what is far from what i expected.

The next step is to apply a padding in the faces and use data from eye, mouth, nose, and jaw to feed into the model. 
I think i'll keep using the Face Recognition library for this. And only change the input of model to comport the new features we are gonna analyze.

I researched about deepfake and find some interesting articles, [The Creation and Detection of Deepfakes: A Survey](https://arxiv.org/pdf/2004.11138.pdf) is a great starting point to
get more in depth into the subject. Talks about how to create deepfake videos and images but also about post processing to make them more realistic and harder to detect.

I also trying some thecnics i found in [FaceFlorencics++](https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md) to maybe make de accuracy better.

Some kaggle competitions are also interesting to try out:
- [DeepFake Starter Kit](https://www.kaggle.com/code/gpreda/deepfake-starter-kit)
- [DeepFake Introducation](https://www.kaggle.com/code/robikscube/kaggle-deepfake-detection-introduction)
