# review_service.py

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Словарь для хранения отзывов в памяти
reviews = {}
current_id = 1

# Вспомогательная функция для проверки существования пользователя
def check_user_exists(user_id):
    try:
        response = requests.get(f"http://localhost:5001/users/{user_id}")
        return response.status_code == 200
    except Exception:
        return False

# POST /reviews — создание нового отзыва
@app.route("/reviews", methods=["POST"])
def create_review():
    global current_id
    data = request.json

    user_id = data.get("user_id")
    text = data.get("text")
    rating = data.get("rating")

    # Проверка обязательных полей
    if not user_id or not text or not rating:
        return jsonify({"error": "Missing fields"}), 400

    # Проверка существования пользователя через UserService
    if not check_user_exists(user_id):
        return jsonify({"error": "User not found"}), 404

    review = {
        "id": current_id,
        "user_id": user_id,
        "text": text,
        "rating": rating
    }

    reviews[current_id] = review
    current_id += 1

    return jsonify(review), 201

# GET /reviews/<id> — получить отзыв по ID
@app.route("/reviews/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = reviews.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review), 200

# Запуск приложения
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)