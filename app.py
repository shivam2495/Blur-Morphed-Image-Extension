from flask import Flask
from flask_cors import CORS
import random
import requests
from flask import jsonify, request
from PIL import Image
from io import BytesIO
import time
app = Flask(__name__)
CORS(app)

@app.route("/img", methods=['POST'])
def infer():
    try:
        url = request.json['img_url']
        ind = request.json['indx']
        save_name = url.split('/').pop()
        print(url)
        response = requests.get(url)
        if response:
            im = Image.open(BytesIO(response.content))
            im.save(save_name)
            server_url = "http://app1.nicheai.io/prediction"
            payload = {'image' : open(save_name, 'rb')}
            response = requests.request("POST", server_url, files=payload)
            result = jsonify(response.json()).json['result']
            print(result)
            time.sleep(1)
            return jsonify({'result': result, 'indx': ind})
        else:
            return jsonify({'error': 'Image not found'})
    except Exception as e:
        return jsonify({'error': '{}'.format(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4201, debug = True, ssl_context=('cert.pem', 'key.pem'))
