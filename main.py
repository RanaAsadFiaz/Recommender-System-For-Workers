from flask import Flask , render_template, request

#Flask Code ==================

app = Flask(__name__)

@app.route('/')
def index():
	#anything you want to do will go here before return 
	#results us page pr lay k janey ka process btata hu messenger pr aja call prok
	name = ['nauman' , 'ali' , 'rana']
	places = ['nauman' , 'ali' , 'rana']
	
	return render_template('index.html' , returned={'name':name , 'place':places})

@app.route('/secondpage' , methods=['POST'])
def secondpage():
	return render_template('secondpage.html' , returned={'name':myArray})

#to bs ya abhhi sahi hay ? ni bhai ye user id 1 tk e rahy bhai user id b hamein ni chahye wo b ura dein


	
if __name__ == '__main__':
	app.run(debug=True)