from tools import make_train_data
import sys
from PyQt5 import QtWidgets, QtCore

class FileUploadBox(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAcceptDrops(True)  # Allow drag and drop events on the file upload box
        self.file_path = ''

    def dragEnterEvent(self, event):
        # Accept drag and drop events if they contain file data
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Get the file path from the dropped data
        self.file_path = event.mimeData().urls()[0].toLocalFile()

        # Update the text of the file upload box to display the file path
        self.setText("File accepted:" + '\n' + self.file_path)

    def text(self):
        # Return the file path when the text method is called
        return self.file_path

class FileProcessorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Quick Annotation Tool')
        self.setGeometry(100, 100, 1200, 600)
        self.setAcceptDrops(True)  # Allow drag and drop events on the main window
        self.setObjectName('mainWindow')  # Set the id of the main window
        self.setStyleSheet("""
            QMainWindow#mainWindow { 
                background-color: white 
            }
        """)  # Set the background color of the main window

        # Create a central widget to hold the file upload boxes and submit button
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Create file upload boxes
        self.file_upload_box1 = FileUploadBox('Drop the texts here', self)
        self.file_upload_box1.setAlignment(QtCore.Qt.AlignCenter)
        self.file_upload_box1.setStyleSheet("""
                        QLabel {
                            background-color: lightgray;
                            border: 2px dashed black;
                            font: bold 14px;
                            min-width: 10em;
                            padding: 6px;
                            text-align: center;
                        }

                        QLabel:hover {
                            background-color: white;
                        }
                    """)
        layout.addWidget(self.file_upload_box1)

        self.file_upload_box2 = FileUploadBox('Drop the labeled entities here', self)
        self.file_upload_box2.setAlignment(QtCore.Qt.AlignCenter)
        self.file_upload_box2.setStyleSheet("""
                        QLabel {
                            background-color: lightgray;
                            border: 2px dashed black;
                            font: bold 14px;
                            min-width: 10em;
                            padding: 6px;
                            text-align: center;
                        }

                        QLabel:hover {
                            background-color: white;
                        }
                    """)
        layout.addWidget(self.file_upload_box2)

        #submit button
        self.submit_button = QtWidgets.QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.process_files)  # Connect the button to the process_files method
        self.submit_button.setStyleSheet('''
            QPushButton {
                background-color: white;
                border-radius: 10px;
                border: 2px solid black;
                font: bold 14px;
                min-width: 10em;
                padding: 6px;
                text-align: center;
            }

            QPushButton:pressed {
                background-color: red;
            }

            QPushButton:hover {
                background-color: yellow;
            }
        ''')
        layout.addWidget(self.submit_button)

        # Set up instance variables to store the file paths
        self.file1_path = ''
        self.file2_path = ''
        #setup the button clicking event
        self.submit_button.clicked.connect(self.process_files)

    def reset_file_upload_boxes(self):
        self.file_upload_box1.setText('Drop the text to be labeled here')
        self.file_upload_box2.setText('Drop the labeled entities here')
        self.submit_button.setText("Submit")
        self.file_upload_box1.file_path = ''
        self.file_upload_box2.file_path = ''
        self.file1_path = ''
        self.file2_path = ''

    def process_files(self):
        self.file1_path = self.file_upload_box1.text()
        self.file2_path = self.file_upload_box2.text()
        print(f"Path of texts is: {self.file1_path}")
        print(f"Path of labels is: {self.file2_path}")

        if self.file1_path == '':
            message_box = QtWidgets.QMessageBox(self)
            message_box.setWindowTitle('Warning')
            message_box.setText('Dude, where are the texts??')
            message_box.exec_()
            return  # Exit the method

        if self.file2_path == '':
            message_box = QtWidgets.QMessageBox(self)
            message_box.setWindowTitle('Warning')
            message_box.setText('Dude, where are the labels??')
            message_box.exec_()
            return  # Exit the method

        self.submit_button.setText("Here you go!")
        # Display a file explorer dialog to choose a directory for saving the generated file
        save_directory = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File','','*.json')[0]

        # Open the files and do something with their contents
        make_train_data(self.file1_path,self.file2_path,save_directory)

        message_box = QtWidgets.QMessageBox(self)
        message_box.setWindowTitle('Success')
        message_box.setText('Processing completed successfully')
        message_box.exec_()

        self.reset_file_upload_boxes()





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FileProcessorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
