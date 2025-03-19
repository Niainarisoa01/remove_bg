import os
import sys
import numpy as np
from PIL import Image
import torch

def enhance_with_pillow(input_path, output_path, target_size=(3840, 3840)):
    """
    Enhance image resolution using Pillow's resizing capabilities
    """
    img = Image.open(input_path)
    original_size = img.size
    print(f"Original image size: {original_size}")
    
    # Resize with high quality
    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
    
    # Save with high quality and DPI
    img_resized.save(output_path, dpi=(300, 300), quality=95)
    print(f"Pillow enhanced image saved to {output_path}")
    return output_path

def download_esrgan_model():
    """
    Download the Real-ESRGAN model
    """
    try:
        import gdown
        
        model_dir = "models"
        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir, "RealESRGAN_x4plus.pth")
        
        if not os.path.exists(model_path):
            print("Downloading Real-ESRGAN model...")
            url = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"
            gdown.download(url, model_path, quiet=False)
            print(f"Model downloaded to {model_path}")
        
        return model_path
    except ImportError:
        print("gdown not installed. Install with 'pip install gdown'")
        return None

def enhance_with_opencv(input_path, output_path):
    """
    Alternative enhancement using OpenCV with edge-preserving filters
    """
    try:
        import cv2
        
        # Read the image
        img = cv2.imread(input_path)
        if img is None:
            print(f"Cannot read image: {input_path}")
            return None
        
        # Convert BGR to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Apply edge-preserving filter (detail enhancement)
        img_enhanced = cv2.detailEnhance(img_rgb, sigma_s=10, sigma_r=0.15)
        
        # Resize with bicubic interpolation to 4K
        height, width = img.shape[:2]
        target_size = (3840, 3840)
        img_resized = cv2.resize(img_enhanced, target_size, interpolation=cv2.INTER_CUBIC)
        
        # Convert back to BGR for saving
        img_bgr = cv2.cvtColor(img_resized, cv2.COLOR_RGB2BGR)
        
        # Save the image
        cv2.imwrite(output_path, img_bgr)
        print(f"OpenCV enhanced image saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error with OpenCV enhancement: {str(e)}")
        return None

def apply_unsharp_mask(input_path, output_path):
    """
    Apply unsharp mask filter to enhance details
    """
    try:
        from PIL import ImageFilter
        
        # Open the image
        img = Image.open(input_path)
        
        # Resize to 4K
        img_resized = img.resize((3840, 3840), Image.Resampling.LANCZOS)
        
        # Apply unsharp mask
        img_sharpened = img_resized.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        
        # Save the image
        img_sharpened.save(output_path, dpi=(300, 300), quality=95)
        print(f"Unsharp mask enhanced image saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error applying unsharp mask: {str(e)}")
        return None

def main():
    # Input and output paths
    input_path = "logo ok.png"
    
    # Create output directory if it doesn't exist
    os.makedirs("enhanced", exist_ok=True)
    
    # Define output paths
    pillow_output = os.path.join("enhanced", "logo_4k_pillow.png")
    opencv_output = os.path.join("enhanced", "logo_4k_opencv.png")
    unsharp_output = os.path.join("enhanced", "logo_4k_unsharp.png")
    
    print("Starting enhancement with multiple methods...")
    
    # Enhance using Pillow (always available)
    enhance_with_pillow(input_path, pillow_output)
    
    # Try to enhance using OpenCV with detail enhancement
    enhance_with_opencv(input_path, opencv_output)
    
    # Apply unsharp mask for additional detail enhancement
    apply_unsharp_mask(input_path, unsharp_output)
    
    print("\nEnhancement complete!")
    print("Check the 'enhanced' directory for your high-resolution images.")
    print("\nAvailable enhanced versions:")
    print(f"1. Basic resize: {pillow_output}")
    print(f"2. Detail enhancement: {opencv_output}")
    print(f"3. Sharpened version: {unsharp_output}")

if __name__ == "__main__":
    main() 