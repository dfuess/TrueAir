#! /usr/bin/python3.10
import sys
import os
from PySide6.QtWidgets import *
from ui_about import Ui_aboutDialog
from analysis import *
import ui_trueair


class TrueAir(QMainWindow, ui_trueair.Ui_MainWindow):
    def __init__(self):
        super(TrueAir, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Blood data plotting and analysis')
        self.db = BloodData()
        if self.db.database is not None:
            self.source.setText(os.path.basename(self.db.database))
            self.note.setText("Select start date")

        self.date_start = None
        self.date_end = None
        self.am_data = []
        self.pm_data = []

        self.fitType.addItems(['Cubic', 'Quadratic', 'Linear'])
        self.fitType.setCurrentText('Cubic')

        self.span.addItems(["None", "30", "90", "365"])
        self.span.currentIndexChanged.connect(self.setSpan)

        self.buttonFrom.setStyleSheet("background-color: red; color: white;")
        self.buttonFrom.clicked.connect(self.selectStartDate)

        self.buttonTo.setStyleSheet("background-color: red; color: white;")
        self.buttonTo.clicked.connect(self.selectEndDate)

        self.buttonPlot.setStyleSheet("background-color: red; color: white;")
        self.buttonPlot.clicked.connect(self.plotData)
        self.buttonPlot.setDisabled(True)

        self.actionOpen .triggered.connect(self.fileOpen)
        self.actionClose.triggered.connect(self.fileClose)
        self.actionQuit .triggered.connect(self.fileQuit)
        self.actionAbout.triggered.connect(self.helpAbout)
        self.selectEndDate()

    def selectStartDate(self):
        self.date_start = datetime.fromisoformat(str(self.calendar.selectedDate().toPython()))
        if self.date_start > datetime.now():
            self.startdate.setText("Start after today?")
            self.date_start = None
            self.buttonFrom.setStyleSheet("background-color: red; color: white;")
            return
        self.buttonFrom.setStyleSheet("background-color: green; color: white;")
        self.startdate.setText(self.date_start.strftime("%D"))
        self.fetchData()

    def selectEndDate(self):
        self.date_end = datetime.fromisoformat(str(self.calendar.selectedDate().toPython()))
        if self.date_end > datetime.now():
            self.enddate.setText("End after today?")
            self.date_end = None
            self.buttonTo.setStyleSheet("background-color: red; color: white;")
            return
        self.buttonTo.setStyleSheet("background-color: green; color: white;")
        self.enddate.setText(self.date_end.strftime("%D"))
        self.fetchData()

    def plotData(self):
        if len(self.am_data) == 0 or len(self.pm_data) == 0:
            self.note.setText("NO DATA!")
            return
        self.note.setText("Plotting ...")
        msg = plotBloodData(self.db, self.fitType.currentText(), 1, am=self.am_data, pm=self.pm_data)
        self.statusbar.showMessage(msg)

    def fetchData(self, updatespan=True):
        if self.date_start is None:
            self.note.setText("Set start date.")
            return
        elif self.date_end is None:
            self.note.setText("Set end date.")
            return
        if updatespan:
            self.span.setItemText(0, str((self.date_end-self.date_start).days))
            self.span.setCurrentIndex(0)
        self.am_data = self.db.getDataRange(start=self.date_start, stop=self.date_end, hours=[0, 12])
        self.pm_data = self.db.getDataRange(start=self.date_start, stop=self.date_end, hours=[12, 24])
        if len(self.am_data) < 3:
            self.note.setText(f"No data")
            self.buttonPlot.setDisabled(True)
            return
        self.buttonPlot.setStyleSheet("background-color: green; color: white;")
        self.note.setText(f"Data items: {len(self.am_data)}")
        self.buttonPlot.setDisabled(False)

    def setSpan(self, index):
        dayspan = self.span.currentText()
        if dayspan == "None":
            return
        self.date_start = self.date_end - timedelta(days=int(dayspan))
        self.buttonFrom.setStyleSheet("background-color: green; color: white;")
        self.startdate.setText(self.date_start.strftime("%D"))
        self.fetchData(updatespan=False)

    def fileOpen(self):
        self.statusbar.showMessage("Open not available yet.")

    def fileClose(self):
        self.statusbar.showMessage("Close not available yet.")

    def fileQuit(self):
        self.close()

    def helpAbout(self):
        dlg = aboutDlg(self)
        dlg.exec()


class aboutDlg(Ui_aboutDialog, QDialog):
    """About dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Run the .setupUi() method to show the GUI
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = TrueAir()
    form.show()
    app.exec()
