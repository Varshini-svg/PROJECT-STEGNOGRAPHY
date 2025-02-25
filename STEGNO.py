import cv2
import os
import string

# Read the input image
img = cv2.imread("C:\Users\varsh\Pictures\Screenshots\Screenshot 2025-02-25 204454.png")  
# Replace with the correct image path

# Take secret message and passcode as input from the user
msg = input("ENTER SECRET MESSAGE: ")
password = input("ENTER A PASSCODE: ")

# Create dictionaries for character-to-ASCII and ASCII-to-character mapping
d = {}  # Dictionary to store character to ASCII mapping
c = {}  # Dictionary to store ASCII to character mapping

for i in range(255):
    d[chr(i)] = i  # Assign ASCII value to each character
    c[i] = chr(i)  # Assign character to each ASCII value

# Initialize pixel position variables
m = 0
n = 0
z = 0

# Encrypt and store message inside the image pixels
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Store ASCII value of message character in pixel
    n = n + 1  # Move to the next pixel row
    m = m + 1  # Move to the next pixel column
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image automatically (for Windows)
os.system("start encryptedImage.jpg")  

# Initialize variables for message extraction
message = ""
n = 0
m = 0
z = 0

# Take input passcode for decryption
pas = input("ENTER PASSCODE FOR DECRYPTION: ")

# Check if the entered passcode matches the original one
if password == pas:
    # Extract and reconstruct the hidden message
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]  # Retrieve ASCII value and convert to character
        n = n + 1  # Move to the next pixel row
        m = m + 1  # Move to the next pixel column
        z = (z + 1) % 3  # Cycle through RGB channels
    print("DECRYPTED MESSAGE:", message.upper())  # Print the retrieved message in uppercase
else:
    print("YOU ARE NOT AUTHORIZED")  # Print access denied message if passcode is incorrect
