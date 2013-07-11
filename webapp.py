import hackbright_app

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find_student")
def get_github():
    return render_template("get_github.html")


@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    rows = hackbright_app.show_grade(student_github) # list of tuples
    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2],
                                                projects=rows)
    return html

@app.route("/project")
def get_project_grades():
    hackbright_app.connect_to_db()
    project_title = request.args.get("title")
    rows = hackbright_app.all_project_grades(project_title) # returns list
    html = render_template("project.html", students=rows)
    return html

@app.route("/add_student")
def add_new_student():
    return render_template("add_student.html")


@app.route("/make_student")
def create_new_student():
    #####################################################3
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    github = request.args.get("github")
    hackbright_app.connect_to_db()
    if hackbright_app.make_new_student(first_name, last_name, github):
        html = render_template("new_student.html", first_name=first_name,
                                                last_name=last_name,
                                                github=github)
    return html


@app.route("/add_project")
def add_new_project():
    return render_template("add_project.html")


@app.route("/make_project")
def create_new_project():
    project_title = request.args.get("title")
    description = request.args.get("description")
    max_grade = request.args.get("max_grade")
    hackbright_app.connect_to_db()
    if hackbright_app.add_project(project_title, description, max_grade):
        html = render_template("new_project.html", title=project_title,
                                                description=description,
                                                max_grade=max_grade)
    return html


@app.route("/add_grade")
def add_new_grade():
    # Get student_github, project_title, and grade from Grades 
    return render_template("add_grade.html")


@app.route("/new_grade")
def new_grade():
    student_github = request.args.get("github")
    project_title = request.args.get("project")
    grade = request.args.get("grade")
    hackbright_app.connect_to_db()
    if hackbright_app.give_grade(student_github, project_title, grade):
        html = render_template("new_grade.html", github=student_github,
                                                title=project_title,
                                                grade=grade)
    return html




if __name__ == "__main__":
    app.run(debug = True)
