import flask
from flask import render_template
#librarires for image to Text 
import pytesseract
from PIL import Image
import pyttsx3
import os
import werkzeug
#libraries for text summarization
from gensim.summarization import summarize
#pytesseract.pytesseract.tesseract_cmd = '/app/vendor/tesseract-ocr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd ='/app/.apt/usr/bin/tesseract'

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
	image= Image.open('sample2.jpg')
	result=pytesseract.image_to_string(image)
	result=result.replace("\n"," ")   
	with open('information.txt',mode='w') as file:
		file.write(result)
		print(result)
	 
	# text_summarization    
	mytext1=open("information.txt","r")
	summary_text=summarize(mytext1.read())
	print(summary_text)
	with open('summary.txt',mode='w') as file:
		file.write(summary_text)    
	if summary_text == "":
		return "Image doesn't contain any text"
	return summary_text


@app.route('/readme', methods=['GET', 'POST'])
def readme():
	return render_template('readme.html')

if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5005, debug=True)
#app.run()
