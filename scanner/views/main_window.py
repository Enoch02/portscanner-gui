import sys

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFormLayout, QLineEdit, QWidget, QPushButton, QHBoxLayout

from utils.helper_functions import scan_host


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_main_window()

    def setup_main_window(self):
        self.setWindowTitle("Really Basic Port Scanner")

        central_widget = QWidget()

        self.host_line_edit = QLineEdit()
        self.host_line_edit.setText("localhost")

        port_range_h_box = QHBoxLayout()
        
        self.start_line_edit = QLineEdit()
        self.start_line_edit.setPlaceholderText("Start")
        self.start_line_edit.setText("50")

        self.end_line_edit= QLineEdit()
        self.end_line_edit.setPlaceholderText("End")
        self.end_line_edit.setText("65535")

        port_range_h_box.addWidget(self.start_line_edit)
        port_range_h_box.addWidget(self.end_line_edit)

        self.scan_button = QPushButton("Scan Host")
        self.scan_button.clicked.connect(lambda: scan_host(self.host_line_edit.text()))

        main_form = QFormLayout()
        main_form.setFieldGrowthPolicy(main_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        main_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        main_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        main_form.addRow("Host", self.host_line_edit)
        main_form.addRow("Port Range", port_range_h_box)
        main_form.addRow(self.scan_button)


        central_widget.setLayout(main_form)
        self.setCentralWidget(central_widget)
        self.show()
