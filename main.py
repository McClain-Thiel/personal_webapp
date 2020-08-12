from flask import Flask, render_template, flash, request
import requests

app = Flask(__name__)
app.secret_key = b'many random bytes'

@app.route('/', methods=["GET", "POST"])
def root():
    return render_template('resume/resume.html')

@app.route('/class_projects')
def class_projects():
    return render_template('resume/projects.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python38_render_template]

