from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QListWidget

from model.port import Port


class ScanResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Result")

        layout = QVBoxLayout()

        self.open_list = QListWidget()
        self.closed_list = QListWidget()

        layout.addWidget(QLabel("Open Ports"))
        layout.addWidget(self.open_list)
        layout.addWidget(QLabel("Closed Ports"))
        layout.addWidget(self.closed_list)

        self.setLayout(layout)

    def show_results(self, result: list[Port]):
        def check_status(port: Port):
            if port.status == "OPEN":
                return True
            else:
                return False

        open_ports = filter(check_status, result)
        closed_ports = filter(lambda port: not check_status(port), result)

        for item in open_ports:
            self.open_list.addItem(f"{item.port}: {item.status}")

        for item in closed_ports:
            self.closed_list.addItem(f"{item.port}: {item.status}")

        self.show()
