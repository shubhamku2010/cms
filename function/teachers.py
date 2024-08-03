from flask import Blueprint,render_template,redirect,request
from function.delete import delete
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

update7 = Blueprint('update_teachers',__name__)



def teachers_add(request):
    teacherId=request.form.get("teacher_id")
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    salary=request.form.get('salary')
    qualification=request.form.get('qualification')
    timing=request.form.get('timing')
    course=request.form.get('course')
    dateOfJoining=request.form.get('date_of_joining')
    

    

    with conn.cursor() as cur:
        sql="INSERT into teachers (teacher_id,first_name,last_name,father_name,mother_name,dob,address,salary,qualification,timing,course,date_of_joining)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (teacherId,firstName,lastName,fatherName,motherName,dob,address,salary,qualification,timing,course,dateOfJoining)
        cur.execute(sql,value)
        conn.commit()

        return 1
    

def update_teachers(id):
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    salary=request.form.get('salary')
    qualification=request.form.get('qualification')
    timing=request.form.get('timing')
    course=request.form.get('course')
    dateOfJoining=request.form.get('date_of_joining')
    

    

    with conn.cursor() as cur:
        sql="UPDATE teachers SET first_name=%s,last_name=%s,father_name=%s,mother_name=%s,dob=%s,address=%s,salary=%s,qualification=%s,timing=%s,course=%s,date_of_joining=%s WHERE teacher_id=%s"
        value = (firstName,lastName,fatherName,motherName,dob,address,salary,qualification,timing,course,dateOfJoining,id)
        cur.execute(sql,value)
        conn.commit()

        return 1
    

@update7.route("/teachersupdate/<id>", methods=['GET', 'POST'])
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


@update7.route("/teacherstable/<param>/<id>")
def  teachersdelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/teacherstable")