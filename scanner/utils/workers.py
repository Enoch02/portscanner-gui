from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget

from utils.helper_functions import validate_input_and_scan

class PortScannerWorker(QThread):
    finished = pyqtSignal(list)

    def __init__(self, parent: QWidget, target: str, start: str, end: str):
        super().__init__()
        self._parent = parent  # QThread also has a `parent` attr, we do not want that.
        self.target = target
        self._start = start
        self.end = end

    def run(self):
        result = validate_input_and_scan(self._parent, self.target, self._start, self.end)
        self.finished.emit(result)
