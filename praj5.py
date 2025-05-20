from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        option = request.form['option']
        return calculate(option)
    return render_template('index.html')

def calculate(option):
    # Here you would write the code to calculate the carbon footprint based on the selected option
    # This is just a placeholder
    return f"Calculating carbon footprint for option: {option}"

if __name__ == '__main__':
    app.run(debug=True)
