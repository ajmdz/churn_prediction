from flask import Flask, request, jsonify, render_template
import util
import webbrowser
import os

app = Flask(__name__, 
	template_folder=os.path.abspath('../client'),
	static_url_path='/',
	static_folder=os.path.abspath('../client'))

@app.route('/predict_churn', methods=['POST'])
def predict_churn():
	x = []
	x.append(int(request.form['total_transaction_on_account']))
	x.append(int(request.form['total_transaction_amount']))
	x.append(int(request.form['total_revolving_balance']))
	x.append(float(request.form['total_transactions_change_q4-q1']))
	x.append(float(request.form['total_number_of_accounts']))
	x.append(float(request.form['total_amount_change_q4-q1']))
	x.append(float(request.form['average utilization ratio']))
    
	response = jsonify({'churn_proba': util.get_churn_proba(*x)})
	response.headers.add('Access-Control-Allow-Origin','*')

	return response

@app.route('/')
def home():
	return render_template('index.html')
    
if __name__ == '__main__':
	print("Starting Python Flask Server for Credit Card Churn")
	util.load_saved_artifacts()
	webbrowser.open('http://localhost:5000/')
	app.run()