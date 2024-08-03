from flask import Blueprint,render_template,redirect,request
from function.delete import delete
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

update1 = Blueprint('update_attendance',__name__)




def attendance_add(req):
    attendeeType=req.form.get("attendee_type")
    attendee_id=int(req.form.get("attendee_id"))
    type=req.form.get("type")
    flag=0


    current_time = datetime.datetime.now()

    with conn.cursor() as cur:
        if attendeeType == "STUDENT":
            sql="select * from students where student_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1
        if attendeeType == "TEACHER":
            sql="select * from teachers where teacher_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1
        
        if attendeeType == "STAFF":
            sql="select * from staff where staff_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1
    
  
    if flag==1:
        with conn.cursor() as cur:
            if type=="in":
                sql="""INSERT INTO attendance(attendee_type,attendee_id,timing_in) 
                        Values(%s,%s,%s)"""
                values=(attendeeType,attendee_id,current_time)
            else:
                sql="""INSERT INTO attendance(attendee_type,attendee_id,timing_out) 
                        Values(%s,%s,%s)"""
                values=(attendeeType,attendee_id,current_time)
                
            cur.execute(sql,values)
            conn.commit()
            
        return 1
    else:
        return 0
    




def attendanceupdate(id):
   

    
    
    attendeeType=request.form.get("attendeeType")
    attendee_id=int(request.form.get("attendeeId"))
    type=request.form.get("type")
    flag=0

    time=datetime.datetime.now()

    with conn.cursor() as cur:
        if attendeeType == "student":
            sql="select * from students where student_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    with conn.cursor() as cur:
        if attendeeType == "teacher":
            sql="select * from teachers where teacher_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    with conn.cursor() as cur:
        if attendeeType == "staff":
            sql="select * from staff where staff_id =%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    if flag==1:
        if type=="in":
            with conn.cursor() as cur:
                sql="""UPDATE  attendance SET attendee_type=%s,attendee_id=%s,timing_in=%s WHERE attendance_id=%s"""
                values=(attendeeType,attendee_id,time,id)
                cur.execute(sql,values)
                conn.commit()

        else:
            with conn.cursor() as cur:
                sql="""UPDATE attendance SET attendee_type=%s,attendee_id=%s,timing_out=%s  WHERE attendance_id=%s"""
                values=(attendeeType,attendee_id,time,id)
                cur.execute(sql,values)
                conn.commit()
        return 1


    else:
        return 0
    


@update1.route("/attendanceupdate/<id>" ,methods=['GET','POST'])
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



@update1.route("/attendancetable/<param>/<id>")
def attendancedelete(param, id):
    if param=="delete":
        delete("attendance", "attendance_id ", id)
        return redirect("/attendancetable")
