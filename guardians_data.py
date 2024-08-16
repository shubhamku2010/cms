from flask import Blueprint,render_template,redirect,request
from function.guardians import update_guardians
from function.delete import conn,delete

guardians = Blueprint('update_guardians',__name__)

        

@guardians.route("/guardiansupdate/<id>", methods=['GET', 'POST'])
def updateguardians(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM guardians WHERE guardian_id=%s"
            values = (id,)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("guardiansupdate.html", datas=data)
    if request.method == 'POST':
        status = update_guardians(id)
        if status == 1:
            return redirect("/guardianstable")
        else:
            return "INVALID"



@guardians.route("/guardianstable/<param>/<id>")
def  guardiansdelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/guardianstable")