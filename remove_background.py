import os
from rembg import remove
from PIL import Image

def remove_background(input_path, output_path=None):
    """
    Remove background from an image
    
    Args:
        input_path: Path to input image
        output_path: Path to save output image (optional)
    """
    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # If no output path specified, create one
    if output_path is None:
        filename = os.path.basename(input_path)
        name, _ = os.path.splitext(filename)
        # Always save as PNG to support transparency
        output_path = os.path.join('output', f"{name}_no_bg.png")
    
    # Load image
    input_image = Image.open(input_path)
    
    # Remove background
    print(f"Removing background from {input_path}...")
    output_image = remove(input_image)
    
    # Save image (always as PNG to support transparency)
    output_image.save(output_path, 'PNG')
    print(f"Image saved to {output_path}")
    return output_path

def process_directory(input_dir):
    """
    Process all images in a directory
    
    Args:
        input_dir: Directory containing images
    """
    # Supported image formats
    supported_formats = ['.png', '.jpg', '.jpeg', '.webp']
    
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(fmt) for fmt in supported_formats):
            input_path = os.path.join(input_dir, filename)
            remove_background(input_path)

def main():
    # Process single image
    input_image = "logo_01.png"  # Change this to your image path
    
    try:
        result_path = remove_background(input_image)
        print("\nBackground removal complete!")
        print(f"Check the 'output' directory for your processed image: {result_path}")
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        print("\nMake sure you have installed rembg:")
        print("pip install rembg")

if __name__ == "__main__":
    main() 