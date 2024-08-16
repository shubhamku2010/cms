from flask import redirect,render_template,request
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

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
    


