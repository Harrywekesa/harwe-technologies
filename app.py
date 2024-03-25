from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    services_list = ['Software Development', 'Web Design', 'Network Solutions', 'Database Management']
    return render_template('services.html', services=services_list)

if __name__ == '__main__':
    app.run(debug=True)
