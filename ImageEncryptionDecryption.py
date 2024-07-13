import os

def xor_encrypt_decrypt(image_path, key):
    """Encrypt or Decrypt an image using XOR."""
    try:
        # Open the image file for reading
        with open(image_path, 'rb') as file:
            image_data = bytearray(file.read())

        # Perform XOR operation
        for index, value in enumerate(image_data):
            image_data[index] = value ^ key

        # Write the encrypted/decrypted data back to the file
        with open(image_path, 'wb') as file:
            file.write(image_data)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    try:
        # Get operation from user
        operation = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
        if operation not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            return

        # Get the image path from the user
        image_path = input("Enter the path of the image file: ").strip()
        if not os.path.isfile(image_path):
            print("The specified file does not exist.")
            return

        # Get the key from the user
        key = int(input("Enter the key for encryption/decryption (an integer): ").strip())

        # Confirm operation
        if operation == 'e':
            print(f"The path of the image file: {image_path}")
            print(f"Key for encryption: {key}")
        else:
            print(f"The path of the image file: {image_path}")
            print("Note: The encryption key and decryption key must be the same.")
            print(f"Key for decryption: {key}")

        # Perform encryption/decryption
        success = xor_encrypt_decrypt(image_path, key)
        if success:
            if operation == 'e':
                print("Encryption completed successfully.")
            else:
                print("Decryption completed successfully.")
        else:
            print("Operation failed.")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the key.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
