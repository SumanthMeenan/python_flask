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

        company_id  = employee_form_data['id']

        # db_connector.execute(" insert into employee_details (Name, Email, Company_Id, DOB, Salary) values("name","email","company_id","dob","salary")
        db_connector.execute(" select Name, Email, Company_Id, DOB, Salary from employee_data where Company_Id = '"+company_id+"')
        id_based = db_connector.fetchone()

        db_instance.commit()
        db_connector.close()

        return render_template("employees.html", id_output = id_based)


    return render_template("index.html")


if __name__ == "__main__":
    flask_app.run(debug=True)


# Upload csv file, audio file, text file, images,  through UI, load it in app.py, upload this dataframe to database