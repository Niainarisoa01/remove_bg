import os
from PIL import Image, ImageEnhance, ImageFilter

def enhance_image(input_path, output_dir, sizes=None):
    """
    Enhance an image using Pillow
    
    Args:
        input_path: Path to the input image
        output_dir: Directory to save the enhanced images
        sizes: List of sizes to generate, if None uses default sizes
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Default sizes if none provided
    if sizes is None:
        sizes = [
            (1920, 1920),  # Full HD
            (2560, 2560),  # 2K
            (3840, 3840),  # 4K
        ]
    
    # Load the image
    try:
        original_img = Image.open(input_path)
        print(f"Original image size: {original_img.size}")
        print(f"Original image format: {original_img.format}")
        print(f"Original image mode: {original_img.mode}")
        
        # Convert to RGBA if it's not already (for transparency support)
        if original_img.mode != 'RGBA':
            original_img = original_img.convert('RGBA')
        
        # Process for each target size
        for size in sizes:
            # Get size name for file naming
            if size[0] == 1920:
                size_name = "FullHD"
            elif size[0] == 2560:
                size_name = "2K"
            elif size[0] == 3840:
                size_name = "4K"
            else:
                size_name = f"{size[0]}x{size[1]}"
            
            # Create base filename without extension
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(output_dir, f"{base_name}_{size_name}.png")
            
            # Resize with high quality
            img_resized = original_img.resize(size, Image.Resampling.LANCZOS)
            
            # Apply slight enhancements for better quality
            img_sharp = ImageEnhance.Sharpness(img_resized).enhance(1.2)
            
            # Save with high quality and DPI
            img_sharp.save(output_path, 'PNG', dpi=(300, 300), quality=95)
            print(f"Saved enhanced image: {output_path}")
    
    except Exception as e:
        print(f"Error processing image: {str(e)}")

def main():
    # Input file and output directory
    input_file = "logo ok.png"
    output_dir = "enhanced"
    
    # Process the image
    enhance_image(input_file, output_dir)
    print("\nEnhancement complete!")

if __name__ == "__main__":
    main() 