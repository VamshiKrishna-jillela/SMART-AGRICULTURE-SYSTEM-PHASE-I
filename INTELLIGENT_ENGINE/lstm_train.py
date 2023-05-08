#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding,Input
from keras.models import Model
from keras.layers import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tensorflow.keras.preprocessing.sequence import pad_sequences



data=pd.read_csv("Crop_recommendation.csv")
data


# In[2]:


data.shape


# In[3]:


l=len(data)
input=[];
output=[];
for i in range(0,l):
  input.append(data.loc[i])
  del input[i]["label"]
  output.append(data.loc[i]["label"])

data


# In[4]:


plant=data.reset_index()["label"]
out=pd.get_dummies(output)
plt.plot(plant)
crop=out.columns
out


# In[5]:


from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))





# In[6]:


x=data[['N','P','K','temperature','humidity','ph','rainfall']].values
x=pad_sequences(x,maxlen=7,padding='pre')
for i in range(0,len(x)):
  for j in range(0,7):
    x[i][j]=float(x[i][j])

y=out.values;
y=scaler.fit_transform(y)
y=pad_sequences(y,maxlen=22,padding='pre')
y


# In[7]:


print(x.shape)
print(y.shape)


# In[8]:


x_train=x[0:1760]
y_train=y[0:1760]

x_test=x[1761:2200]
y_test=y[1761:2200]


x_train,x_test,y_train,y_test=train_test_split(x,y)

x_train


# In[9]:


inp=Input(shape=(7,));
em=Embedding(input_dim=500,output_dim=500)(inp)
m1=LSTM(units=32,return_sequences=True)(em)
m2=LSTM(units=64)(m1)
out=Dense(units=22,activation='softmax')(m2)
model=Model(inputs=inp,outputs=out)

model.summary()


# In[10]:


model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['acc'])


# In[11]:


model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=40,verbose=1,batch_size=256)


# In[12]:


x_train.shape


# In[21]:


output=model.predict(x_test)

model.save('my_model.h5')


# In[22]:


# send=[107,34,32,26,82,6.780,177.77]
# v=[]
# v.append(send)
# rec=model.predict(v)
# plant=[]
# print("Percentage of work by crops")
# for i in range(0,22):
#   plant.append([rec[0][i]*100,crop[i]])


# plant.sort(reverse=1)
# for i in range(0,22):
#   print(plant[i])


print(crop)
# In[ ]:




