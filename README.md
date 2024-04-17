
## Pattern Recognition Project: Image Compression with K-means Clustering

This project implements a GUI application for image compression using the K-means clustering algorithm.

**Features**

* **User-friendly Interface:** Select images and easily adjust compression settings.
* **K Selection:** Choose automatic K value selection or manually set the number of clusters (2-100). 
* **Visual Comparison:** View the original and compressed images side-by-side.
* **Detailed Statistics:** Get insights into compression effectiveness with color reduction and file size changes.
* **Performance Monitoring:** Track compression time for efficiency evaluation.
* **Informed K Selection (Optional):** Visualize the WCSS curve to make better decisions about the K value.
* **Theme Options:** Switch between light and dark themes for user preference.

**Installation**

1. **Python 3.x:** Ensure you have Python 3.x installed on your system.
2. **Required Libraries:** Install necessary libraries using pip:
    * `pip install PyQt5`
    * `pip install scikit-image` (usually includes NumPy)
    * `pip install qdarkstyle` (optional, dark theme)
    * `pip install matplotlib` (optional, WCSS curve & enlarged image)
3. **Download & Run:** Download the application script and run it to start the compression tool.

**Usage**

1. **Image Selection:** Click "Select Image" and choose a PNG, JPG, JPEG, or BMP image file for compression.
2. **K Value Selection:** Decide between automatic K selection or manually enter a value between 2 and 100 in the K textbox.
3. **Compression Initiation:** Click "Compress Image" to start the compression process.
4. **Results & Statistics:** The compressed image and detailed statistics (color reduction, file size changes) will be displayed.
5. **WCSS Curve (Optional):** Click "WCSS curve" to visualize the Within-Cluster Sum of Squares curve for informed K selection (requires matplotlib).
6. **Enlarged Image (Optional):** Click "Enlarge image" to see the original image full-size in a separate window (requires matplotlib).
7. **Theme Toggle:** Switch between light and dark themes for a more comfortable user experience.
8. **Exit Application:** Click "Quit" to close the image compression tool.

**Notes**

* K-means clustering reduces the number of colors in an image, potentially affecting image quality. 
* The optimal K value depends on the specific image and the desired balance between image quality and file size. Automatic selection might not always be ideal.
* The GUI is currently optimized for a screen resolution of 1920x1080. Functionality on other resolutions might be limited.

**Disclaimer**

This code is provided for educational purposes only and may contain bugs or limitations.

**Future Enhancements**

* Improve GUI responsiveness for various screen sizes.
* Integrate advanced image quality metrics for a more comprehensive evaluation of compression effectiveness.
