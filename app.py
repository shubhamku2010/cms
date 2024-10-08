from flask import Flask,redirect,url_for,render_template,request
import pymysql
import datetime
from function.attendance import attendance_add
from function.enquiry import enquiry_add
from function.courses import courses_add
from function.guardians import guardian_add
from function.staff import staff_add
from function.students import students_add
from function.teachers import teachers_add
from attendance_data import attendance
from course_data import course
from enquiry_data import enquiry
from guardians_data import guardians
from staff_data import staff
from students_data import students
from teachers_data import teachers



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')


app=Flask(__name__)
app.register_blueprint(attendance)
app.register_blueprint(course)
app.register_blueprint(enquiry)
app.register_blueprint(guardians)
app.register_blueprint(staff)
app.register_blueprint(students)
app.register_blueprint(teachers)





@app.route('/')
def base():
    return render_template('base.html')

@app.route('/attendance-form')
def attendance():
    return render_template('attendance.html')

@app.route("/attendance", methods=["POST"])
def submit_attendance():
    status = attendance_add(request)
    if status == 1:
        
        return redirect("/attendancetable")
    
    else:
        return "invalid"

  
    
    



@app.route('/courses-form')
def courses():
    return render_template('courses.html')

@app.route("/courses", methods=["POST"])
def submit_courses():
    status = courses_add(request)
    if status == 1:
        
        return redirect("/coursestable")
    
    else:
        return "invalid"   

    



@app.route('/enquiry-form')
def enquiry():
    return render_template('enquiryforms.html')

@app.route("/enquiry", methods=["POST"])
def submit_enquiry():
    status=enquiry_add(request)
    if status==1:
        return redirect("/enquirytable")
    else:
        return "invalid" 



@app.route('/guardians-form')
def gurdians():
    return render_template('guardians.html')

@app.route("/gurdians", methods=["POST"])
def submit_gurdians():
    status=guardian_add(request)
    if status==1:
        return redirect("/gurdianstable")
    else:
        return "invalid" 

    


@app.route('/staff-form')
def staff():
    return render_template('staff.html')

@app.route("/staff", methods=["POST"])
def submit_staff():
    status=staff_add(request)
    if status==1:
        return redirect('/stafftable')
    else:
        return "invalid" 
    
    


@app.route('/students-form')
def students():
    return render_template('students.html')

@app.route("/students", methods=["POST"])
def submit_students():
    status=students_add(request)
    if status==1:
        return redirect("/studentstable") 
    else:
        return "invalid" 
    

    



@app.route('/teachers-form')
def teachers():
    return render_template('teachers.html')


@app.route('/teachers', methods=["POST"])
def submit_teachers():
    status=teachers_add(request)
    if status==1:
        return redirect("/teacherstable")
    else:
        return "invalid" 


    
    

@app.route("/attendancetable")
def attendancetable():
    with conn.cursor() as cur:
        sql = "select * from attendance"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("attendancetable.html",datas=data)







@app.route("/coursestable")
def coursestable():
    with conn.cursor() as cur:
        sql = "select * from courses"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("coursestable.html" , datas=data)



@app.route("/enquirytable")
def enquirytable():
    with conn.cursor() as cur:
        sql = "select * from enquiry_forms"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("enquirytable.html" , datas=data)


@app.route("/guardianstable")
def gurdianstable():
    with conn.cursor() as cur:
        sql = "select * from guardians"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("guardianstable.html" , datas=data)


@app.route("/stafftable")
def stafftable():
    with conn.cursor() as cur:
        sql = "select * from staff"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("stafftable.html" , datas=data)


@app.route("/studentstable")
def studentstable():
    with conn.cursor() as cur:
        sql = "select * from students"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("studentstable.html" , datas=data)


@app.route("/teacherstable")
def teacherstable():
    with conn.cursor() as cur:
        sql = "select * from teachers"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("teacherstable.html" , datas=data)



if __name__ == "__main__":
    app.run(debug=True)