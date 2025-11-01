from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# مسار ملف بيانات الطلبة
DATA_FILE = "students_data.csv"

# دالة لقراءة بيانات الطلبة
def read_students():
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame(columns=["رقم_القيد", "الاسم_الكامل", "التخصص", "الفصل", "المعدل", "الحالة"])
    return pd.read_csv(DATA_FILE)

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html")

# صفحة تسجيل دخول الطالب
@app.route("/student", methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        df = read_students()
        student = df[df["رقم_القيد"] == int(student_id)] if not df.empty else None
        if student is not None and not student.empty:
            return render_template("student_results.html", student=student.to_dict(orient="records")[0])
        else:
            return render_template("student_login.html", error="رقم القيد غير موجود.")
    return render_template("student_login.html")

# صفحة تسجيل دخول الإدارة
@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "1234":
            return redirect(url_for("admin_dashboard"))
        else:
            return render_template("admin_login.html", error="بيانات الدخول غير صحيحة.")
    return render_template("admin_login.html")

# لوحة الإدارة
@app.route("/dashboard")
def admin_dashboard():
    df = read_students()
    return render_template("admin_dashboard.html", students=df.to_dict(orient="records"))

# إضافة طالب جديد
@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form.get("name")
    student_id = request.form.get("student_id")
    df = read_students()
    new_row = {"رقم_القيد": student_id, "الاسم_الكامل": name, "التخصص": "", "الفصل": "", "المعدل": "", "الحالة": ""}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    return redirect(url_for("admin_dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
