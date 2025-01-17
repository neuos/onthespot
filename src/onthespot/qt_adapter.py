try:
    from PyQt5.QtCore import QObject, pyqtSignal, QThread
    QObject = QObject
    pyqtSignal = pyqtSignal
    QThread = QThread
except ImportError:
    from .runtimedata import get_logger
    from threading import Thread
    
    logger = get_logger("qt_adapter")
    logger.info("PyQt5 not found, using stubs")
    
    def pyqtSignal(*args, **kwargs):
        class Signal:
            def connect(*args, **kwargs):
                pass
            def emit(*args, **kwargs):
                pass
        return Signal()

    class QObject:
        pass

    class QThread:
        def __init__(self):
            self.thread = Thread(target=self.run)
        def start(self):
            self.thread.start()
        def wait(self):
            self.thread.join()
        def run(self):
            pass
