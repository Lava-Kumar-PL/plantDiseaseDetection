# from flask import Flask, render_template, jsonify, request , Markup
from flask import Flask, render_template, jsonify, request
from markupsafe import Markup

import base64
from io import BytesIO
from PIL import Image

from model import predict_image
import utils

app = Flask(__name__)

@app.route('/',methods=['GET'])
def landing():
    return render_template('landing.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img_bytes = file.read()

            # Convert image to base64 for HTML display
            encoded_img = base64.b64encode(img_bytes).decode('utf-8')
            image_data = f"data:image/jpeg;base64,{encoded_img}"

            prediction = predict_image(img_bytes)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('predict.html', status=200, result=res, image=image_data)
        except Exception as e:
            print(e)
    return render_template('predict.html', status=500, res="get")



if __name__ == "__main__":
    app.run(debug=True)
