from flask import Flask,render_template,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   

import sys
sys.path.insert(0, '/home/vamshi2171/Desktop/temp/INTELLIGENT_ENGINE')
from lstm_test import cropRecommend



@app.route('/form',methods=['POST',"GET"])
def index():
    send=request.get_json()
    # send={
    #     "N": "50",
    #     "P": "91",
    #     "K": "1",
    #     "temperature":"203.79744",
    #     "humidity":"198.002744",
    #     "ph":"7.902985",
    #     "rainfall":"110.99"
    # }
    #Gives the labelled Data
    
    Predicted_JSON=cropRecommend(send)
    print(Predicted_JSON)
    
    # return Predicted_JSON
    return jsonify(Predicted_JSON)

if __name__ == "__main__":

    app.run(debug=True)
    