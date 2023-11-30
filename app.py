import base64
from io import BytesIO

from PIL import Image
from flask import Flask, request, jsonify
import cv2
import numpy as np


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/blur', methods = ["POST"])
def analyze():
    content_type = request.headers.get("Content-Type")
    print(content_type)
    data = request.json
    image_str = data.get("image")
    img = Image.open(BytesIO(base64.b64decode(image_str)))
    print(img.size)
    img = img.convert("L") #grayscale
    laplacian = cv2.Laplacian(np.asarray(img), cv2.CV_64F, ksize=3)
    # Convert back to uint8 and normalize values to 0-255 range
    # laplacian = np.uint8(np.absolute(laplacian))
    # laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    return jsonify({"score": str(np.amax(laplacian))})

if __name__ == '__main__':
    app.run()
