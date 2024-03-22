import importlib
import sys
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog, QStyleFactory
from PyQt5.QtGui import QBrush, QPainter, QPen, QColor, QFont, QPalette, QPixmap,QDesktopServices
# import serial
from PyQt5.QtCore import QUrl
# from PyQt5.QtCore import QProcess
import subprocess


# port = 'COM8'  # Replace with your Arduino's port (Windows: 'COM1', 'COM2', etc.)
# baud_rate = 9600  # Must match the Arduino's baud rate

# # Establish a connection to the Arduino
# ser = serial.Serial(port, baud_rate)

        

class Joystick(QWidget):
    
    
    def __init__(self, label_text, keys):
        super().__init__()

        self.joystick_x = 0
        self.joystick_y = 0
        self.keys = keys

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label_text)
        self.label.setStyleSheet("font-size: 26px; color: white;")
        layout.addWidget(self.label)

        self.setFocusPolicy(Qt.StrongFocus)

        self.pressed_keys = {}
        
        
        # self.connect_to_arduino()
        # def connect_to_arduino(self):
        
    
    

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the joystick widget
        outer_radius = min(self.width(), self.height()) / 2 - 10
        painter.setPen(QPen(Qt.white, 2))
        painter.setBrush(QColor(32, 33, 33))
        painter.drawEllipse(QRectF(self.rect()).center(), outer_radius, outer_radius)

        # Calculate the position of the joystick handle
        handle_radius = 27
        handle_x = int(self.width() / 2 + self.joystick_x * outer_radius)
        handle_y = int(self.height() / 2 + self.joystick_y * outer_radius)

        # Draw the joystick handle
        painter.setPen(QPen(Qt.white, 1))
        painter.setBrush(Qt.blue)
        painter.drawEllipse(handle_x - handle_radius, handle_y - handle_radius, handle_radius * 2, handle_radius * 2)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space:
            p='0'
            data = p.encode()
            print(p)
            #self.serial.write(data)
        if key in self.keys:
            self.pressed_keys[key] = True

        self.update_joystick_position()

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self.pressed_keys:
            del self.pressed_keys[key]

        self.update_joystick_position()

    def update_joystick_position(self):
        x = 0
        y = 0
        p='p'
        
        for key in self.keys:
            if key in self.pressed_keys:
                if key == Qt.Key_W:
                    y -= 0.1
                    p='s'
                elif key == Qt.Key_S:
                    y += 0.1
                    p="w"
                elif key == Qt.Key_A:
                    x -= 0.1
                    p="a"
                elif key == Qt.Key_D:
                    x += 0.1
                    p="d"
                elif key == Qt.Key_8:
                    y -= 0.1
                    p="8"
                elif key == Qt.Key_2:
                    y += 0.1
                    p="2"
                elif key == Qt.Key_4:
                    x -= 0.1
                    p="4"
                elif key == Qt.Key_6:
                    x += 0.1
                    p="6"
                elif key == Qt.Key_I:
                    y -= 0.1
                    p="i"
                elif key == Qt.Key_K:
                    y += 0.1
                    p="k"
                elif key == Qt.Key_J:
                    x -= 0.1
                    p="j"
                elif key == Qt.Key_L:
                    x += 0.1
                    p="l"
                elif key == Qt.Key_T:
                    y -= 0.1
                    p="t"
                elif key == Qt.Key_G:
                    y += 0.1
                    p="g"
                elif key == Qt.Key_F:
                    x -= 0.1
                    p="f"
                elif key == Qt.Key_H:
                    x += 0.1
                    p="h"
                else:
                    continue
                print(p)
                data = p
                print(data)
                ser.write(data.encode())  
               

        if not self.pressed_keys:  # No keys pressed, return to center
            x = 0
            y = 0 
        self.joystick_x = max(-1, min(x, 1))
        self.joystick_y = max(-1, min(y, 1))

        self.update()
        
    


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Joystick Control")
        self.setGeometry(100, 100, 800, 600)
        self.set_background_image("E:\Extra Curriculum\Competition\IEEE R10 Project Contest\Base\Python/pp.png")
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create the joysticks
        joystick1 = Joystick("Rover Movement", [Qt.Key_W, Qt.Key_A, Qt.Key_S, Qt.Key_D])
        joystick2 = Joystick("Camera ", [Qt.Key_8, Qt.Key_4, Qt.Key_6, Qt.Key_2])
        joystick3 = Joystick("Sh1-Sh2", [Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L])
        joystick4 = Joystick("Gripper", [Qt.Key_T, Qt.Key_F, Qt.Key_G, Qt.Key_H])

        # Create the button layout
        button_layout = QHBoxLayout()
        
        self.button1 = QPushButton(f"Stream")
        self.button1.setObjectName("button1")
        button_layout.addWidget(self.button1)
        self.button1.clicked.connect(self.run_ezviz)
        self.button1.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
        
        
        self.button2 = QPushButton(f"Disease Detect")
        self.button2.setObjectName("button2")
        button_layout.addWidget(self.button2)
        self.button2.clicked.connect(self.check_disease)
        self.button2.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
        
        
        self.button3 = QPushButton(f"GRAD-CAM Visualization")
        self.button3.setObjectName("button3")
        button_layout.addWidget(self.button3)
        self.button3.clicked.connect(self.grad_cam)
        self.button3.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
        
        
        self.button4 = QPushButton(f"Clear Directory")
        self.button4.setObjectName("button4")
        button_layout.addWidget(self.button4)
        self.button4.clicked.connect(self.clear_data)
        self.button4.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
        
        
        self.button5 = QPushButton(f"Arm_Lock")
        self.button5.setObjectName("button5")
        button_layout.addWidget(self.button5)
        self.button5.clicked.connect(self.button_arm_lock)
        self.button5.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
        
        
        self.button6 = QPushButton(f"Arm_Power")
        self.button6.setObjectName("button6")
        button_layout.addWidget(self.button6)
        self.button6.clicked.connect(self.button_arm_pow)
        self.button6.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
  
        self.button7 = QPushButton(f"Wheel_Power")
        self.button7.setObjectName("button7")
        button_layout.addWidget(self.button7)
        self.button7.clicked.connect(self.button_wheel_pow)
        self.button7.setStyleSheet("QPushButton {\n"
"color:rgb(240, 240, 240);\n"
"background-color:rgb(32, 33, 33);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-radius: 10px;\n"
"border-color:rgb(30, 65, 102);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(10, 4, 8);\n"
                          "}")
        
        
        # self.button8 = QPushButton(f"Stream")
        # buttons.append(button8)
        # button_layout.addWidget(self.button8)
        # self.button8.clicked.connect(self.button_ip_stream)
        
        
        # self.button9 = QPushButton(f"Stream")
        # buttons.append(button9)
        # button_layout.addWidget(self.button9)
        # self.button9.clicked.connect(self.button_ip_stream)
        
        




        # Create the text edit box
        # text_edit = QTextEdit()
        # text_edit.setMaximumHeight(50)
        # Add the joysticks, buttons, and text edit box to the layout
        layout.addWidget(joystick1)
        layout.addWidget(joystick2)
        layout.addWidget(joystick3)
        layout.addWidget(joystick4)
        layout.addLayout(button_layout)
        # layout.addWidget(text_edit)

        self.show()
        
    def set_background_image(self, image_path):
        pixmap = QPixmap(image_path)

        # Scale the pixmap to the size of the main window
        scaled_pixmap = pixmap.scaled(self.size())

        # Create a QPalette with the pixmap as the background
        palette = self.palette()
        palette.setBrush(QPalette.Background, QBrush(scaled_pixmap))

        # Set the updated palette as the main window's palette
        self.setPalette(palette)
        
    def run_ezviz(self,checked):
        app_path = r'"C:\Program Files (x86)\Ezviz Studio\EzvizStudio.exe"' # Replace with the actual path to your app's EXE file
        QDesktopServices.openUrl(QUrl.fromLocalFile(app_path))
        

    def check_disease(self,checked):
        subprocess.call(['python', 'E:\Research_Papers\Plant_disease\Grape_for_rover\Code\Python\check_image.py'])
        
    def grad_cam(self,checked):
        subprocess.call(['python', 'E:\Research_Papers\Plant_disease\Grape_for_rover\Code\Python\check_gradcam.py'])

    def clear_data(self,checked):

        def delete_images_in_folder(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")

# Provide the path to the folder containing the images
        folder_path = "E:\Extra Curriculum\Competition\IEEE R10 Project Contest\Ezviz Images\captrue"
        # Call the function to delete the images
        delete_images_in_folder(folder_path)
        # self.label.setText("Data Cleared!")


    def button_arm_lock(self,checked):
        p='b'
        data = p
        print(data)
        ser.write(data.encode())

    def button_arm_pow(self,checked):
        p='n'
        data = p
        print(data)
        ser.write(data.encode())

    def button_wheel_pow(self,checked):
        p='m'
        data = p
        print(data)
        ser.write(data.encode())



# def button_ip_stream(self,checked):
#     p=','

# def button_ip_stream(self,checked):
#     p='.s'


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set dark theme
    app.setStyle(QStyleFactory.create("Fusion"))
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)

    # Set font sizes
    font = QFont("Arial")
    font.setPointSize(14)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
