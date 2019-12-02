from flask import Flask, render_template, jsonify, request, flash, redirect
import server_details
import json
import importlib
import os,sys
from collections import OrderedDict
from werkzeug.utils import secure_filename

cur_dir = os.path.dirname(os.path.abspath(__file__))
connecting_config_dir = os.path.abspath(os.path.join(cur_dir, "../../connecting_configs"))
flask_config_dir = os.path.abspath(os.path.join(cur_dir, "configs"))

sys.path.append(connecting_config_dir)
from flask_apis import api_objects_config_dict
del sys.path[sys.path.index(connecting_config_dir)]

app = Flask(__name__)

app.secret_key = "secret key"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



data_migrator_config_dir = os.path.join(flask_config_dir, "data_migrator")
data_migrator_ui_params_file = os.path.join(data_migrator_config_dir, "data_migrator_ui_params.json")
data_migrator_ui_params_dict = dict()
with open(data_migrator_ui_params_file, "r") as f:
	data_migrator_ui_params_dict = json.load(f, object_pairs_hook=OrderedDict)

@app.route("/data_migrator")
def data_migrator():
	return render_template("data_migrator.html", data_migrator_ui_params=data_migrator_ui_params_dict)





############################################################################################

data_migrator_dir = os.path.abspath(os.path.join(cur_dir, "../../services/data_migrator"))
data_migrator_input_configs_dir = os.path.join(data_migrator_dir, "src/config/run_time_config")


# @app.route("/upload_files")
# def upload_files():
# 	return render_template("upload_files.html")


@app.route("/upload_files", methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files')
		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(data_migrator_input_configs_dir, filename))
		flash('File(s) successfully uploaded')
		# return redirect('/upload_files')
		return dict()


###########################################################################################

@app.route("/<version>/<api_name>/process", methods = ['POST', 'GET'])
def process(version, api_name):
	request_dict = dict()
	if request.method == "POST":
		request_dict = request.json
	elif request.method == "GET":
		request_dict = request.args
		
	reponse_dict = dict()
	api_object = api_objects_config_dict.get(version).get(api_name).get("object_instance")
	response_dict = api_object.process(request_dict)
	
	return jsonify(response_dict)


if __name__ == "__main__":
	app.run(host = server_details.FLASK_HOST, port = server_details.FLASK_PORT, debug = True)
