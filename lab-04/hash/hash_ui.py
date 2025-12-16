import sys
import hashlib
from Crypto.Hash import SHA3_256
from PyQt5 import QtWidgets
from ui_hash import Ui_MainWindow


class HashWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bth_md5.clicked.connect(self.hash_md5)
        self.ui.bttn_sha256.clicked.connect(self.hash_sha256)
        self.ui.bttn_sha3.clicked.connect(self.hash_sha3)
        self.ui.btn_blake2.clicked.connect(self.hash_blake2)

    def get_text(self):
        return self.ui.txt_input.toPlainText().encode("utf-8")

    def show_result(self, result):
        self.ui.txt_output.setPlainText(result)

    def hash_md5(self):
        data = self.get_text()
        result = hashlib.md5(data).hexdigest()
        self.show_result(result)

    def hash_sha256(self):
        data = self.get_text()
        result = hashlib.sha256(data).hexdigest()
        self.show_result(result)

    def hash_sha3(self):
        data = self.get_text()
        sha3_hash = SHA3_256.new()
        sha3_hash.update(data)
        self.show_result(sha3_hash.hexdigest())

    def hash_blake2(self):
        data = self.get_text()
        blake_hash = hashlib.blake2b(digest_size=64)  # 512-bit
        blake_hash.update(data)
        self.show_result(blake_hash.hexdigest())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HashWindow()
    window.show()
    sys.exit(app.exec_())
