from mtcnn.mtcnn import MTCNN
import cv2

# Supress tensorflow warnings
import os
#os. environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

detector = MTCNN()

IMAGES_PATH = './dataset/fake'

def get_filenames():
    import os
    return [os.path.join('./data/dataset/fake/', f) for f in os.listdir('./data/dataset/fake/')]

if __name__ == '__main__':
  print('Extracting faces...')

  filenames = get_filenames()

  total = len(filenames)

  for filename in filenames:
    print('Processing {} ({}/{})'.format(filename, filenames.index(filename) + 1, total))
    img = cv2.imread(filename)    
    cv2.waitKey(0)    
    detected_faces = detector.detect_faces(img)
    print(detected_faces)
    if len(detected_faces) > 0:
      for face in detected_faces:
        x, y, w, h = face['box']
        crop_img = img[y:y+h, x:x+w]        
        out_path = os.path.join(IMAGES_PATH, 'face_' + os.path.basename(filename))
        cv2.imwrite(out_path,crop_img)    