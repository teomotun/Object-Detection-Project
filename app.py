import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


APP_ROOT =os.path.dirname(os.path.abspath(__file__))
upload = os.getcwd() + '/uploads/'

app = Flask(__name__)
dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
#app.config['DROPZONE_REDIRECT_VIEW'] = 'index'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

# #Remove files in uploads directory
# filelist = [f for f in os.listdir(upload)]
# [os.remove(os.path.join(upload, f)) for f in filelist]

@app.route('/', methods=['GET', 'POST'])
def index():
	# set session for image results
	if "file_urls" not in session:
		session['file_urls'] = []
	# list to hold our uploaded image urls
	file_urls = session['file_urls']

	# handle image upload from Dropszone
	if request.method == 'POST':
		file_obj = request.files
		for f in file_obj:
			file = request.files.get(f)

			# save the file with to our photos folder
			filename = photos.save(
					file,
					name=file.filename
			)

			# append image urls
			file_urls.append(photos.url(filename))

		session['file_urls'] = file_urls
	# return dropzone template on GET request
	return render_template('index.html')


# @app.route('/show_image')
# def results():
# 	# set the file_urls and remove the session variable
# 	file_urls = session['file_urls']
# 	session.pop('file_urls', None)
# 	return render_template('index.html', file_urls=file_urls)

	


if __name__ == "__main__":
    app.run(debug=True)
