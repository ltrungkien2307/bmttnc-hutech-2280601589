import sys
from PyQt5 import QtWidgets
from ui_dh_key import Ui_MainWindow

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

class DHKeyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.parameters = None
        self.private_key = None
        self.public_key = None

        self.ui.btn_gen_param.clicked.connect(self.generate_params)
        self.ui.btn_gen_key.clicked.connect(self.generate_key_pair)
        self.ui.btn_load_pub.clicked.connect(self.load_other_public)
        self.ui.btn_shared.clicked.connect(self.compute_shared_secret)

    def generate_params(self):
        self.parameters = dh.generate_parameters(generator=2, key_size=2048)
        self.ui.txt_param.setPlainText("Parameters generated successfully!")

    def generate_key_pair(self):
        if not self.parameters:
            QtWidgets.QMessageBox.warning(self, "Error", "Generate parameters first!")
            return
        self.private_key = self.parameters.generate_private_key()
        self.public_key = self.private_key.public_key()
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.ui.txt_pubkey.setPlainText(pem.decode())

        # Save to file
        with open("my_public_key.pem", "wb") as f:
            f.write(pem)

    def load_other_public(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Public Key", "", "PEM Files (*.pem)")
        if fname:
            with open(fname, "rb") as f:
                self.other_public_key = serialization.load_pem_public_key(f.read())
            self.ui.txt_param.append("\nLoaded other public key!")

    def compute_shared_secret(self):
        if not hasattr(self, "other_public_key") or not self.private_key:
            QtWidgets.QMessageBox.warning(self, "Error", "Missing public or private key!")
            return
        
        shared_key = self.private_key.exchange(self.other_public_key)
        self.ui.txt_shared.setPlainText(shared_key.hex())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DHKeyApp()
    window.show()
    sys.exit(app.exec_())
