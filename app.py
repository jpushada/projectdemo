# import the libraries
from flask import Flask, render_template,request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('Student_Marks.html')
@app.route('/submit', methods = ['POST'])
def submit():
    try:
        # Create a dictionary to store all student marks
        student_details = {
            'name':request.form['name'],
            'class': request.form['class'],
            'roll_number': request.form['roll_number'],
            'Maths': request.form['Maths'],
            'Science': request.form['Science'],
            'SocialScience': request.form['SocialScience'],
            'Telugu': request.form['Telugu'],
            'English': request.form['English'],
            'Hindi': request.form['Hindi'],
        }
        # Open CSV file in append mode
        with open("student_marks.csv",'a',newline='') as csvfile:
            fieldnames = ['name','class','roll_number','Maths','Science','SocialScience','Telugu','English','Hindi']

            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(student_details)

        return "Congratulations!! Your Data Submitted Successfully!"
    except Exception as exp:
        return "An Error Occured while submitting your Details"
if __name__ == '__main__':
    app.run(debug=True)