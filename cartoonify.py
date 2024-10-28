# Import necessary libraries
import cv2
import numpy as np

# Function to show or save images based on the environment
def show_or_save_image(image, title):
    try:
        # Check if running in Google Colab
        from google.colab.patches import cv2_imshow
        cv2_imshow(image)  # Show image in Colab
    except ImportError:
        # Save image if not in Colab
        cv2.imwrite(f"{title}.jpeg", image)
        print(f"{title}.jpeg saved.")

# Main function
def cartoonize_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Check if the image was loaded correctly
    if img is None:
        print("Error: Could not load image. Please check the file path.")
        return
    
    # Step 1: Detect Edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Step 2: Cartoonize
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # Show or save the images
    show_or_save_image(img, "original_image")
    show_or_save_image(edges, "edges_image")
    show_or_save_image(cartoon, "cartoon_image")

# Run the program
cartoonize_image("screenshot.jpeg")  # Replace "screenshot.jpeg" with the path to your image
