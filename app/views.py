#coding=utf-8
from app import app, db
from flask import render_template
import os
import markdown2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/<page_name>')
def page(page_name):
	#find file
	flag = False
	file_list = os.listdir(app.config['DATA_POSITION'])
	for file_name in file_list:
		if page_name == file_name:
			flag = True
			break
		if page_name + '.md' == file_name:
			flag = True
			page_name = page_name + '.md'
			break
	if not flag:
		param = {
			'title': 'Error',
			'content': 'File Not Found'
		}
		return render_template('page.html',
								param = param)
	
	#read file
	file_object = open(os.path.join(app.config['DATA_POSITION'], page_name), 'r')
	try:
		content = file_object.read()
	finally:
		file_object.close()

	#render markdown
	content = markdown2.markdown(content)

	#render html
	param = {
		'title': 'Page',
		'content': content
	}
	return render_template('page.html',
							param = param)
