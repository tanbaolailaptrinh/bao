import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import time
for i in range(10):
    print("Run:", i )
    start_time = time.perf_counter()
    # Generate a random key and initialization vector
    key = os.urandom(32)
    iv = os.urandom(16)

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Encrypt the plaintext
    plaintext = b"This is a secret message."
    padded_plaintext = plaintext + b"\0" * (16 - len(plaintext) % 16)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = padded_plaintext.rstrip(b"\0")

    print("Key:", key.hex())
    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())
    print("Plaintext:", plaintext.decode())
    end_time= time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Time to run this program are: {elapsed_time: .7f} second")
