from flask import Blueprint,render_template,redirect,request
from function.students import update_students
from function.delete import conn,delete


students = Blueprint('update_students',__name__)


@students.route("/studentsupdate/<id>", methods=['GET', 'POST'])
def updatestudents(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM students WHERE student_id=%s"
            values = (id,)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("studentsupdate.html", datas=data)
    if request.method == 'POST':
        status = update_students(id)
        if status == 1:
            return redirect("/studentstable")
        else:
            return "INVALID"



@students.route("/studentstable/<param>/<id>")
def  studentsdelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/studentstable")