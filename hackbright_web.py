"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""    

    html = render_template("student_search.html")

    return html


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github) 

    rows = hackbright.get_grades_by_github(github)



    html = render_template("student_info.html",
                               first=first,
                               last=last,
                               github=github,
                               rows=rows)

    return html


@app.route("/student-form")
def student_form():
    """Display form."""

    html = render_template("student_form.html")

    return html


@app.route("/student-add", methods=['POST'])    
def student_add():
    """Add a student."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    github = request.form.get("github")

    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("student_acknowledge.html", first_name=first_name, 
        last_name=last_name, github=github)

    return html

@app.route("/projects/<project>")
def describe_project():
    """Gives description of project."""

    title, description, max_grade = hackbright.get_project_by_title(project)

    html = render_template("project.html", title=title, description=description, 
        max_grade=max_grade)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
