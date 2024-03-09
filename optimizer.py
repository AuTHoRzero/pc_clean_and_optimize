import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.uic import loadUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi('./templates/MainWindow.ui', self)

        self.settings_btn.clicked.connect(self.open_settings)
        self.exit_btn.clicked.connect(self.close_app)

    def open_settings(self):
        settings.show()
        self.close()

    def close_app(self):
        self.close()

        
class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('./templates/Settings.ui', self)
        self.back_btn.clicked.connect(self.back)
        self.clear_chrome_check.stateChanged.connect(lambda: self.set_checkbox_settings("Chrome", self.clear_chrome_check.isChecked()))
        self.clear_downloads_check.stateChanged.connect(lambda: self.set_checkbox_settings("Downloads", self.clear_downloads_check.isChecked()))
        self.clear_epic_check.stateChanged.connect(lambda: self.set_checkbox_settings("Epic", self.clear_epic_check.isChecked()))
        self.clear_userdata_check.stateChanged.connect(lambda: self.set_checkbox_settings("Userdata", self.clear_userdata_check.isChecked()))
        self.clear_workshop_check.stateChanged.connect(lambda: self.set_checkbox_settings("Workshop", self.clear_workshop_check.isChecked()))
        self.autoaccept_check.stateChanged.connect(lambda: self.set_checkbox_settings("Autoaccept", self.autoaccept_check.isChecked()))
        self.update_dir_list.clicked.connect(self.update_dirs)

    def back(self):
        main_window.show()
        self.close()

    def set_checkbox_settings(self, setting, state):
        print(state)

    def update_dirs(self):
        ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    settings = SettingsWindow()
    sys.exit(app.exec())
