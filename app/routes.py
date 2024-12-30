from flask import render_template, request, redirect, url_for, flash
from app import app
from app.redis_db import save_reservation, get_all_reservations, delete_reservation

# Main page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("time")
        guests = request.form.get("guests")
        comments = request.form.get("comments")

        save_reservation(name, email, date, time, guests, comments)
        flash("Reservation created successfully! Thank you!", "success")
        return redirect(url_for("confirmation"))

    return render_template("index.html")


# Administration panel
@app.route("/admin")
def admin():
    reservations = get_all_reservations()
    return render_template("admin.html", reservations=reservations)


# Usuwanie rezerwacji
@app.route("/delete/<reservation_id>")
def delete(reservation_id):
    delete_reservation(reservation_id)
    flash("Reservation deleted successfully!", "info")
    return redirect(url_for("admin"))

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")