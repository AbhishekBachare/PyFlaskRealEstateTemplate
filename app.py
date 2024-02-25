from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/estate')
def estate():
    estate_pics = [
        'static/pics/pic1.png',
        'static/pics/pic2.png',
        'static/pics/pic3.png',
    ]
    return render_template('estate.html', estate_pics=estate_pics)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
