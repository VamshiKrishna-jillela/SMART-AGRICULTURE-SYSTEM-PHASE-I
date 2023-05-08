from tensorflow import keras
from keras.models import load_model
import json
import collections
from datetime import date


# send=[107,34,32,26,82,6.780,177.77]
model = load_model('/home/vamshi2171/Desktop/temp/INTELLIGENT_ENGINE/my_model.h5')
crop=['apple', 'banana', 'blackgram', 'chickpea', 'coconut', 'coffee',
       'cotton', 'grapes', 'jute', 'kidneybeans', 'lentil', 'maize', 'mango',
       'mothbeans', 'mungbean', 'muskmelon', 'orange', 'papaya', 'pigeonpeas',
       'pomegranate', 'rice', 'watermelon']
parameter_Names=['N','P','K','temperature','humidity','ph','rainfall']
# v=[]
# v.append(send)
# rec=model.predict(v)
# plant=[]
# for i in range(0,22):
#   plant.append([rec[0][i]*100,crop[i]])


# plant.sort(reverse=1)
# for i in range(0,22):
#   print(plant[i])



def cropRecommend(Params):
    model = load_model('/home/vamshi2171/Desktop/temp/INTELLIGENT_ENGINE/my_model.h5')
    final={}
    v=[]
    extracted_params=[]
    for parameter in parameter_Names:
      extracted_params.append(float(Params[parameter]))
    print(extracted_params)
    v.append(extracted_params)
    rec=model.predict(v)
    Prediction_Distribution={}
    for i in range(0,22):
      Prediction_Distribution[crop[i]]=rec[0][i]*100
    dict(sorted(Prediction_Distribution.items(), key=lambda item: item[1]))
    final["label"]=Prediction_Distribution
    final["date"]= str(date.today())
    json_final = json.dumps(final)
    # print(json_final)
    return json_final



    


