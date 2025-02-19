import cv2
import numpy as np

def encrypt_image(image_path, key=42):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read image!")
        return
    
    encrypted_img = img.copy()
    
    encrypted_img = encrypted_img ^ key 
    
    encrypted_path = "encrypted_image.png"
    cv2.imwrite(encrypted_path, encrypted_img)
    print(f"Encrypted image saved as {encrypted_path}")

def decrypt_image(image_path, key=42):
    encrypted_img = cv2.imread(image_path)
    if encrypted_img is None:
        print("Error: Unable to read image!")
        return

    decrypted_img = encrypted_img ^ key 

    decrypted_path = "decrypted_image.png"
    cv2.imwrite(decrypted_path, decrypted_img)
    print(f"Decrypted image saved as {decrypted_path}")

encrypt_image("image.jpg") 
decrypt_image("encrypted_image.png") 