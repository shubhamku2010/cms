from flask import redirect,render_template,request
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def enquiry_add(request):
    formId=request.form.get("form_id")
    studentName=request.form.get("student_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    mobile=request.form.get("mobile")
    email=request.form.get("email")
    course=request.form.get("course")
    date=request.form.get("date")

    with conn.cursor() as cur:	
        sql="INSERT into enquiry_forms (form_id, student_name, father_name, mother_name,dob,address,mobile,email,course,date) values(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
        values = (formId, studentName, fatherName, motherName,dob,address,mobile,email,course,date)
        cur.execute(sql,values)
        conn.commit()
        
        return 1    

