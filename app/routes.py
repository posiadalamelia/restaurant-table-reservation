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
@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Get data from search formula
    name = request.args.get("name", "")
    email = request.args.get("email", "")
    date = request.args.get("date", "")
    time = request.args.get("time", "")
    guests = request.args.get("guests", "")

    all_reservations = get_all_reservations()

    # Data's filtering 
    search_results = all_reservations
    if name: 
        search_results = [r for r in search_results if name.lower() in r['name'].lower()]
    if email:
        search_results = [r for r in search_results if email.lower() in r['email'].lower()]
    if date:
        search_results = [r for r in search_results if date == r['date']]
    if time:
        search_results = [r for r in search_results if time == r['time']]
    if guests:
        search_results = [r for r in search_results if str(guests) == str(r['guests'])]

    return render_template("admin.html", search_results=search_results, all_reservations=all_reservations)

# Delete reservation
@app.route("/delete/<reservation_id>")
def delete(reservation_id):
    delete_reservation(reservation_id)
    flash("Reservation deleted successfully!", "info")
    return redirect(url_for("admin"))

# Confirmation of reservation
@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")