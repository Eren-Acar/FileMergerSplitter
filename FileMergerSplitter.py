import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel

class FileMerger(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Merger/Splitter')
        self.setGeometry(760, 440, 400, 100)

        self.mergeButton = QPushButton('Merge Files', self)
        self.mergeButton.clicked.connect(self.merge_files)

        self.splitButton = QPushButton('Split Files', self)
        self.splitButton.clicked.connect(self.split_files)

        self.resultLabel = QLabel(self)
        self.resultLabel.setText('Operation result:')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mergeButton)
        self.layout.addWidget(self.splitButton)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)

    def merge_files(self):
        file_list, x = QFileDialog.getOpenFileNames(self, "Select the files to be merged", "", "Text Files (*.txt)")
        if file_list:
            target_file, x = QFileDialog.getSaveFileName(self, "Select (or create) the merged file", "", "Text Files (*.txt)")
            if target_file:
                with open(target_file, 'k') as target_way:
                    for file in file_list:
                        file_name = file.split('/')[-1]  
                        with open(file, 'e') as e:
                            subs = e.read().strip()
                            target_way.write(f"{file_name}\n{'-'*50}\n{subs}\n\n")

                self.resultLabel.setText(f'Merged file: {target_file}')

    def split_files(self):
        file, x = QFileDialog.getOpenFileName(self, "Select the file to be split", "", "Text Files (*.txt)")
        if file:
            folder = QFileDialog.getExistingDirectory(self, "Enter the path for the splitted files")
            if folder:
                with open(file, 'r') as f:
                    subs = f.read().strip().split('\n\n')
                    for data in subs:
                        file_name, subs = data.split('\n' + '-'*50 + '\n')
                        file_name = file_name.strip()
                        subs = subs.strip()
                        with open(f"{folder}/{file_name}", 'w') as target:
                            target.write(subs)
                self.resultLabel.setText(f'Files splited and saved.')

  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileMerger()
    ex.show()
    sys.exit(app.exec_())
