# from flask import Flask,redirect,url_for,render_template,request
# import pymysql


# conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

# app=Flask(__name__)



# @app.route('/attendance-form')
# def attendance():
#     return render_template('attendance.html')

# @app.route("/attendance", methods=["POST"])
# def submit_attendance():
#     attendanceId=request.form.get("attendance_id")
#     attendanceType=request.form.get("attendee_type")
#     attendeeId=request.form.get("attendee_id")
#     timeIn=request.form.get("timing_in")
#     timeOut=request.form.get("timing_out")
#     attendanceDate=request.form.get("attendance_date")
    
#     return f'{attendanceId} ,\t{attendanceType} ,\t{attendeeId} ,\t{timeIn} ,\t{timeOut} ,\t{attendanceDate}'



# @app.route('/classes-form')
# def classes():
#     return render_template('classes.html')

# @app.route("/classes", methods=["POST"])
# def submit_classes():
#     classId=request.form.get("class_id")
#     courseName=request.form.get("course_name")
#     startTime=request.form.get("start_time")
#     endTime=request.form.get("end_time")
#     return f'{classId} ,\t{courseName} ,\t{startTime} ,\t{endTime}'



# @app.route('/course-form')
# def course():
#     return render_template('course.html')

# @app.route("/course", methods=["POST"])
# def submit_courses():
#     courseId=request.form.get("course_id")
#     name=request.form.get("name")
#     duration=request.form.get("duration")
#     fees=request.form.get("fees")
#     return f'{courseId} ,\t{name} ,\t{duration} ,\t{fees}'



# @app.route('/enquiry-form')
# def enquiry():
#     return render_template('enquiry.html')

# @app.route("/enquiry", methods=["POST"])
# def submit_enquiry():
#     formId=request.form.get("form_id")
#     studentName=request.form.get("student_name")
#     fatherName=request.form.get("father_name")
#     motherName=request.form.get("mother_name")
#     dob=request.form.get("dob")
#     address=request.form.get("address")
#     mobile=request.form.get("mobile")
#     email=request.form.get("email")
#     course=request.form.get("course")
#     date=request.form.get("date")
#     return f'{formId} ,\t{studentName} ,\t{fatherName} ,\t{motherName} ,\t{dob} ,\t{address} ,\t{mobile} ,\t{email} ,\t{course} ,\t{date}'



# @app.route('/gurdians-form')
# def gurdians():
#     return render_template('gurdians.html')

# @app.route("/gurdians", methods=["POST"])
# def submit_gurdians():
#     gurdianId=request.form.get("gurdian_id")
#     studentId=request.form.get("student_id")
#     fatherName=request.form.get("father_name")
#     motherName=request.form.get("mother_name")
#     address=request.form.get("address")
#     mobile=request.form.get("mobile")
#     email=request.form.get("email")
#     return f'{gurdianId} ,\t{studentId} ,\t{fatherName} ,\t{motherName} ,\t{address} ,\t{mobile} ,\t{email}'


# @app.route('/staff-form')
# def staff():
#     return render_template('staff.html')

# @app.route("/staff", methods=["POST"])
# def submit_staff():
#     staffId=request.form.get("staff_id")
#     firstName=request.form.get("first_name")
#     lastName=request.form.get("last_name")
#     fatherName=request.form.get("father_name")
#     motherName=request.form.get("mother_name")
#     dob=request.form.get("dob")
#     address=request.form.get("address")
#     qualification=request.form.get("qualification")
#     timing=request.form.get("timing")
#     course=request.form.get("course")
#     dateOfJoining=request.form.get("date_of_joining")
    
#     return f'{staffId} ,\t{firstName} ,\t{lastName} ,\t{fatherName} ,\t{motherName} ,\t{dob} ,\t{address} ,\t{qualification} ,\t{timing} ,\t{course} ,\t{dateOfJoining}'

# @app.route('/students-form')
# def students():
#     return render_template('students.html')

# @app.route("/students", methods=["POST"])
# def submit_students():
#     studentId=request.form.get("student_id")
#     firstName=request.form.get("first_name")
#     lastName=request.form.get("last_name")
#     fatherName=request.form.get("father_name")
#     motherName=request.form.get("mother_name")
#     dob=request.form.get("dob")
#     address=request.form.get("address")
#     course=request.form.get("course")
#     mobile=request.form.get("mobile")
#     email=request.form.get("email")
#     photo = request.files['photo']
#     photo.save('image/ ' + photo.filename)
#     path='image/ ' + photo.filename

#     return f'{studentId} ,\t{firstName} ,\t{lastName} ,\t{fatherName} ,\t{motherName} ,\t{dob} ,\t{address} ,\t{mobile} ,\t{email} ,\t{course} ,\t{photo}'  



# @app.route('/teachers-form')
# def teachers():
#     return render_template('teachers.html')


# @app.route('/teachers', methods=["POST"])
# def submit_teachers():
#     teacherId=request.form.get("teacher_id")
#     firstName=request.form.get("first_name")
#     lastName=request.form.get("last_name")
#     fatherName=request.form.get("father_name")
#     motherName=request.form.get("mother_name")
#     dob=request.form.get("dob")
#     address=request.form.get("address")
#     salary=request.form.get('salary')
#     qualification=request.form.get('qualification')
#     timing=request.form.get('timing')
#     course=request.form.get('course')
#     dateOfJoining=request.form.get('date_of_joining')


#     return f'{teacherId} ,\t{firstName} ,\t{lastName} ,\t{fatherName} ,\t{motherName} ,\t{dob} ,\t{address} ,\t{salary} ,\t{qualification} ,\t{timing} ,\t{course} ,\t{dateOfJoining} '


# if __name__=='__main__':
#     app.run(debug=True)