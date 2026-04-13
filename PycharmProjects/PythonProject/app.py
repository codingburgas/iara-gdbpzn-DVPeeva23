from flask import Flask, render_template, request, redirect

app = Flask(__name__)

signals = []

@app.route('/')
def home():
    return render_template('index.html', signals=signals)

@app.route('/add', methods=['POST'])
def add_signal():
    location = request.form.get('location')
    signals.append(location)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)