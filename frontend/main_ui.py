import sys
import subprocess
import os # For path joining
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

# Adjust Python path to find backend modules
# This assumes the script is run from the root of the repository or that the structure is in PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.python.acquisition import AcquisitionModule


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Reconstruction Viewer")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Placeholder for 3D view
        self.placeholder_label = QLabel("3D View Placeholder", self)
        self.placeholder_label.setStyleSheet("border: 1px solid black; padding: 10px; font-size: 16px;")
        self.placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.placeholder_label)

        # Start Scan button
        self.start_scan_button = QPushButton("Start Scan", self)
        self.start_scan_button.clicked.connect(self.on_start_scan_clicked)
        layout.addWidget(self.start_scan_button)

        central_widget.setLayout(layout)

        # Initialize Acquisition Module
        self.acquisition_module = AcquisitionModule()
        # Define path to the mock rust runner - adjust if your structure is different
        # Assuming 'frontend' and 'backend' are sibling directories
        self.mock_rust_runner_path = os.path.join(
            os.path.dirname(__file__), # current dir (frontend)
            "..",                     # project root
            "backend", "rust", "mock_rust_runner.py"
        )


    def on_start_scan_clicked(self):
        self.placeholder_label.setText("Scanning...")
        QApplication.processEvents() # Update UI

        try:
            # 1. Get frame paths from acquisition module
            rgb_filepath, depth_filepath = self.acquisition_module.get_frames()
            self.placeholder_label.setText(f"Frames saved: {rgb_filepath}, {depth_filepath}\nRunning reconstruction...")
            QApplication.processEvents()

            # 2. Simulate calling Rust reconstruction engine
            # In a real scenario, this would be the path to the compiled Rust executable
            cmd = [sys.executable, self.mock_rust_runner_path, rgb_filepath, depth_filepath]

            # Run the command
            # We are in frontend/ folder, paths temp_rgb.npy and temp_depth.npy are in current working directory
            # which is the root of the repo if we run from root.
            # The acquisition module saves them to CWD.
            # The mock_rust_runner.py expects them to be accessible.
            process = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=".") # Run from repo root

            result_output = process.stdout.strip()
            self.placeholder_label.setText(result_output)

        except FileNotFoundError:
            self.placeholder_label.setText(f"Error: Mock runner script not found at {self.mock_rust_runner_path}")
        except subprocess.CalledProcessError as e:
            self.placeholder_label.setText(f"Error during reconstruction: {e.stderr}")
        except Exception as e:
            self.placeholder_label.setText(f"An unexpected error occurred: {str(e)}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
