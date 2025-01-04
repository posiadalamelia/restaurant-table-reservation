from app import redis_client
import uuid
from datetime import datetime

def save_reservation(name, email, date, time, guests, comments):
    reservation_id = str(uuid.uuid4()) # create unique id of reservation
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M') # Get the current date and time in ISO 8601 format
    reservation_data = {
        "id": reservation_id,
        "timestamp" : timestamp,
        "name": name,
        "email": email,
        "date": date,
        "time": time,
        "guests": guests,
        "comments": comments
    }
    redis_client.hset(f"reservation:{reservation_id}", mapping=reservation_data)
    redis_client.lpush("reservations", reservation_id)
    return reservation_id

def get_all_reservations():
    reservation_ids = redis_client.lrange("reservations", 0, -1)
    reservations = []
    for reservation_id in reservation_ids:
        reservation = redis_client.hgetall(f"reservation:{reservation_id}")
        if reservation:
            reservations.append(reservation)
    return reservations

def get_reservation(reservation_id):
    return redis_client.hgetall(f"reservation:{reservation_id}")

def delete_reservation(reservation_id):
    redis_client.delete(f"reservation:{reservation_id}")
    redis_client.lrem("reservations", 0, reservation_id)

def update_reservation(reservation_id, updated_data):
    redis_client.hmset(f"reservation:{reservation_id}", updated_data)