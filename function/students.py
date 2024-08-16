from flask import redirect,render_template,request
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def students_add(request):
    studentId = request.form.get("student_id")
    firstName = request.form.get("first_name")
    lastName = request.form.get("last_name")
    fatherName = request.form.get("father_name")
    motherName = request.form.get("mother_name")
    dob = request.form.get("dob")
    address = request.form.get("address")
    course = request.form.get("course")
    mobile = request.form.get("mobile")
    email = request.form.get("email")
    
    # Handle photo upload
    photo = request.files.get('photo')  # Use .get() to avoid KeyError if no file is uploaded
    if photo:  # Check if a photo was uploaded
        photo.save('image/' + photo.filename.strip())  # Remove any accidental spaces in the filename
        path = 'image/' + photo.filename.strip()
    else:
        path = None  # Handle this case as needed (e.g., if photo is optional)

    with conn.cursor() as cur:
        sql = """INSERT INTO students (student_id, first_name, last_name, father_name, mother_name, dob, address, course, mobile, email, photo) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (studentId, firstName, lastName, fatherName, motherName, dob, address, course, mobile, email, path)
        
        try:
            cur.execute(sql, values)
            conn.commit()
            return 1  
        except Exception as e:
            conn.rollback()  
            return f"An error occurred: {str(e)}"

def update_students(id):
    firstName = request.form.get("first_name")
    lastName = request.form.get("last_name")
    fatherName = request.form.get("father_name")
    motherName = request.form.get("mother_name")
    dob = request.form.get("dob")
    address = request.form.get("address")
    course = request.form.get("course")
    mobile = request.form.get("mobile")
    email = request.form.get("email")
    
   
    photo = request.files.get('photo')
    if photo:  
        photo.save('image/' + photo.filename)
        path = 'image/' + photo.filename
    else:
        path = None  

    with conn.cursor() as cur:

        sql = """UPDATE students 
                 SET first_name=%s, last_name=%s, father_name=%s, mother_name=%s, dob=%s, 
                     address=%s, course=%s, mobile=%s, email=%s, photo=%s 
                 WHERE student_id=%s"""  
        values = (firstName, lastName, fatherName, motherName, dob, address, course, mobile, email, path, id)
        cur.execute(sql, values)
        conn.commit()
        return 1
        