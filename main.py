from skimage.color import rgb2lab, lab2rgb
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import numpy as np
import qdarkstyle
import time
import sys
import os


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Remove the window frame
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set the dark mode style
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.pointer = 0
        self.flag1 = False
        self.flag2 = False

        # Set window title and size
        self.setWindowTitle('Pattern Recognition')
        self.setGeometry(0, 0, 1850, 950)

        # Set window icon
        self.setWindowIcon(QIcon('Images/logo.png'))

        # Create labels to display the selected images
        self.res = QLabel(self)
        self.res.setGeometry(50, 100, 1500, 800)

        self.img = QLabel(self)
        self.img.setGeometry(20, 80, 800, 800)
        pixmap = QPixmap('Images/error-image.png')
        self.img.setPixmap(pixmap)
        self.img.setScaledContents(True)

        self.img_com = QLabel(self)
        self.img_com.setGeometry(830, 80, 800, 800)
        self.img_com.setPixmap(pixmap)
        self.img_com.setScaledContents(True)

        # Center window on screen
        self.center()

        # create widgets
        self.create_widgets()

    def center(self):
        # Get the screen geometry
        screen = QDesktopWidget().screenGeometry()

        # Calculate the center point
        center_x = (screen.width() - self.width()) // 2
        center_y = (screen.height() - self.height()) // 2

        # Move the window to the center
        self.move(center_x, center_y)

    def create_widgets(self):
        # layout for the main window
        layout = QVBoxLayout(self)

        # Add a label
        self.label = QLabel("Image Compression Project", self)
        self.label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignTop)

        # Add buttons
        self.txt = QLabel("K :", self)
        self.txt.setStyleSheet("font-size: 12pt;")
        self.txt.move(1650, 110)

        self.auto_k = QCheckBox("Auto", self)
        self.auto_k.move(1700, 110)
        self.auto_k.setChecked(True)
        self.auto_k.clicked.connect(self.check_k_button)

        self.k_input = QSpinBox(self)
        self.k_input.move(1650, 160)
        self.k_input.setMinimum(2)
        self.k_input.setMaximum(100)
        self.k_input.resize(175, 40)
        self.k_input.hide()
        self.k_input.setStyleSheet("font-size: 12pt;")

        self.select_file_button = QPushButton('Select Image', self)
        self.select_file_button.setStyleSheet("font-size: 12pt;")
        self.select_file_button.resize(175, 50)
        self.select_file_button.move(1650, 250)
        self.select_file_button.clicked.connect(self.select_file)

        self.compress_button = QPushButton('Compress Image', self)
        self.compress_button.setStyleSheet("font-size: 12pt;")
        self.compress_button.resize(175, 50)
        self.compress_button.move(1650, 350)
        self.compress_button.clicked.connect(self.kmeans)

        self.wcss_button = QPushButton('WCSS curve ', self)
        self.wcss_button.setStyleSheet("font-size: 12pt;")
        self.wcss_button.resize(175, 50)
        self.wcss_button.move(1650, 450)
        self.wcss_button.clicked.connect(self.wcss)

        self.Display_button = QPushButton('Enlarge image', self)
        self.Display_button.setStyleSheet("font-size: 12pt;")
        self.Display_button.resize(175, 50)
        self.Display_button.move(1650, 550)
        self.Display_button.clicked.connect(self.show_fig)

        self.close_button = QPushButton('Quit', self)
        self.close_button.setStyleSheet("font-size: 12pt;")
        self.close_button.resize(175, 50)
        self.close_button.move(1650, 650)
        self.close_button.clicked.connect(self.close)

        self.dark = QRadioButton("Dark mode", self)
        self.dark.move(1750, 880)
        self.dark.setChecked((True))
        self.dark.toggled.connect(self.setDark)

        self.light = QRadioButton("Light mode", self)
        self.light.move(1750, 910)
        self.light.toggled.connect(self.setLight)

    # Define a method to select an image
    def select_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')

        # If an image is selected, display it
        if self.filename:
            pixmap = QPixmap(self.filename)
            self.img.setPixmap(pixmap)
            self.img.setScaledContents(True)

            self.flag1 = True

            errcomimg = QPixmap('Images/error-compress.png')
            self.img_com.setPixmap(errcomimg)
            self.img_com.setScaledContents(True)

    # Define a method to perform K-means clustering on the image
    def kmeans(self):
        if self.flag1:
            loading = QPixmap('Images/loading.jpg')
            self.img_com.setPixmap(loading)
            self.img_com.setScaledContents(True)
            self.img_com.show()
            self.flag2 = True

            if self.auto_k.isChecked():
                kmean(self.filename)
            else:
                kmean(self.filename, self.k_input.value())

            com = QPixmap("Results/compressed_img.jpg")
            self.img_com.setPixmap(com)
            self.img_com.setScaledContents(True)

            self.orgi = QLabel(self)
            self.orgi.setText('Original Image ({} colors) (size: {:.2f} KB)'.format(org_colors, org_size))
            self.orgi.setGeometry(100, 890, 700, 50)
            self.orgi.setStyleSheet("font-size: 16pt; font-weight: bold;")
            self.orgi.show()
            self.pcom = QLabel(self)
            self.pcom.setText('Compressed Image ({} colors) (size: {:.2f} KB)'.format(n_clusters, compressed_img_size))
            self.pcom.setGeometry(950, 890, 700, 50)
            self.pcom.setStyleSheet("font-size: 16pt; font-weight: bold;")
            self.pcom.show()

            self.timetxt = QLabel("Time:", self)
            self.timetxt.setStyleSheet("font-size: 10pt;")
            self.timetxt.move(1650, 800)
            self.timetxt.show()
            self.tim = QLabel(self)
            self.tim.setText(f'{minutes} min {seconds} sec')
            self.tim.move(1650, 825)
            self.tim.setStyleSheet("font-size: 10pt;")
            self.tim.show()

    # Desplay the WCSS curve
    def wcss(self):
        if self.flag2:
            if self.pointer % 2 == 0:
                self.img.hide()
                self.img_com.hide()
                self.orgi.hide()
                self.pcom.hide()
                pixmap = QPixmap('Results/elbow_method.png')
                self.res.setPixmap(pixmap)
                self.res.setScaledContents(True)
                self.res.show()
                self.pointer += 1
            else:
                self.img.show()
                self.img_com.show()
                self.orgi.show()
                self.pcom.show()
                self.res.hide()
                self.pointer += 1

    # Define a function for checking the state of the radio button
    def check_k_button(self):
        if self.auto_k.isChecked():
            self.k_input.hide()
            self.wcss_button.setEnabled(True)
            return True
        self.k_input.show()
        self.wcss_button.setEnabled(False)
        return False

    def show_fig(self):
        plt.show()

    # Define a function for setting the dark theme
    def setDark(self):
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # Define a function for setting the light theme
    def setLight(self):
        self.setStyleSheet('')


org_colors, org_size, n_clusters, compressed_img_size, it, minutes, seconds = None, None, None, None, 1, 0, 0


def k_means_lab(X, k, max_iters=10):
    # Convert RGB image to Lab color space
    X_lab = rgb2lab(X)
    X_lab_flat = X_lab.reshape((-1, 3))  # (n_pixels, 3)

    # Initialize centroids randomly
    centroids = X_lab_flat[np.random.choice(X_lab_flat.shape[0], k, replace=False), :]  # (k, 3)

    for i in range(max_iters):
        # Assign each example to the nearest centroid
        distances = np.sqrt(((X_lab_flat - centroids[:, np.newaxis]) ** 2).sum(axis=2))  # (k, n_pixels, 3)
        labels = np.argmin(distances, axis=0)

        # Update centroids to be the mean of the examples assigned to them
        for j in range(k):
            if (X_lab_flat[labels == j, :].size == 0):
                # Re-initialize the centroid with a random data point
                centroids[j] = X_lab_flat[np.random.choice(X_lab_flat.shape[0], 1), :]
            else:
                centroids[j] = X_lab_flat[labels == j, :].mean(axis=0)

    # Convert back to RGB color space and reshape to image dimensions
    compressed_img_lab = centroids[labels].reshape(X_lab.shape)
    compressed_img = (np.clip(lab2rgb(compressed_img_lab), 0, 1) * 255).astype(np.uint8)

    # Calculate WCSS
    wcss = calculate_wcss_value(X_lab_flat, centroids, labels)
    return compressed_img, wcss


def calculate_wcss_value(X, centroids, labels):
    # Calculate the sum of squared distances of each data point from its closest cluster center
    distances = np.sqrt(((X - centroids[labels, :]) ** 2).sum(axis=1))
    wcss = (distances ** 2).sum()
    return wcss


def elbow_method(img, k_range):
    # Define the range of k values to test
    wcss_values = []

    for k in k_range:
        # Use K-means to compress the image and calculate WCSS
        _, wcss = k_means_lab(img, k)
        wcss_values.append(wcss)

    # Find the elbow point in the WCSS plot
    diffs = np.diff(wcss_values)
    elbow_point = np.argmin(diffs) + k_range[0]
    return elbow_point, wcss_values


def plot_WCSS_curve(k, wcss_values, k_range):
    # Plot the WCSS curve
    plt.plot(k_range, wcss_values, 'bx-')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS')
    plt.title(f'The Elbow Method - elbow point "optimal k" : {k}')
    plt.savefig('Results/elbow_method.png')
    # plt.show()


def comparison_images(img, path, compressed_img):
    global org_colors
    global org_size
    global n_clusters
    global compressed_img_size
    plt.close()
    org_size = os.path.getsize(path) / 1024
    org_colors = len(np.unique(img.reshape(-1, img.shape[2]), axis=0))
    plt.imsave("Results/compressed_img.jpg", compressed_img)
    compressed_img_size = os.path.getsize("Results/compressed_img.jpg") / 1024
    n_clusters = len(np.unique(compressed_img.reshape(-1, compressed_img.shape[2]), axis=0))

    # Plot the original and compressed images side by side
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(img)
    ax[0].set_title('Original Image ({} colors) (size: {:.2f} KB)'.format(org_colors, org_size))
    ax[1].imshow(compressed_img)
    ax[1].set_title('Compressed Image ({} colors) (size: {:.2f} KB)'.format(n_clusters, compressed_img_size))
    # plt.show()


def kmean(path, k=None):
    global it
    global minutes
    global seconds
    start_time = time.time()

    img = plt.imread(path)
    k_range = range(21, 31)
    if k is None:
        k, wcss_values = elbow_method(img, k_range)
        plot_WCSS_curve(k, wcss_values, k_range)
    compressed_img, _ = k_means_lab(img, k)

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"Task {it}:\nElapsed time: {minutes} minutes {seconds} seconds\n")
    it += 1

    comparison_images(img, path, compressed_img)


if __name__ == '__main__':
    # Create a QApplication instance
    app = QApplication(sys.argv)
    # Create an instance of our window
    window = MyWindow()
    # Show the window
    window.show()
    # Start the event loop and exit the application when the loop is finished
    sys.exit(app.exec_())
