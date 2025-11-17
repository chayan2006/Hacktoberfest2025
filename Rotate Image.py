from PIL import Image

def rotate_image(input_path, output_path, angle):
    """
    Rotate an image by a given angle and save the result.
    """
    try:
        img = Image.open(input_path)
        rotated = img.rotate(angle, expand=True)
        rotated.save(output_path)
        print(f"✅ Image rotated by {angle}° and saved as {output_path}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    # Example usage
    rotate_image("input.jpg", "rotated.jpg", 90)
