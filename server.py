from flask import Flask, render_template, request, redirect # type: ignore
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

# static type website uRL
# @app.route('/about.html')
# def about_page():
#     return render_template('about.html')

#dynamically get website URL
@app.route('/<string:page_route>')
def web_page(page_route):
    return render_template(page_route)

#store form data in local text file
def fileDataBase(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')
        
# store form data in csv file
def csv_file_database(data):
    #newline='', this alwasy write our file into new line
     with open('database.csv', mode='a', newline='') as csv_database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        #delimiter=',' put comma each title of this 'email,subject,message'
        csv_file = csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])

        
#form data get
@app.route('/submit-form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        try:
            # we can recieve formd data using this
            # email = request.form['email']
            # subject = request.form['subject']
            # message = request.form['message']
            
            # we can directly change form data into dictionary(object)
            formData = request.form.to_dict()
            print(formData)
            # fileDataBase(formData)
            csv_file_database(formData)
            
            # print(formData.get('email'))# specific field
            return redirect('/thankyou.html')
        except: 
            return 'Not save to csv something error'
    else:
        return 'something error try again'