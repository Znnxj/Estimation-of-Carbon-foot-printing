from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate/<option>')
def calculate(option):
    # Here you would write the code to calculate the carbon footprint based on the selected option
    # This is just a placeholder
    return f"Calculating carbon footprint for option: {option}"

if __name__ == '__main__':
    app.run(debug=True)
