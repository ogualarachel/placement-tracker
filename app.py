from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placements.db"

db = SQLAlchemy(app)
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False)

@app.route("/")
def home():
    applications = Application.query.all()

    total_applications = Application.query.count()
    interviews = Application.query.filter_by(status="interview").count()
    offers = Application.query.filter_by(status="offer").count()

    return render_template(
        "index.html",
        applications=applications,
        total_applications=total_applications,
        interviews=interviews,
        offers=offers
    )

@app.route("/add", methods=["GET", "POST"])
def add_application():

    if request.method == "POST":
        company = request.form.get("company", "").strip()
        role = request.form.get("role", "").strip()
        location = request.form.get("location", "").strip()
        deadline = request.form.get("deadline", "").strip()
        status = request.form.get("status", "").strip()

        valid_statuses = [
            "interested",
            "applied",
            "assessment",
            "interview",
            "offer",
            "rejected"
        ]

        if not company or not role or not location or not deadline:
            return render_template(
                "add_application.html",
                error="Please complete all fields."
            )

        if status not in valid_statuses:
            return render_template(
                "add_application.html",
                error="Please choose a valid status."
            )

        new_application = Application(
            company=company,
            role=role,
            location=location,
            deadline=deadline,
            status=status
        )

        db.session.add(new_application)
        db.session.commit()

        return redirect(url_for("applications"))

    return render_template("add_application.html")

@app.route("/applications/edit/<int:id>", methods=["GET", "POST"])
def edit_application(id):
    application = Application.query.get_or_404(id)

    if request.method == "POST":
        company = request.form.get("company", "").strip()
        role = request.form.get("role", "").strip()
        location = request.form.get("location", "").strip()
        deadline = request.form.get("deadline", "").strip()
        status = request.form.get("status", "").strip()

        valid_statuses = [
            "interested", "applied", "assessment",
            "interview", "offer", "rejected"
        ]

        if not company or not role or not location or not deadline:
            return render_template(
                "edit_application.html",
                application=application,
                error="Please complete all fields."
            )

        if status not in valid_statuses:
            return render_template(
                "edit_application.html",
                application=application,
                error="Please choose a valid status."
            )

        application.company = company
        application.role = role
        application.location = location
        application.deadline = deadline
        application.status = status

        db.session.commit()

        return redirect(url_for("applications"))

    return render_template(
        "edit_application.html",
        application=application
    )
@app.route("/applications")
def applications():
    search = request.args.get("search", "").strip()
    status = request.args.get("status", "")

    query = Application.query

    if search:
        query = query.filter(
            Application.company.ilike(f"%{search}%")
        )

    if status:
        query = query.filter_by(status=status)

    applications = query.order_by(Application.id.desc()).all()

    return render_template(
        "applications.html",
        applications=applications,
        search=search,
        selected_status=status
    )
@app.route("/applications/delete/<int:id>", methods=["POST"])
def delete_application(id):
    application = Application.query.get_or_404(id)

    db.session.delete(application)
    db.session.commit()

    return redirect(url_for("applications"))

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)