from flask import Blueprint,render_template,redirect,request
from function.delete import delete
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

update5 = Blueprint('update_staff',__name__)

def staff_add(request):
    staffId=request.form.get("staff_id")
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    qualification=request.form.get("qualification")
    timing=request.form.get("timing")
    course=request.form.get("course")
    dateOfJoining=request.form.get("date_of_joining")

    with conn.cursor() as cur:
        sql="INSERT into staff (staff_id,first_name,last_name,father_name,mother_name,dob,address,qualification,timing,course,date_of_joining)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (staffId,firstName,lastName,fatherName,motherName,dob,address,qualification,timing,course,dateOfJoining)
        cur.execute(sql,value)
        conn.commit()

        return 1
    

def update_staff(id):
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    qualification=request.form.get("qualification")
    timing=request.form.get("timing")
    course=request.form.get("course")
    dateOfJoining=request.form.get("date_of_joining")

    with conn.cursor() as cur:
        sql="UPDATE staff SET first_name=%s,last_name=%s,father_name=%s,mother_name=%s,dob=%s,address=%s,qualification=%s,timing=%s,course=%s,date_of_joining=%s where staff_id=%s"
        value = (firstName,lastName,fatherName,motherName,dob,address,qualification,timing,course,dateOfJoining,id)
        cur.execute(sql,value)
        conn.commit()

        return 1
    



@update5.route("/staffupdate/<id>", methods=['GET', 'POST'])
def updatestaff(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM staff WHERE staff_id=%s"
            values = (id,)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("staffupdate.html", datas=data)
    if request.method == 'POST':
        status = update_staff(id)
        if status == 1:
            return redirect("/stafftable")
        else:
            return "INVALID"



@update5.route("/stafftable/<param>/<id>")
def  staffdelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/stafftable")