import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")




fake_input = os.path.join('.','data','dataset','fake')
real_input = os.path.join('.','data','dataset','real')
fake_output = os.path.join('.','data','face_extraction_cv2','fake')
real_output = os.path.join('.','data','face_extraction_cv2','real')

def extract_faces(image_path, output_path):
  image = cv2.imread(image_path)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
  )
  for (x, y, w, h) in faces:
    crop = image[y:y+h, x:x+w]
    path = os.path.join(output_path, os.path.basename(image_path))
    if not cv2.imwrite(path, crop):
      print('Save image {path} failed'.format(path=path))

def get_filenames(path):
    return [os.path.join(path, f) for f in os.listdir(path)]

def main():
  print('Extracting faces...')

  print('Fake:')
  filenames = get_filenames(fake_input)
  total = len(filenames)

  for filename in filenames:
    print('Processing {} ({}/{})'.format(filename, filenames.index(filename) + 1, total))
    extract_faces(filename, fake_output)

  print('Real:')
  filenames = get_filenames(real_input)
  total = len(filenames)

  for filename in filenames:
    print('Processing {} ({}/{})'.format(filename, filenames.index(filename) + 1, total))
    extract_faces(filename, real_output)

if __name__ == '__main__':
    main()