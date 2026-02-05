from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Налаштування
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Змініть це на складний ключ у реальному проекті
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Імітація бази даних
users_db = {}


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if username in users_db:
        return jsonify({"msg": "User already exists"}), 400

    # Хешування пароля перед збереженням
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    users_db[username] = hashed_password
    return jsonify({"msg": "User created successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Перевірка наявності користувача та валідація хешу пароля
    if username not in users_db or not bcrypt.check_password_hash(users_db[username], password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Генерація JWT-токена
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/profile', methods=['GET'])
@jwt_required()  # Цей декоратор вимагає валідного токена
def profile():
    # Отримуємо ідентифікатор користувача з токена
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Welcome back, {current_user}!", "user": current_user}), 200


if __name__ == '__main__':
    app.run(debug=True)