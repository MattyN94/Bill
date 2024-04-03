from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/split', methods=['POST'])
def split_bill():
    try:
        bill_total = request.form['bill_total']
        people = int(request.form['people'])
        tip_percentage = float(request.form['tip_percentage'])

        percentage_decimal = tip_percentage / 100
        tip_total = float(bill_total) * percentage_decimal
        bill_total = float(bill_total) + tip_total
        cost_per_person = bill_total / people

        bill_total = round(bill_total, 2)
        cost_per_person = round(cost_per_person, 2)

        return render_template('result.html', bill_total=bill_total, cost_per_person=cost_per_person)

    except ValueError:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run(debug=True)
