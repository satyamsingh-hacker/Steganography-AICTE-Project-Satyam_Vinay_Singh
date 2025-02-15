import os
from PIL import Image
import stepic

def extract_text_from_image():
    # User se input lo
    image_path = input("Enter the path of the encoded image file: ").strip().replace('"', '')

    try:
        # Encoded image ko open karo
        img = Image.open(image_path)

        # Steganography ke through hidden text decode karo
        decoded_data = stepic.decode(img)

        # Decoded text ko print karo
        print("\n🔍 Extracted Hidden Text:")
        print("─────────────────────────")
        print(decoded_data)
        print("─────────────────────────")

    except FileNotFoundError:
        print("❌ Error: File not found. Check the file paths.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Function ko call karo
extract_text_from_image()
