from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import time
for i in range(11):
    print("Run: ",i)
    # Generate RSA keys
    start_time = time.perf_counter()
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    public_key = private_key.public_key()

    # Encrypt a message
    message = b'521H0438_NguyenTanBao_Essay'
    ciphertext = public_key.encrypt(message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Message: ", message)
    print("Message was encrypted to be ciphertext: ")
    print(ciphertext)
    # Decrypt the ciphertext
    plaintext = private_key.decrypt(ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Decrypted ciphertext to be a message: ")
    print(plaintext)
    end_time= time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Time to run this program are: {elapsed_time: .4f} second")


