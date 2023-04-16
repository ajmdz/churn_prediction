from flask import Flask, request, jsonify
import util

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def test():
    return 'hello'
    
if __name__ == '__main__':
	print("Starting Python Flask Server for Credit Card Churn")
	util.load_saved_artifacts()
	app.run()