import csv
import json
import os
import shutil
from datetime import datetime

# ===================== File Names =====================
STUDENTS_FILE = "students.csv"
COURSES_FILE = "courses.json"
ENROLLMENTS_FILE = "enrollments.csv"
LOG_FILE = "app.log"

# ===================== Data Structures =====================
students = {}            # dict[int, dict]
courses = {}             # dict[str, dict]
enrollments = []         # list[dict]

# ===================== Logging =====================
def log_action(action: str):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {action}\n")

# ===================== File I/O =====================
def load_students():
    global students
    if not os.path.exists(STUDENTS_FILE):
        return
    try:
        with open(STUDENTS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    students[int(row["student_id"])] = {
                        "name": row["full_name"],
                        "year": int(row["year"]),
                        "gpa": float(row["gpa"])
                    }
                except Exception:
                    continue
    except FileNotFoundError:
        pass

def load_courses():
    global courses
    if not os.path.exists(COURSES_FILE):
        return
    try:
        with open(COURSES_FILE) as f:
            courses = json.load(f)
            for c in courses.values():
                c.setdefault("enrolled", set())
    except Exception:
        pass

def load_enrollments():
    global enrollments
    if not os.path.exists(ENROLLMENTS_FILE):
        return
    try:
        with open(ENROLLMENTS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    enrollments.append({
                        "student_id": int(row["student_id"]),
                        "course_code": row["course_code"],
                        "grade": float(row["grade"]) if row["grade"] else None
                    })
                except Exception:
                    continue
    except FileNotFoundError:
        pass

def save_students():
    with open(STUDENTS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["student_id", "full_name", "year", "gpa"])
        writer.writeheader()
        for sid, data in students.items():
            writer.writerow({
                "student_id": sid,
                "full_name": data["name"],
                "year": data["year"],
                "gpa": data["gpa"]
            })
    backup_file = f"students_{datetime.now().strftime('%Y%m%d%H%M')}.csv"
    shutil.copy(STUDENTS_FILE, backup_file)

def save_courses():
    for c in courses.values():
        if isinstance(c.get("enrolled"), set):
            c["enrolled"] = list(c["enrolled"])
    with open(COURSES_FILE, "w") as f:
        json.dump(courses, f, indent=2)
    for c in courses.values():
        if isinstance(c.get("enrolled"), list):
            c["enrolled"] = set(c["enrolled"])

def save_enrollments():
    with open(ENROLLMENTS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["student_id", "course_code", "grade"])
        writer.writeheader()
        for e in enrollments:
            writer.writerow(e)

def save_all():
    save_students()
    save_courses()
    save_enrollments()
    log_action("Saved and backed up data")

# ===================== Features =====================
def list_students():
    print("\n--- Students ---")
    for sid, data in students.items():
        print(f"{sid}: {data['name']} (Year {data['year']}, GPA {data['gpa']})")

def list_courses():
    print("\n--- Courses ---")
    for code, c in courses.items():
        print(f"{code}: {c['title']} ({c['credits']} credits, cap {c['capacity']})")

def add_student():
    sid = int(input("Enter ID: "))
    if sid in students:
        print("Student already exists.")
        return
    name = input("Enter name: ")
    year = int(input("Enter year: "))
    gpa = float(input("Enter GPA: "))
    students[sid] = {"name": name, "year": year, "gpa": gpa}
    log_action(f"Added student {sid}")

def add_course():
    code = input("Enter course code: ")
    if code in courses:
        print("Course already exists.")
        return
    title = input("Enter title: ")
    credits = int(input("Credits: "))
    cap = int(input("Capacity: "))
    prereqs = input("Prereqs (comma separated): ").split(",")
    prereqs = [p.strip() for p in prereqs if p.strip()]
    courses[code] = {"title": title, "credits": credits, "capacity": cap, "prereqs": prereqs, "enrolled": set()}
    log_action(f"Added course {code}")

def enroll_student():
    sid = int(input("Student ID: "))
    code = input("Course code: ")
    if sid not in students or code not in courses:
        print("Invalid student or course.")
        return
    course = courses[code]
    if len(course["enrolled"]) >= course["capacity"]:
        print("Course full.")
        return
    if (sid, code) in [(e["student_id"], e["course_code"]) for e in enrollments]:
        print("Already enrolled.")
        return
    # check prereqs
    for pre in course["prereqs"]:
        if all(e["course_code"] != pre for e in enrollments if e["student_id"] == sid):
            print("Missing prerequisite.")
            return
    enrollments.append({"student_id": sid, "course_code": code, "grade": None})
    course["enrolled"].add(sid)
    log_action(f"Enrolled {sid} in {code}")

def record_grade():
    sid = int(input("Student ID: "))
    code = input("Course code: ")
    for e in enrollments:
        if e["student_id"] == sid and e["course_code"] == code:
            e["grade"] = float(input("Enter grade: "))
            log_action(f"Updated grade for {sid} in {code}")
            return
    print("Enrollment not found.")

def transcript():
    sid = int(input("Student ID: "))
    if sid not in students:
        print("Student not found.")
        return
    print(f"Transcript for {students[sid]['name']}: ")
    total_points = 0
    total_credits = 0
    for e in enrollments:
        if e["student_id"] == sid:
            code = e["course_code"]
            grade = e["grade"]
            print(f"{code} - {courses[code]['title']} : {grade}")
            if grade is not None:
                total_points += grade
                total_credits += 1
    if total_credits > 0:
        gpa = total_points / total_credits
        print(f"Calculated GPA: {gpa:.2f}")

def search():
    q = input("Enter name or course code: ").lower()
    print("Students:")
    for sid, s in students.items():
        if q in s["name"].lower():
            print(f"{sid}: {s['name']}")
    print("Courses:")
    for code in courses:
        if q in code.lower():
            print(f"{code}: {courses[code]['title']}")

def analytics():
    print("1. Top N students by GPA")
    print("2. Course fill rates")
    print("3. Average grade per course")
    choice = input("Choose: ")
    if choice == "1":
        n = int(input("Enter N: "))
        top = sorted(students.items(), key=lambda x: x[1]["gpa"], reverse=True)[:n]
        for sid, data in top:
            print(f"{data['name']} GPA {data['gpa']}")
    elif choice == "2":
        for code, c in courses.items():
            fill = len(c["enrolled"]) / c["capacity"] * 100
            print(f"{code}: {fill:.1f}% full")
            if fill > 90:
                print("Warning: over 90% capacity!")
    elif choice == "3":
        for code in courses:
            grades = [e["grade"] for e in enrollments if e["course_code"] == code and e["grade"] is not None]
            if grades:
                avg = sum(grades) / len(grades)
                print(f"{code}: avg grade {avg:.2f}")

# ===================== Main Loop =====================
def main():
    load_students()
    load_courses()
    load_enrollments()
    while True:
        print("\nCampus Registrar Menu:")
        print("1. List students/courses")
        print("2. Add student")
        print("3. Add course")
        print("4. Enroll student")
        print("5. Record/update grade")
        print("6. Show transcript")
        print("7. Search")
        print("8. Save & backup data")
        print("9. Analytics")
        print("10. Exit")
        choice = input("Enter choice: ")
        match choice:
            case "1":
                list_students(); list_courses()
            case "2":
                add_student()
            case "3":
                add_course()
            case "4":
                enroll_student()
            case "5":
                record_grade()
            case "6":
                transcript()
            case "7":
                search()
            case "8":
                save_all()
            case "9":
                analytics()
            case "10":
                save_all(); break
            case _:
                print("Invalid choice.")

if __name__== "__main__":
             main()