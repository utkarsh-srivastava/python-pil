from PIL import Image
import os

read_folder_path = 'read-images'
write_folder = 'write-images'

ratio = (200,100)

def shrink_images():
  for dirpath, dirnames, filenames in os.walk(read_folder_path):
    print(dirpath, dirnames, filenames)
    for filename in filenames:
      image = Image.open(os.path.join(os.getcwd(),dirpath,filename))
      resized_image = image.resize(ratio)
      resized_image.save(os.path.join(os.getcwd(),write_folder,filename))


if __name__ == '__main__':
  shrink_images()

