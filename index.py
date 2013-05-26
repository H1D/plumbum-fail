from plumbum.cmd import ls
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return ls()

if __name__ == "__main__":
	app.debug = True
	app.run()
