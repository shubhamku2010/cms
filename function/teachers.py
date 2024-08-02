from flask import redirect,render_template,request
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

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