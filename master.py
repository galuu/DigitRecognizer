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



## Model 1: linearSVC one-vs-rest appraoch - 85% accuracy, relatively little time

classifier2=svm.LinearSVC()
classifier2.fit(train_data[0::,1::], train_data[0::,0])
predicted=classifier2.predict(test_data)
num_obs=np.size(test_data[0::,0])

prediction_file=open('Documents/SideProjects/Projects/DigitRecognizer/submission2.csv', 'wb')            #open a link
p=csv.writer(prediction_file)      #create a writer object

p.writerow(['ImageId', 'Label'])
for i in range(num_obs):
    p.writerow([i+1, predicted[i].astype(np.int)])
    
prediction_file.close()





    
    