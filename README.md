#  Brain Tumor Detection using OpenCV

This project uses OpenCV to process an MRI brain scan and highlight the tumor area using adaptive thresholding and contour detection. By reading and running code, you can see my development process.

## How to Run
Run the script with the path to an MRI image (grayscale or color) as a command-line argument:

``` python tumor_detection.py ./tumor_images/tumor_8.png ```

## How it Works
    1. Preprocessing
        -  Applies median blur to reduce noise.
    2. Adaptive Thresholding
        - Uses both mean and Gaussian adaptive methods.
        - Fine-tunes parameters (block size & C value) for better contrast of tumor region.
        - Inverts binary result so tumor appears white.
    3. Contour Detection
        -  Detects external contours in the thresholded image.
        - Draws green contours on the original image to highlight detected tumor region(s).
    4. Visualization
        - Displays preprocessing, thresholding, and final tumor-highlighted results.
    
## Requirements
- Python 3.x
- OpenCV
- NumPy
- Matplotlib

Install dependencies:

``` pip install opencv-python numpy matplotlib ```

## Challenges:
- Choosing statistical operator - Mean or Gaussian
- Tuning parameters - depending on image, block and C, might need to adjust until tumor is outlined
- Inverting depending if white tumor on black background

## Resources
Links that helped me understand:
- https://encord.com/blog/image-thresholding-image-processing/
- https://youtu.be/9-8Js62wzQs?si=4ghw_7QmAnJ-yu15
- https://youtu.be/DcWrbsPJEd8?si=azYxqe3YTT2jsOAT
- https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
