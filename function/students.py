from flask import redirect,render_template,request
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def students_add():
    studentId=request.form.get("student_id")
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    course=request.form.get("course")
    mobile=request.form.get("mobile")
    email=request.form.get("email")
    photo = request.files['photo']
    photo.save('image/ ' + photo.filename)
    path='image/ ' + photo.filename

    with conn.cursor() as cur:
        sql="INSERT into students (student_id, first_name, last_name, father_name, mother_name, dob, address, course, mobile, email, photo) values(%s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s)"
        values = (studentId, firstName, lastName, fatherName, motherName, dob, address, course, mobile, email, path)
        cur.execute(sql,values)
        conn.commit()
        return 1
    