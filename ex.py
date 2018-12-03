from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('quiz-bot.html')

@app.route('/science1', methods=['POST', 'GET'])
def science1():
    return render_template('science1.html')

@app.route('/maths1', methods=['POST', 'GET'])
def maths1():
    return render_template('maths1.html')

@app.route('/history1', methods=['POST', 'GET'])
def history1():
    return render_template('history1.html')

@app.route('/science2', methods=['POST', 'GET'])
def science2():
    return render_template('science2.html')

@app.route('/maths2', methods=['POST', 'GET'])
def maths2():
    return render_template('maths2.html')

@app.route('/history2', methods=['POST', 'GET'])
def history2():
    return render_template('history2.html')

@app.route('/science3', methods=['POST', 'GET'])
def science3():
    return render_template('science3.html')

@app.route('/maths3', methods=['POST', 'GET'])
def maths3():
    return render_template('maths3.html')

@app.route('/history3', methods=['POST', 'GET'])
def history3():
    return render_template('history3.html')

if __name__ == '__main__':
	app.run()
