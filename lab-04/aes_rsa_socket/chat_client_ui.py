import sys
import threading
from PyQt5 import QtWidgets
from ui_chat import Ui_MainWindow

import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# RSA
client_key = RSA.generate(2048)

server_public_key = RSA.import_key(client_socket.recv(2048))
client_socket.send(client_key.publickey().export_key(format='PEM'))

cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(client_socket.recv(2048))

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()


class ChatApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_send.clicked.connect(self.send_message)

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        msg = self.ui.txt_chat_input.text()
        if msg:
            encrypted = encrypt_message(aes_key, msg)
            client_socket.send(encrypted)
            self.ui.txt_chat.append(f"Me: {msg}")
            self.ui.txt_chat_input.clear()

    def receive_messages(self):
        while True:
            try:
                encrypted_message = client_socket.recv(1024)
                message = decrypt_message(aes_key, encrypted_message)
                self.ui.txt_chat.append(f"Friend: {message}")
            except:
                break

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec_())
