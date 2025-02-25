# PROJECT-STEGNOGRAPHY
This project implements Least Significant Bit (LSB) steganography combined with AES encryption to securely hide and retrieve sensitive data within images. The encryption ensures that even if the hidden data is extracted, it remains unreadable without the correct decryption key.

How It Works?
1️ Encrypts the input message using AES.
2️ Converts encrypted text into binary format.
3️ Embeds binary data into the least significant bits (LSB) of image pixels.
4️ Saves the modified image (stego-image).
5️ Extracts the binary data, decrypts it, and retrieves the original message.

Security Considerations
1 Uses AES-256 encryption for data security.
2 Prevents steganographic analysis detection.
3 Only users with the correct AES decryption key can retrieve the message

Example Screenshots
1 Original vs. Stego Image (No visible difference)
2 Encrypted vs. Decrypted Message (Verifying security)
