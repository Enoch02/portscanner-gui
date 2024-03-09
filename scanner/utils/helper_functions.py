from socket import *
import time
from PyQt6.QtWidgets import QWidget, QMessageBox

from model.port import Port
from utils.custom_errros import InvalidPortRangeException


def validate_input_and_scan(parent: QWidget, target: str, start: str, end: str) -> list[Port]:
    try:
        start = int(start)
        end = int(end)

        if start < 0 or end > 65535:
            raise InvalidPortRangeException("Mininum index is 0 and max index is 65535")

        if start > end:
            raise InvalidPortRangeException(
                "Start port is greater than end port in the range"
            )

        return scan_host(target, start, end)

    except InvalidPortRangeException as e:
        QMessageBox.critical(
            parent,
            "Error",
            str(e),
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Ok,
        )


def scan_host(target: str, start: int, end: int) -> list[Port]:
    ports: list[Port] = []
    start_time = time.time()
    t_IP = gethostbyname(target)
    print("Starting scan on host: ", t_IP)

    for i in range(start, end):  # max value = 65535
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            print("Port %d: OPEN" % (i,))
            ports.append(Port(i, "OPEN"))
        else:
            ports.append(Port(i, "CLOSED"))

        s.close()

    print("Time taken:", time.time() - start_time)

    return ports
