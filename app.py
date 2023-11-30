from PIL import Image
from flask import Flask, request
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
    print(data.get("image"))
    # image = request.files["image"] #odczytywanie obrazka z requesta
    # img = Image.open(image)
    # print(img.size)
    # img = img.convert("L") #grayscale
    # laplacian = cv2.Laplacian(np.asarray(img), cv2.CV_64F, ksize=3)
    # Convert back to uint8 and normalize values to 0-255 range
    # laplacian = np.uint8(np.absolute(laplacian))
    # laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    # return str(np.amax(laplacian))

if __name__ == '__main__':
    app.run()
