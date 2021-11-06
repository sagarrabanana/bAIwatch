
# this script is made to help in the manual classificatio. You will have to modify the directories before using.
# the script will show you all the images from the main directory and move them to their correct place by pressing B(for good waves), M(for bad ones) and D(for discards)

import os
import shutil
import cv2
import time
i=0
directory = r'dataset directory'#'/home/myuser/Escritorio/dataSet_Plentzia/SanValentin'
directorySaveBuenas = r'folder for good waves'
directorySaveMalas = r'folder for bad waves'
directorySaveDescarte = r'folder for discarted images'
for filename in sorted(os.listdir(directory)):
    cv2.destroyAllWindows()
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img=cv2.imread(os.path.join(directory, filename))
        cv2.imshow(filename,img)
        key=cv2.waitKey(0)
        if key== ord('b'):
            print('tecla B pulsada')
            shutil.move(directory+'/'+ filename,directorySaveBuenas+'/'+filename)
            print('movida a Buenas')
        elif key== ord('m'):
            print('tecla M pulsada')
            shutil.move(directory+'/'+ filename,directorySaveMalas+'/'+filename)
            print('movida a Malas')
        elif key== ord('d'):
            print('tecla D pulsada')
            shutil.move(directory+'/'+ filename,directorySaveDescarte+'/'+filename)
            print('movida a Descartes')
    else:
        continue