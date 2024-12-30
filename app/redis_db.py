from app import redis_client
import uuid

# Save reservation to Redis
def save_reservation(name, email, date, time, guests, comments):
    reservation_id = str(uuid.uuid4())
    reservation_data = {
        "id": reservation_id,
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

# Pobranie wszystkich rezerwacji
def get_all_reservations():
    reservation_ids = redis_client.lrange("reservations", 0, -1)
    reservations = []
    for reservation_id in reservation_ids:
        reservation = redis_client.hgetall(f"reservation:{reservation_id}")
        if reservation:
            reservations.append(reservation)
    return reservations

# Pobranie szczegółów rezerwacji
def get_reservation(reservation_id):
    return redis_client.hgetall(f"reservation:{reservation_id}")

# Usunięcie rezerwacji
def delete_reservation(reservation_id):
    redis_client.delete(f"reservation:{reservation_id}")
    redis_client.lrem("reservations", 0, reservation_id)