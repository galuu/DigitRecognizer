######## Digit Recognizer Challenge 

## Importing the tools

import csv as csv
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import random as random



## opening and loading csv file
csv_file_object=csv.reader(open('Documents/SideProjects/Projects/DigitRecognizer/train.csv','rb'))
header=csv_file_object.next()


## saving the file as a dataframe 
data=[]

for row in csv_file_object:
    data.append(row)
    
## turning the list object into an array object using numpy function
data=np.array(data)

## turning strings into float
train_data=data.astype(np.float)

## Loading test data
csv_file_testobject=csv.reader(open('Documents/SideProjects/Projects/DigitRecognizer/test.csv','rb'))
header=csv_file_testobject.next()
test=[]

for row in csv_file_testobject:
    test.append(row)

test=np.array(test)
test_data=test.astype(np.float)

## Defining useful variables

number_obs=np.size(train_data[0::,1])
pixel_height=28
pixel_width=28
output=train_data[0::,1]
input=train_data[0::,1:]



## Visualizing a random observation

##picking a random observation



index_range=range(number_obs)
index=random.sample(index_range, 1)

##reshaping the observation into an array

display_array=np.reshape(input[index,0::], (pixel_height, pixel_width))

##plotting the chosen observation

plt.imshow(display_array, cmap=cm.Greys_r)
plt.show()


## Visualizing 10 random observations
## Picking 10 random observations
indexarray=random.sample(index_range, 4) 

##defining a new array for the image


im_array=np.array([[-np.ones([28,28]), -np.ones([28,28])],[ -np.ones([28,28]), -np.ones([28,28])]])

num_rows=2
num_col=2


curr_image=0
im1=np.reshape(input[indexarray[curr_image],0::], (pixel_height, pixel_width))
        
curr_image=1
im2=np.reshape(input[indexarray[curr_image],0::], (pixel_height, pixel_width))
        
curr_image=2
im3=np.reshape(input[indexarray[curr_image],0::], (pixel_height, pixel_width))    
curr_image=3
im4=np.reshape(input[indexarray[curr_image],0::], (pixel_height, pixel_width))
        
new_array=np.reshape(im_array.flatten(), (pixel_height*2, pixel_width*2))  
    
plt.imshow(new_array, cmap=cm.Greys_r)
plt.show()


fig=plt.figure(facecolor='white')
ax.set_xticks([])
ax.set_yticks([])
a=fig.add_subplot(221)
ax.set_xticks([])
imgplot=plt.imshow(im1, cmap=cm.Greys_r)
a=fig.add_subplot(222)
imgplot=plt.imshow(im2,cmap=cm.Greys_r)
a=fig.add_subplot(223)
imgplot=plt.imshow(im3, cmap=cm.Greys_r)
a=fig.add_subplot(224)
imgplot=plt.imshow(im4, cmap=cm.Greys_r)
plt.show()

## Turning each observation into a polynomial function

poly_array[i]= sum over j input[i,j] x^j 
plot all of them see if there is a clear divide between classes
















