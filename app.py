# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/estate')
def estate():
    # You can replace this with logic to fetch and display real estate pictures
    estate_pics = [
        'pic1.jpg',
        'pic2.jpg',
        'pic3.jpg',
    ]
    return render_template('estate.html', estate_pics=estate_pics)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
