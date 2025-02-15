import os
from PIL import Image
import stepic

def hide_text_in_image():
    # Get user inputs
    image_path = input("Enter the path of the image file: ").strip().replace('"', '')
    text_file_path = input("Enter the path of the text file: ").strip().replace('"', '')
    output_image_path = input("Enter the name for the output image (with .png extension): ").strip().replace('"', '')

    try:
        # Open the image
        img = Image.open(image_path)

        # Check if the image is in RGB, RGBA, or CMYK mode
        if img.mode not in ["RGB", "RGBA", "CMYK"]:
            print(f"⚠️ Image is in '{img.mode}' mode. Converting to RGB...")
            img = img.convert("RGB")

        # Read the text file data
        with open(text_file_path, "r") as file:
            text_data = file.read().encode()

        # Encode the text into the image
        encoded_img = stepic.encode(img, text_data)

        # Save the encoded image
        encoded_img.save(output_image_path, "PNG")

        print(f"✅ Text successfully hidden in '{output_image_path}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Check the file paths.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Call the function
hide_text_in_image()
