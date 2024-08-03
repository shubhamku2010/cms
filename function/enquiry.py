from flask import Blueprint,render_template,redirect,request
from function.delete import delete
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

update3 = Blueprint('update_enquiry',__name__)



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
    

def update_enquiry(id):
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
        sql="UPDATE enquiry_forms SET student_name=%s, father_name=%s, mother_name=%s,dob=%s,address=%s,mobile=%s,email=%s,course=%s,date=%s where form_id=%s"
        values = (studentName, fatherName, motherName,dob,address,mobile,email,course,date,id)
        cur.execute(sql,values)
        conn.commit()
        
        return 1 
    

        
@update3.route("/enquiryupdate/<id>" ,methods=['GET','POST'])
def updateenquiry(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM enquiry_forms WHERE form_id=%s"
            values = (id)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("enquiryupdate.html", datas=data)
    if request.method == 'POST':
        status = update_enquiry(id)
        if status == 1:
            return redirect("/enquirytable")
        else:
            return "INVALID"
        

@update3.route("/enquirytable/<param>/<id>")
def  enquirydelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/enquirytable")