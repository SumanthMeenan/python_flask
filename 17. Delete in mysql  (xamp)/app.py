from flask import Flask, render_template, request
flask_app = Flask(__name__)

# pip install mysql-connector
import mysql.connector


@flask_app.route("/home", methods = ["GET", "POST"])
def home():

    db_instance = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "employee_data"
    )

    db_connector = db_instance.cursor()

    if request.method == "POST":

        employee_form_data = request.form.to_dict()

        name  = employee_form_data['person_name']

        # db_connector.execute(" insert into employee_details (Name, Email, Company_Id, DOB, Salary) values("name","email","company_id","dob","salary")
        db_connector.execute(" delete from employee_details where Name = '"+name+"')

        db_instance.commit()
        db_connector.close()

        return "Deleted record with name = {}".format(name)


    return render_template("index.html")


if __name__ == "__main__":
    flask_app.run(debug=True)


# Upload csv file, audio file, text file, images,  through UI, load it in app.py, upload this dataframe to database