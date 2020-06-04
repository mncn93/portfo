from flask import Flask,render_template, url_for,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_data_to_file(input_data):
    with open('database.txt',mode='a') as database:
        email = input_data['email']
        subject = input_data['subject']
        message = input_data['message']
        database.write(f'\nemail={email}, subject={subject}, message={message}')

def write_data_to_csv(input_data):
    with open('database2.csv',mode='a') as database2:
        email = i   nput_data["email"]
        subject = input_data["subject"]
        message = input_data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data_to_file(data)
        write_data_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again!!'
