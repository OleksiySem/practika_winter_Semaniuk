import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# --- 1. SHA-256 Гешування ---
def get_sha256_hash(text):
    """Обчислює SHA-256 геш рядка."""
    # Перетворюємо рядок у байти
    data = text.encode('utf-8')
    # Створюємо об'єкт гешування
    sha256 = hashlib.sha256()
    sha256.update(data)
    # Повертаємо шістнадцяткове представлення
    return sha256.hexdigest()


# --- 2. AES Симетричне Шифрування (AES-GCM) ---
def aes_encrypt(key, plaintext):
    """Шифрує дані за допомогою AES (режим GCM)."""
    # Генеруємо випадковий nonce (number used once) - 12 байт для GCM
    nonce = os.urandom(12)

    # Створюємо шифр
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = cipher.encryptor()

    # Шифруємо
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()

    # Повертаємо nonce, шифротекст та тег автентифікації
    return nonce, ciphertext, encryptor.tag


def aes_decrypt(key, nonce, ciphertext, tag):
    """Розшифровує дані AES."""
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = cipher.decryptor()

    # Розшифровуємо та перевіряємо цілісність
    try:
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data.decode('utf-8')
    except Exception as e:
        return "Помилка розшифрування (невірний ключ або пошкоджені дані)!"


# --- 3. RSA Асиметричний підпис ---
def generate_rsa_keys():
    """Генерує пару ключів RSA (приватний та публічний)."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(message, private_key):
    """Створює цифровий підпис повідомлення."""
    signature = private_key.sign(
        message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify_signature(message, signature, public_key):
    """Перевіряє цифровий підпис."""
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


# --- ГОЛОВНА ФУНКЦІЯ ---
def main():
    message = "Секретне повідомлення для передачі."
    print(f"Оригінальне повідомлення: '{message}'\n")
    print("-" * 50)

    # 1. ДЕМОНСТРАЦІЯ ГЕШУВАННЯ
    print("1. ГЕШУВАННЯ (SHA-256)")
    hashed_msg = get_sha256_hash(message)
    print(f"SHA-256 Digest: {hashed_msg}")
    print("Властивість: Неможливо відновити текст із цього рядка.")
    print("-" * 50)

    # 2. ДЕМОНСТРАЦІЯ AES (Симетричне шифрування)
    print("2. СИМЕТРИЧНЕ ШИФРУВАННЯ (AES)")
    # Генеруємо 256-бітний ключ (32 байти)
    aes_key = os.urandom(32)
    print(f"AES Ключ (hex): {aes_key.hex()[:20]}... (приховано)")

    nonce, ciphertext, tag = aes_encrypt(aes_key, message)
    print(f"Зашифрований текст (bytes): {ciphertext}")

    decrypted_msg = aes_decrypt(aes_key, nonce, ciphertext, tag)
    print(f"Розшифрований текст: '{decrypted_msg}'")
    print("-" * 50)

    # 3. ДЕМОНСТРАЦІЯ RSA (Цифровий підпис)
    print("3. ЦИФРОВИЙ ПІДПИС (RSA)")
    private_key, public_key = generate_rsa_keys()
    print("Ключі згенеровано.")

    signature = sign_message(message, private_key)
    print(f"Підпис (hex): {signature.hex()[:40]}... (довгий рядок)")

    is_valid = verify_signature(message, signature, public_key)
    print(f"Перевірка підпису успішна? -> {is_valid}")

    # Спроба підробити повідомлення
    fake_msg = "Підроблене повідомлення"
    is_valid_fake = verify_signature(fake_msg, signature, public_key)
    print(f"Перевірка підпису для зміненого тексту успішна? -> {is_valid_fake}")


if __name__ == "__main__":
    main()