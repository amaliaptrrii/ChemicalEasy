import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

kamus_unsur = {
    "H": ["Hidrogen", 1, 1.008],
    "He": ["Helium", 2, 4.0026],
    "Li": ["Litium", 3, 6.94],
    "Be": ["Berilium", 4, 9.0122],
    "B": ["Boron", 5, 10.81],
    "C": ["Karbon", 6, 12.011],
    "N": ["Nitrogen", 7, 14.007],
    "O": ["Oksigen", 8, 15.999],
    "F": ["Fluorin", 9, 18.9984],
    "Na": ["Natrium", 11, 22.98],
    "Mg": ["Magnesium", 12, 24.305],
    "Al": ["Aluminium", 13, 26.981],
    "Si": ["Silikon", 14, 28.085],
    "P": ["Fosfor", 15, 30.9738],
    "S": ["Sulfur", 16, 32.06],
    "Cl": ["Klorin", 17, 35.45],
    "K": ["Kalium", 19, 39.0983],
    "Ca": ["Kalsium", 20, 40.078],
    "Sc": ["Skandium", 21, 44.9559],
    "Ti": ["Titanium", 22, 47.867],
    "V": ["Vanadium", 23, 50.942],
    "Cr": ["Kromium", 24, 51.996],
    "Mn": ["Mangan", 25, 54.938],
    "Fe": ["Besi", 26, 55.847],
    "Co": ["Kobalt", 27, 58.933],
    "Ni": ["Nikel", 28, 58.693],
    "Cu": ["Tembaga", 29, 63.546],
    "Zn": ["Seng", 30, 65.38],
    "Ga": ["Galium", 31, 69.723],
    "Ge": ["Germanium", 32, 72.61],
    "As": ["Arsen", 33, 74.922],
    "Se": ["Selen", 34, 78.971],
    "Br": ["Brom", 35, 79.904],
    "Kr": ["Kripton", 36, 83.798],
    "Rb": ["Rubidium", 37, 85.468],
    "Sr": ["Stronsium", 38, 87.62],
    "Y": ["Itrium", 39, 88.906],
    "Zr": ["Zirkonium", 40, 91.22],
    "Nb": ["Niobium", 41, 92.906],
    "Mo": ["Molibdenum", 42, 95.95],
    "Tc": ["Teknesium", 43, 98.0],
    "Ru": ["Rutenium", 44, 101.07],
    "Rh": ["Rodium", 45, 102.91],
    "Pd": ["Palladium", 46, 106.42],
    "Ag": ["Perak", 47, 107.87],
    "Cd": ["Kadmium", 48, 112.41],
    "In": ["Indium", 49, 114.82],
    "Sn": ["Timah", 50, 118.71],
    "Sb": ["Antimon", 51, 121.76],
    "Te": ["Telurium", 52, 127.6],
    "I": ["Yodium", 53, 126.904],
    "Xe": ["Xenon", 54, 131.29],
    "Cs": ["Sesium", 55, 132.905],
    "Ba": ["Barium", 56, 137.33],
    "La": ["Lanthanum", 57, 138.905],
    "Ce": ["Serium", 58, 140.12],
    "Pr": ["Praseodimium", 59, 140.908],
    "Nd": ["Neodimium", 60, 144.24],
    "Pm": ["Promethium", 61, 145.0],
    "Sm": ["Samarium", 62, 150.36],
    "Eu": ["Europium", 63, 151.96],
    "Gd": ["Gadolinium", 64, 157.25],
    "Tb": ["Terbium", 65, 158.92],
    "Dy": ["Dysprosium", 66, 162.5],
    "Ho": ["Holmium", 67, 164.93],
    "Er": ["Erbium", 68, 167.26],
    "Tm": ["Thulium", 69, 168.93],
    "Yb": ["Ytterbium", 70, 173.04],
    "Lu": ["Lutetium", 71, 174.97],
    "Hf": ["Hafnium", 72, 178.49],
    "Ta": ["Tantalum", 73, 180.948],
    "W": ["Tungsten", 74, 183.85],
    "Re": ["Rhenium", 75, 186.207],
    "Os": ["Osmium", 76, 190.2],
    "Ir": ["Iridium", 77, 192.22],
    "Pt": ["Platinum", 78, 195.08],
    "Au": ["Emas", 79, 196.97],
    "Hg": ["Mercury", 80, 200.59],
    "Tl": ["Timbal", 81, 204.383],
    "Pb": ["Plumbum", 82, 207.2],
    "Bi": ["Bismuth", 83, 208.980],
    "Po": ["Polonium", 84, 209.0],
    "At": ["Astatine", 85, 210.0],
    "Rn": ["Radon", 86, 222.0],
    "Fr": ["Fransium", 87, 223.0],
    "Ra": ["Radium", 88, 226.025],
    "Ac": ["Aktinium", 89, 227.03],
    "Th": ["Torium", 90, 232.04],
    "Pa": ["Protaktinium", 91, 231.04],
    "U": ["Uranium", 92, 238.03],
    "Np": ["Neptunium", 93, 237.05],
    "Pu": ["Plutonium", 94, 244.0],
    "Am": ["Americium", 95, 243.0],
    "Cm": ["Curium", 96, 247.0],
    "Bk": ["Berkelium", 97, 247.0],
    "Cf": ["Californium", 98, 251.0],
    "Es": ["Einsteinium", 99, 252.0],
    "Fm": ["Fermium", 100, 257.0],
    "Md": ["Mendelevium", 101, 258.0],
    "No": ["Nobelium", 102, 259.0],
    "Lr": ["Lawrencium", 103, 262.0],
    "Rf": ["Rutherfordium", 104, 267.0],
    "Db": ["Dubnium", 105, 268.0],
    "Sg": ["Seaborgium", 106, 269.0],
    "Bh": ["Bohrium", 107, 270.0],
    "Hs": ["Hassium", 108, 270.0],
    "Mt": ["Meitnerium", 109, 278.0],
    "Ds": ["Darmstadtium", 110, 281.0],
    "Rg": ["Roentgenium", 111, 281.0],
    "Cn": ["Copernicium", 112, 285.0],
    "Nh": ["Nihonium", 113, 286.0],
    "Fl": ["Flerovium", 114, 289.0],
    "Mc": ["Moscovium", 115, 289.0],
    "Lv": ["Livermorium", 116, 293.0],
    "Ts": ["Tennessine", 117, 294.0],
    "Og": ["Oganesson", 118, 294.0],
}

def hitung_massa_molar(senyawa, kamus_unsur):
    massa_molar = 0
    unsur_saat_ini = ""
    jumlah = ""
    i = 0
    while i < len(senyawa):
        char = senyawa[i]
        if char.isupper():
            if unsur_saat_ini:
                if jumlah:
                    massa_molar += kamus_unsur[unsur_saat_ini][2] * int(jumlah)
                else:
                    massa_molar += kamus_unsur[unsur_saat_ini][2]
            unsur_saat_ini = char
            jumlah = ""
        elif char.islower():
            unsur_saat_ini += char
        elif char.isdigit():
            jumlah += char
        elif char == "(":
            start = i + 1
            end = start
            count_brackets = 1
            while count_brackets != 0:
                if senyawa[end] == "(":
                    count_brackets += 1
                elif senyawa[end] == ")":
                    count_brackets -= 1
                end += 1
            sub_senyawa = senyawa[start:end - 1]
            i = end - 1
            sub_massa_molar = hitung_massa_molar(sub_senyawa, kamus_unsur)
            multiplier = ""
            while end < len(senyawa) and senyawa[end].isdigit():
                multiplier += senyawa[end]
                end += 1
            if multiplier:
                multiplier = int(multiplier)
            else:
                multiplier = 1
            massa_molar += sub_massa_molar * multiplier
        i += 1

    if unsur_saat_ini:
        if jumlah:
            massa_molar += kamus_unsur[unsur_saat_ini][2] * int(jumlah)
        else:
            massa_molar += kamus_unsur[unsur_saat_ini][2]

    return massa_molar

class ChemicalEasyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical-Easy")
        self.setGeometry(350, 50, 650, 650)
        self.setStyleSheet("background-color: #B22222; font-family: Times New Roman;")
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.clear_layout()
        self.menu_layout = QVBoxLayout()
        self.welcome_label = QLabel("Selamat datang di Chemical-Easy!")
        self.welcome_label.setStyleSheet("font-size: 40px; font-weight: bold; color: orange; margin-bottom: 20px")
        self.layout.addWidget(self.welcome_label, alignment=Qt.AlignCenter)

        logo_label = QLabel(self)
        pixmap = QPixmap("Logo.png")
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(logo_label)

        start_button = QPushButton("Mulai")
        start_button.setStyleSheet("font-size: 16px; padding: 20px 100px; background-color: #DAA520; color: black; border: none; border-radius: 5px;")
        start_button.clicked.connect(self.tampilan_menu)
        self.layout.addWidget(start_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def handle_choice(self, choice):
        if choice == "Mencari Nomor Atom dan Nomor Massa":
            self.display_nomorAtom_nomorMassa()
        elif choice == "Cari Jumlah Mol Senyawa":
            self.cari_mol_senyawa()
        elif choice == "Seimbangkan Reaksi Kimia":
            self.seimbangkan_reaksi_kimia()
        elif choice == "Keluar":
            self.close()

    def tampilan_menu(self):
        self.clear_layout()
        self.menu_layout = QVBoxLayout()

        menu_label = QLabel("Menu Chemical-Easy:")
        menu_label.setStyleSheet("font-size: 30px; font-weight: bold; margin-bottom: 5px; color: orange;")
        self.layout.addWidget(menu_label)

        self.button = []
        menu_options = [
            "Mencari Nomor Atom dan Nomor Massa",
            "Cari Jumlah Mol Senyawa",
            "Seimbangkan Reaksi Kimia",
            "Keluar"
        ]
        for option in menu_options:
            button = QPushButton(option)
            button.setStyleSheet("font-size: 14px; padding: 20px 40px; background-color: #DAA520; color: black; border: none; border-radius: 5px;")
            button.clicked.connect(lambda _, choice=option: self.handle_choice(choice))
            self.layout.addWidget(button)

        self.layout.addLayout(self.layout)

    def display_nomorAtom_nomorMassa(self):
        self.clear_layout()
        self.current_choice_label = QLabel("Mencari Nomor Atom dan Nomor Massa")
        self.current_choice_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 2px; color: white;")
        self.layout.addWidget(self.current_choice_label)

        self.current_choice_label = QLabel("Masukkan unsur")
        self.current_choice_label.setStyleSheet("font-size: 16px; margin-top: 2px; font-weight: bold; color: white;")
        self.layout.addWidget(self.current_choice_label)

        self.unsur_input = QLineEdit()
        self.unsur_input.setStyleSheet("font-size: 16px; padding: 10px; border: 1px solid #DAA520; border-radius: 5px; color: white")
        self.layout.addWidget(self.unsur_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("font-size: 14px; padding: 10px 20px; background-color: #DAA520; color: black; border: none; border-radius: 5px;")
        self.submit_button.clicked.connect(self.submit_nomorAtom_nomorMassa)
        self.layout.addWidget(self.submit_button)

        self.back_button = QPushButton("Kembali")
        self.back_button.setStyleSheet("font-size: 14px; padding: 10px 20px; background-color: #DAA520; color: black; border: none; border-radius: 5px;")
        self.back_button.clicked.connect(self.kembali_ke_menu)
        self.layout.addWidget(self.back_button)

    def submit_nomorAtom_nomorMassa(self):
        nama_unsur = self.unsur_input.text().strip()
        if nama_unsur in kamus_unsur:
            unsur = kamus_unsur[nama_unsur]
            message = f"Singkatan unsur: {nama_unsur}\nNama unsur: {unsur[0]}\nNomor Atom: {unsur[1]}\nNomor Massa: {unsur[2]}"
            QMessageBox.information(self, "Hasil", message)
        else:
            QMessageBox.warning(self, "Peringatan", "Nama unsur tidak valid")

    def cari_mol_senyawa(self):
        self.clear_layout()
        self.current_choice_label = QLabel("Mencari Jumlah Mol Senyawa")
        self.current_choice_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        self.layout.addWidget(self.current_choice_label)

        self.method_label = QLabel("Pilih metode untuk menghitung mol senyawa:")
        self.method_label.setStyleSheet("font-size: 18px; margin-top: 8px; color: white;")
        self.layout.addWidget(self.method_label)

        self.method_buttons = []
        method_options = ["Jumlah partikel", "Massa", "Volume gas (STP)", "Molaritas"]
        for i, option in enumerate(method_options, 1):
            button = QPushButton(option)
            button.setStyleSheet("font-size: 14px; padding: 20px 24px; background-color: #DAA520; color: black; border: none; border-radius: 5px;")
            button.clicked.connect(lambda _, method=i: self.handle_mol_senyawa_method(method))
            self.layout.addWidget(button)
            self.method_buttons.append(button)

        self.back_button = QPushButton("Kembali")
        self.back_button.setStyleSheet("font-size: 14px; padding: 10px 20px; background-color: #DAA520; color: black; border: none; border-radius: 5px;")
        self.back_button.clicked.connect(self.kembali_ke_menu)
        self.layout.addWidget(self.back_button)

    def handle_mol_senyawa_method(self, method):
        self.clear_layout()
        self.current_choice_label = QLabel("Cari Jumlah Mol Senyawa")
        self.current_choice_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
        self.layout.addWidget(self.current_choice_label)

        if method == 1:
            self.display_jumlah_partikel()
        elif method == 2:
            self.display_dari_massa()
        elif method == 3:
            self.display_dari_volume_gas()
        elif method == 4:
            self.display_dari_molaritas()

    def display_jumlah_partikel(self):
        self.senyawa_label = QLabel("Masukkan Senyawa:")
        self.senyawa_label.setStyleSheet("font-size: 14px; margin-top: 8px; color: white;")
        self.layout.addWidget(self.senyawa_label)

        self.senyawa_input = QLineEdit()
        self.senyawa_input.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.senyawa_input)

        self.jumlah_partikel_label = QLabel("Masukkan jumlah partikel:")
        self.jumlah_partikel_label.setStyleSheet("font-size: 14px; margin-top: 8px; color: white;")
        self.layout.addWidget(self.jumlah_partikel_label)

        self.jumlah_partikel_input = QLineEdit()
        self.jumlah_partikel_input.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.jumlah_partikel_input)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.setStyleSheet("font-size: 14px; padding: 5px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.calculate_button.clicked.connect(self.calculate_jumlah_partikel)
        self.layout.addWidget(self.calculate_button)

        self.back_button = QPushButton("Kembali")
        self.back_button.setStyleSheet("font-size: 14px; padding: 5px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.back_button.clicked.connect(self.cari_mol_senyawa)
        self.layout.addWidget(self.back_button)

    def calculate_jumlah_partikel(self):
        senyawa = self.senyawa_input.text().strip()
        jumlah_partikel = float(self.jumlah_partikel_input.text())
        bilangan_avogadro = 6.02*10e23
        mol = jumlah_partikel / bilangan_avogadro
        QMessageBox.information(self, "Hasil", f"Jumlah mol senyawa {senyawa}: {mol:.25f} mol")

    def display_dari_massa(self):
        self.senyawa_label = QLabel("Masukkan Senyawa:")
        self.senyawa_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.senyawa_label)

        self.senyawa_input = QLineEdit()
        self.senyawa_input.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.senyawa_input)

        self.massa_label = QLabel("Masukkan massa (dalam gram):")
        self.massa_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.massa_label)

        self.massa_input = QLineEdit()
        self.massa_input.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.massa_input)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.setStyleSheet("font-size: 14px; padding: 5px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.calculate_button.clicked.connect(self.calculate_dari_massa)
        self.layout.addWidget(self.calculate_button)

        self.back_button = QPushButton("Kembali")
        self.back_button.setStyleSheet("font-size: 14px; padding: 5px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.back_button.clicked.connect(self.cari_mol_senyawa)
        self.layout.addWidget(self.back_button)

    def calculate_dari_massa(self):
        senyawa = self.senyawa_input.text().strip()
        massa = float(self.massa_input.text())
        massa_molar = hitung_massa_molar(senyawa, kamus_unsur)
        if massa_molar is not None:
            mol = massa / massa_molar
            QMessageBox.information(self, "Hasil", f"Jumlah mol senyawa: {mol:.2f} mol")
        else:
            QMessageBox.warning(self, "Peringatan","Senyawa tidak dapat dihitung karena unsur yang digunakan tidak ada dalam kamus unsur.")

    def display_dari_volume_gas(self):
        self.senyawa_label = QLabel("Masukkan Senyawa:")
        self.senyawa_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.senyawa_label)

        self.senyawa_input = QLineEdit()
        self.senyawa_input.setStyleSheet("font-size: 14px; padding: 10px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.senyawa_input)

        self.volume_label = QLabel("Masukkan jumlah volume:")
        self.volume_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.volume_label)

        self.volume_input = QLineEdit()
        self.volume_input.setStyleSheet("font-size: 14px; padding: 10px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.volume_input)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.setStyleSheet("font-size: 14px; padding: 10px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.calculate_button.clicked.connect(self.calculate_dari_volume_gas)
        self.layout.addWidget(self.calculate_button)

        self.back_button = QPushButton("Kembali")
        self.back_button.setStyleSheet("font-size: 14px; padding: 5px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.back_button.clicked.connect(self.cari_mol_senyawa)
        self.layout.addWidget(self.back_button)

    def calculate_dari_volume_gas(self):
        senyawa = self.senyawa_input.text().strip()
        V = float(self.volume_input.text())
        A = 22.4
        mol = V / A
        QMessageBox.information(self, "Hasil", f"Jumlah mol senyawa: {mol:.2f} mol")

    def display_dari_molaritas(self):
        self.senyawa_label = QLabel("Masukkan Senyawa:")
        self.senyawa_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.senyawa_label)

        self.senyawa_input = QLineEdit()
        self.senyawa_input.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.senyawa_input)

        self.molaritas_label = QLabel("Masukkan Molaritas:")
        self.molaritas_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.molaritas_label)

        self.molaritas_input = QLineEdit()
        self.molaritas_input.setStyleSheet("font-size: 14px; padding: 10px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.molaritas_input)

        self.volume_label = QLabel("Masukkan Volume:")
        self.volume_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: white;")
        self.layout.addWidget(self.volume_label)

        self.volume_input = QLineEdit()
        self.volume_input.setStyleSheet("font-size: 14px; padding: 10px; border: 1px solid white; border-radius: 5px; color: white;")
        self.layout.addWidget(self.volume_input)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.setStyleSheet("font-size: 14px; padding: 10px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.calculate_button.clicked.connect(self.calculate_dari_molaritas)
        self.layout.addWidget(self.calculate_button)

        self.back_button = QPushButton("Kembali")
        self.back_button.setStyleSheet("font-size: 14px; padding: 5px 20px; background-color: white; color: black; border: none; border-radius: 5px;")
        self.back_button.clicked.connect(self.cari_mol_senyawa)
        self.layout.addWidget(self.back_button)

    def calculate_dari_molaritas(self):
        senyawa = self.senyawa_input.text().strip()
        M = float(self.molaritas_input.text())
        V = float(self.volume_input.text())
        mol = M * V
        QMessageBox.information(self, "Hasil", f"Jumlah mol senyawa: {mol:.2f} mol")

    def seimbangkan_reaksi_kimia(self):
        QMessageBox.information(self, "Peringatan", "Fitur ini masih dalam proses pengembangan. Mohon tunggu pembaruan selanjutnya!")

    def kembali_ke_menu(self):
        self.clear_layout()
        self.tampilan_menu()

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChemicalEasyApp()
    window.show()
    sys.exit(app.exec_())