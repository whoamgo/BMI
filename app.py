from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 25:
        status = "Normal weight"
    elif 25 <= bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return render_template('result.html', bmi=round(bmi, 2), status=status)

if __name__ == '__main__':
    app.run(debug=True)
