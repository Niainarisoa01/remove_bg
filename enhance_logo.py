import os
import numpy as np
from PIL import Image

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

def enhance_with_superres(input_path, output_path, model_path=None):
    """
    Enhance image using OpenCV's Super Resolution models
    """
    try:
        import cv2
        
        # Read the image
        img = cv2.imread(input_path)
        
        # Create the super resolution object
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        
        # Check if a model path was provided, otherwise use default path
        if model_path and os.path.exists(model_path):
            # Load the model
            model_name = os.path.basename(model_path).split('_')[0].lower()
            scale = int(os.path.basename(model_path).split('_x')[1].split('.')[0])
            sr.readModel(model_path)
            sr.setModel(model_name, scale)
            
            # Upscale the image
            result = sr.upsample(img)
            
            # Save the upscaled image
            cv2.imwrite(output_path, result)
            print(f"Super-resolution enhanced image saved to {output_path}")
            return output_path
        else:
            print("Super-resolution model not found, skipping this method")
            return None
    except ImportError:
        print("OpenCV or dnn_superres module not available, skipping this method")
        return None

def main():
    # Input and output paths
    input_path = "logo ok.png"
    
    # Create output directory if it doesn't exist
    os.makedirs("enhanced", exist_ok=True)
    
    # Define output paths
    pillow_output = os.path.join("enhanced", "logo_4k_pillow.png")
    superres_output = os.path.join("enhanced", "logo_4k_superres.png")
    
    # Enhance using Pillow (always available)
    enhance_with_pillow(input_path, pillow_output)
    
    # Try to enhance using super-resolution if available
    enhance_with_superres(input_path, superres_output)
    
    print("\nEnhancement complete!")
    print("Check the 'enhanced' directory for your high-resolution images.")

if __name__ == "__main__":
    main() 