from flask import Blueprint,render_template,redirect,request
from function.attendance import attendanceupdate
from function.delete import conn,delete

attendance = Blueprint('update_attendance',__name__)


@attendance.route("/attendanceupdate/<id>" ,methods=['GET','POST'])
def updateattendence(id):
    if request.method=='GET':
        with conn.cursor() as cur:
            sql="select * from attendance where attendance_id=%s"
            values=(id)
            cur.execute(sql,values)
            data=cur.fetchone()
        return render_template("attendanceupdate.html",datas=data)
       
    status=attendanceupdate(id)
    if status==1:
               
        return redirect("/attendancetable") 
    

    else:   
        return "INVALID"



@attendance.route("/attendancetable/<param>/<id>")
def attendancedelete(param, id):
    if param=="delete":
        delete("attendance", "attendance_id ", id)
        return redirect("/attendancetable")
    