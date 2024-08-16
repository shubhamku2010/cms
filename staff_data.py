from flask import Blueprint,render_template,redirect,request
from function.staff import update_staff
from function.delete import conn,delete


staff = Blueprint('update_staff',__name__)



@staff.route("/staffupdate/<id>", methods=['GET', 'POST'])
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



@staff.route("/stafftable/<param>/<id>")
def  staffdelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/stafftable")