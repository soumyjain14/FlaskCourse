from flask import Flask, render_template, redirect, request

app1=Flask(__name__)

friends=['Ram','Shyam','Dham']
num=5

@app1.route('/')
def hello():
	return render_template("index.html",my_friends=friends,number=num)

@app1.route('/about')
def about():
	return "<h1> About Page </h1>"

@app1.route('/home',)
def home():
	return redirect ("/")

@app1.route('/submit',methods=['POST'])
def submit():
	if request.method == 'POST':
		name=request.form['Your name']

		f=request.files['userfiles']
		print(f)
		f.save(f.filename)

	return "<h1> Hello {}".format(name)




if __name__=='__main__':
	app1.run(debug=True)