from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        file = database.write(f'{data}\n')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        sub = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, sub, message, ])


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)

        except:
            return 'did not connect to the database'

        return redirect('/thank.html')
    else:
        return 'something went wrong'

# app.run(debug=True) #, host='0.0.0.0', port=5000)
