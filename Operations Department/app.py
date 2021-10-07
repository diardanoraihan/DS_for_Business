from logging import debug
from flask import Flask, render_template, request
# from werkzeug.wrappers import request

# standard instance name
app = Flask(__name__)

# create a route 
@app.route('/', methods=['GET'])
def hello_world():
    # return 'Hello world'
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    # retrieve the name of the tag that contains the image file in index.html
    imagefile = request.files['imagefile']
    image_path = "./Images/" + imagefile.filename
    imagefile.save(image_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
