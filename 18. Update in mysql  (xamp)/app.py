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

        name        = employee_form_data['person_name']
        email       = employee_form_data['mail']
        company_id  = employee_form_data['id']
        salary      = int(employee_form_data["ctc"])
        dob         = employee_form_data["dob"]

        # db_connector.execute(" insert into employee_details (Name, Email, Company_Id, DOB, Salary) values("name","email","company_id","dob","salary")
        db_connector.execute(" update employee_data set Name=%s, Email=%s, Company_Id=%s, DOB=%s, Salary=%s where Company_Id = %s", (name, email, company_id, salary, dob))

        db_instance.commit()
        db_connector.close()

        return "Updated my Database"


    return render_template("index.html")


if __name__ == "__main__":
    flask_app.run(debug=True)


# Upload csv file, audio file, text file, images,  through UI, load it in app.py, upload this dataframe to database