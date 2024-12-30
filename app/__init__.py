from flask import Flask
from redis import Redis
import os

app = Flask(__name__) # Flask appliaction's object
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key_here')
app.config['REDIS_HOST'] = os.getenv('REDIS_HOST', 'redis')
app.config['REDIS_PORT'] = os.getenv('REDIS_PORT', 6379)

redis_client = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], decode_responses=True) # responses as string, not bytes

from app import routes

# class Reservation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     time = db.Column(db.Time, nullable=False)
#     guests = db.Column(db.Integer, nullable=False)
#     comments = db.Column(db.Text, nullable=True)

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method=='POST':
#         #pobranie danych z formularza
#         name = request.form.get("name")
#         email = request.form.get("email")
#         date = request.form.get("date")
#         time = request.form.get("time")
#         guests = request.form.get("guests")
#         comments = request.form.get("comments")

#         #stworzenie nowej rezerwacji
#         new_reservation = Reservation(
#             name=name,
#             email=email,
#             date=date,
#             time=time,
#             guests=guests,
#             comments=comments,
#         )

#         try:
#             db.session.add(new_reservation)
#             db.session.commit()
#             flash("Reservation created successfully!", "success")
#             return redirect(url_for("index"))
#         except:
#             return 'There was an issue adding your reservation'

#     else:
#         return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)