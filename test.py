import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    salt_and_hash = salt + hash_obj
    return salt_and_hash.hex()  # Store as hex to ensure compatibility

def verify_password(stored_password, provided_password):
    try:
        salt_and_hash = bytes.fromhex(stored_password)  # Attempt to decode from hex
    except ValueError:
        print("Error: stored_password is not in hex format.")
        return False  # Handle the error by returning False for verification failure

    salt = salt_and_hash[:16]
    original_hash = salt_and_hash[16:]
    test_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    return test_hash == original_hash

# Test with sample data
test_password = "test123"
hashed = hash_password(test_password)
print(f"Hashed Password (hex): {hashed}")

# Attempt to verify the password
if verify_password(hashed, test_password):
    print("Password verification successful!")
else:
    print("Password verification failed.")
