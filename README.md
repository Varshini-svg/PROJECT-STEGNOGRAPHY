# PROJECT-STEGNOGRAPHY
This project implements Least Significant Bit (LSB) steganography combined with AES encryption to securely hide and retrieve sensitive data within images. The encryption ensures that even if the hidden data is extracted, it remains unreadable without the correct decryption key.

How It Works?
Encrypts the input message using AES.
Converts encrypted text into binary format.
Embeds binary data into the least significant bits (LSB) of image pixels.
Saves the modified image (stego-image).
Extracts the binary data, decrypts it, and retrieves the original message.

Security Considerations
Uses AES-256 encryption for data security.
Prevents steganographic analysis detection.
Only users with the correct AES decryption key can retrieve the message

Example Screenshots
Original vs. Stego Image (No visible difference)
Encrypted vs. Decrypted Message (Verifying security)
