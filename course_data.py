from flask import Blueprint,render_template,redirect,request
from function.courses import update_courses
from function.delete import conn,delete


course = Blueprint('update_courses',__name__)
    


@course.route("/coursesupdate/<id>" ,methods=['GET','POST'])
def updatecourses(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM courses WHERE course_id=%s"
            values = (id)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("coursesupdate.html", datas=data)
    if request.method == 'POST':
        status = update_courses(id)
        if status == 2:
            return redirect("/coursestable")
        else:
            return "INVALID"


@course.route("/coursestable/<param>/<id>")
def  coursesdelete(param,id):
   if param=="delete":
        delete("courses", "course_id ", id)
        return redirect("/coursestable")
    