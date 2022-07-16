from os import path
from os import listdir
import cv2
import face_recognition

directory = './data/boundbox'

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
    image = face_recognition.load_image_file(path.join(base_fake_path,filename))
    face_locations = face_recognition.face_locations(image)
    for face_location in face_locations:
      top, right, bottom, left = face_location
      crop_img = image[top:bottom, left:right]
      out_path = path.join(base_path, 'fake', path.basename(filename))
      cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB, crop_img)
      cv2.imwrite(out_path, crop_img)
      break

  for i,f in enumerate(reals):
    f = f.split(',')
    filename = f[0]
    print(f'Processing {filename} ({i}/{real_total})')
    image = face_recognition.load_image_file(path.join(base_real_path, filename))
    face_locations = face_recognition.face_locations(image)    
    for face_location in face_locations:
      top, right, bottom, left = face_location
      crop_img = image[top:bottom, left:right]
      out_path = path.join(base_path, 'real', path.basename(filename))
      cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB, crop_img)
      cv2.imwrite(out_path, crop_img)