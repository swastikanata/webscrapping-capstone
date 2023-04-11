from flask import Flask, render_template

#don't change this
app = Flask(__name__) #do not change this

@app.route("/")
def index(): 

	# render to html
	return render_template('index.html')


if __name__ == "__main__": 
    app.run(debug=True)