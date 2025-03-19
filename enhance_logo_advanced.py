import os
import sys
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

def download_esrgan_model():
    """
    Download the Real-ESRGAN model
    """
    try:
        import gdown
        import zipfile
        
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

def enhance_with_realesrgan(input_path, output_path, model_path=None):
    """
    Enhance image using Real-ESRGAN
    """
    try:
        from basicsr.archs.rrdbnet_arch import RRDBNet
        from realesrgan import RealESRGANer
        from realesrgan.archs.srvgg_arch import SRVGGNetCompact
        import cv2
        import torch
        
        # Set device (use CUDA if available)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {device}")
        
        # Load model
        if model_path and os.path.exists(model_path):
            print(f"Using model: {model_path}")
            # Create model (RRDBNet for x4 models)
            model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
            upsampler = RealESRGANer(
                scale=4,
                model_path=model_path,
                model=model,
                tile=0,  # tile size, 0 for no tile
                tile_pad=10,
                pre_pad=0,
                half=False,  # use half precision (fp16)
                device=device
            )
            
            # Read image
            img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
            if img is None:
                print(f"Cannot read image: {input_path}")
                return None
                
            # Upsample image
            try:
                output, _ = upsampler.enhance(img, outscale=4)
                cv2.imwrite(output_path, output)
                print(f"Real-ESRGAN enhanced image saved to {output_path}")
                return output_path
            except Exception as e:
                print(f"Error during upsampling: {str(e)}")
                return None
        else:
            print("Real-ESRGAN model not found")
            return None
    except ImportError as e:
        print(f"Required packages not installed: {str(e)}")
        print("Install Real-ESRGAN with:")
        print("pip install realesrgan basicsr facexlib torch opencv-python")
        return None

def main():
    # Input and output paths
    input_path = "logo ok.png"
    
    # Create output directory if it doesn't exist
    os.makedirs("enhanced", exist_ok=True)
    
    # Define output paths
    pillow_output = os.path.join("enhanced", "logo_4k_pillow.png")
    esrgan_output = os.path.join("enhanced", "logo_4k_realesrgan.png")
    
    # Enhance using Pillow (always available)
    enhance_with_pillow(input_path, pillow_output)
    
    # Try to enhance using Real-ESRGAN if available
    model_path = download_esrgan_model()
    if model_path:
        enhance_with_realesrgan(input_path, esrgan_output, model_path)
    
    print("\nEnhancement complete!")
    print("Check the 'enhanced' directory for your high-resolution images.")

if __name__ == "__main__":
    main() 