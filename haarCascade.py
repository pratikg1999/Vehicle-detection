import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513
    neg_images_link  = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    neg_image_urls  = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 859

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE )
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
            pic_num+=1

        except Exception as e:
            print(str(e))

def find_uglies():
    for(file_type) in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+ '/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    if(ugly.shape == question.shape and not(np.bitwise_xor(ugly, question).any())):
                        print('ugly found')
                        print(current_image_path)
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))

def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if(file_type=='neg'):
                line = file_type+'/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

            elif(file_type=='pos'):
                line = img+' 1 0 0 50 50\n'
                with open('info.lst', 'a') as f:
                    f.write(line)

def toGrayScale(path):
    j=0
    for img in os.listdir(str(path)):
        print(img)
        i = cv2.imread(str(path)+"/"+img, cv2.IMREAD_GRAYSCALE )
        #resized_image = cv2.resize(i, (100,100))
        
        cv2.imwrite(str(path)+"2/"+str(j)+".jpg", i)
        j+=1

toGrayScale('pos')
#create_pos_n_neg()
# find_uglies()