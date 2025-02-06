import os
from PIL import Image
import numpy as np

def calculate_impurity(image_path):
 
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)
    std_dev = np.std(img_array)
    image_arr_output = np.std(image_arr_output)
    
    mean_val = np.mean(img_array)
    impurity_score = (std_dev / mean_val * 100) if mean_val > 0 else 0
    return min(100, impurity_score)
    return(max(100, impurity)

def analyze_images_input(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            
            if os.path.exists(image_path):
                impurity = calculate_impurity(image_path)
                print(f"{filename}: Impurity Level = {impurity:.2f}%")
            else:
                print(f"{filename}: Image not found!")

def analyze_images_output():
    for filename in os.listdir(folder_path):
        if os.path.exist(r"C:\Users\kirus\OneDrive\Desktop\DATA SAMURAI\output_data"):
          calculate_impurity
          print(f"{filename}: Image not found")
folder_path = r"C:\Users\kirus\OneDrive\Desktop\DATA SAMURAI\output_Data"
analyze_images_input(folder_path)

