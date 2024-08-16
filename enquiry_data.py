from flask import Blueprint,render_template,redirect,request
from function.enquiry import update_enquiry
from function.delete import conn,delete


enquiry = Blueprint('update_enquiry',__name__)


        
@enquiry.route("/enquiryupdate/<id>" ,methods=['GET','POST'])
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
        

@enquiry.route("/enquirytable/<param>/<id>")
def  enquirydelete(param,id):
   if param=="delete":
        delete("enquiry", "form_id", id)
        return redirect("/enquirytable")