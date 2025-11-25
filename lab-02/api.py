from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(__name__)
cipher = CaesarCipher()

# @app.route("/api/caesar/encrypt", methods=["POST"])
# def caesar_encrypt():
#     data = request.json
#     plain_text = data['plain_text']
#     key = int(data['key'])
#     encrypted_text = cipher.encrypt(plain_text, key)
#     return jsonify({"encrypted_text": encrypted_text})

# @app.route("/api/caesar/decrypt", methods=["POST"])
# def caesar_decrypt():
#     data = request.json
#     cipher_text = data['cipher_text']
#     key = int(data['key'])
#     decrypted_text = cipher.decrypt(cipher_text, key)
#     return jsonify({"decrypted_text": decrypted_text})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001   , debug=True)
from cipher.vigenere import VigenereCipher    # Thêm vào phần đầu của file api.py

# Thêm đoạn sau vào trước hàm main
# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000   , debug=True)