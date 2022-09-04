from os import path
from os import listdir
import cv2
import face_recognition
from mtcnn.mtcnn import MTCNN

directory = './data/boundbox'
detector = MTCNN()

if __name__ == '__main__':
  base_path = './data/face_extraction'
  base_fake_path = './data/dataset/fake'
  base_real_path = './data/dataset/real'

  print('Extracting faces...')

  fakes = listdir('./data/dataset/fake')
  reals = listdir('./data/dataset/real')

  fake_total = len(fakes)
  real_total = len(reals)  

  for i,f in enumerate(fakes):
    f = f.split(',')
    filename = f[0]
    print(f'Processing {filename} ({i}/{fake_total})')
    img = cv2.imread(path.join(base_fake_path,filename))    
    face_locations = detector.detect_faces(img)
    print(face_locations)
    break