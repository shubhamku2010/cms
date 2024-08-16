from flask import Blueprint,render_template,redirect,request
from function.teachers import update_teachers
from function.delete import conn,delete

teachers = Blueprint('update_teachers',__name__)



@teachers.route("/teachersupdate/<id>", methods=['GET', 'POST'])
def updateteachers(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM teachers WHERE teacher_id=%s"
            values = (id,)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("teachersupdate.html", datas=data)
    if request.method == 'POST':
        status = update_teachers(id)
        if status == 1:
            return redirect("/teacherstable")
        else:
            return "INVALID"


@teachers.route("/teacherstable/<param>/<id>")
def  teachersdelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/teacherstable")