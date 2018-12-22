from flask import Flask, request, render_template

yes_ctr = 0
no_ctr = 0

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('quiz-bot.html')

@app.route('/happy1', methods=['POST', 'GET'])
def happy1():
	global yes_ctr
	yes_ctr = 0
	global no_ctr
	no_ctr = 0
	return render_template('happy1.html')

@app.route('/unhappy1', methods=['POST', 'GET'])
def unhappy1():
	global yes_ctr
	yes_ctr = 0
	global no_ctr
	no_ctr = 0
	return render_template('unhappy1.html')

@app.route('/neutral1', methods=['POST', 'GET'])
def neutral1():
	global yes_ctr
	yes_ctr = 0
	global no_ctr
	no_ctr = 0
	return render_template('neutral1.html')

@app.route('/happy2', methods=['POST', 'GET'])
def happy2():
	text = request.form['happy1ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('happy2.html')

@app.route('/unhappy2', methods=['POST', 'GET'])
def unhappy2():
	text = request.form['unhappy1ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('unhappy2.html')

@app.route('/neutral2', methods=['POST', 'GET'])
def neutral2():
	text = request.form['neutral1ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('neutral2.html')

@app.route('/happy3', methods=['POST', 'GET'])
def happy3():
	text = request.form['happy2ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('happy3.html')

@app.route('/unhappy3', methods=['POST', 'GET'])
def unhappy3():
	text = request.form['unhappy2ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('unhappy3.html')

@app.route('/neutral3', methods=['POST', 'GET'])
def neutral3():
	text = request.form['neutral2ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('neutral3.html')

@app.route('/happy4', methods=['POST', 'GET'])
def happy4():
	text = request.form['happy3ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('happy4.html')

@app.route('/unhappy4', methods=['POST', 'GET'])
def unhappy4():
	text = request.form['unhappy3ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('unhappy4.html')

@app.route('/neutral4', methods=['POST', 'GET'])
def neutral4():
	text = request.form['neutral3ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('neutral4.html')

@app.route('/happy5', methods=['POST', 'GET'])
def happy5():
	text = request.form['happy4ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('happy5.html')

@app.route('/unhappy5', methods=['POST', 'GET'])
def unhappy5():
	text = request.form['unhappy4ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('unhappy5.html')

@app.route('/neutral5', methods=['POST', 'GET'])
def neutral5():
	text = request.form['neutral4ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	return render_template('neutral5.html')

@app.route('/happy6', methods=['POST', 'GET'])
def happy6():
	text = request.form['happy5ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	
	if yes_ctr > no_ctr:
		return ("<body><center><h1>You are feeling happy! :)" + "</h1></center></body>")
	else:
		return ("<body><center><h1>You are not feeling very happy today. But it's okay, there are good days and bad days, so cheer up! :)" + "</h1></center></body>")

@app.route('/unhappy6', methods=['POST', 'GET'])
def unhappy6():
	text = request.form['unhappy5ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1
	
	if yes_ctr > no_ctr:
		return ("<body><center><h1>Don't worry too much. You are happy today :)" + "</h1></center></body>")
	else:
		return ("<body><center><h1>Today is not such a happy day but its okay to feel that way sometimes. Take care :)" + "</h1></center></body>")

@app.route('/neutral6', methods=['POST', 'GET'])
def neutral6():
	text = request.form['neutral5ans']
	global yes_ctr
	global no_ctr
	if text == "yes":
		yes_ctr = yes_ctr + 1
	elif text == "no":
		no_ctr = no_ctr + 1

	if yes_ctr == 3:
		return ("<body><center><h1>You are bending towards happy! :)" + "</h1></center></body>")
	elif yes_ctr == 2:
		return ("<bpdy><center><h1>You are bending towards unhappy! :(" + "</h1></center></body>")
	else:
		return ("<body><center><h1>You are not neutral today. Take the happy quiz if you feel you are happy or the unhappy quiz if you feel unhappy! :)" + "</h1></center></body>")



if __name__ == '__main__':
	app.run()
