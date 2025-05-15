def encrypt(plaintext, key):
    ciphertext = []
    key = key.lower()
    key_length = len(key)
    
    for i in range(len(plaintext)):
        p_char = plaintext[i]
        k_char = key[i % key_length]
        
        if p_char.isalpha():
            base = ord('A') if p_char.isupper() else ord('a')
            shift = ord(k_char) - ord('a')
            encrypted_char = chr((ord(p_char) - base + shift) % 26 + base)
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p_char)
    
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    key = key.lower()
    key_length = len(key)

    for i in range(len(ciphertext)):
        c_char = ciphertext[i]
        k_char = key[i % key_length]

        if c_char.isalpha():
            base = ord('A') if c_char.isupper() else ord('a')
            shift = ord(k_char) - ord('a')
            decrypted_char = chr((ord(c_char) - base - shift) % 26 + base)
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c_char)
    
    return ''.join(plaintext)


key = input("Enter the key:       ")
plaintext = input("Enter the plaintext: ")
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("\nVigenere Cipher")
print("\nPlaintext:      ", plaintext)
print("Key:            ", key)
print("Ciphertext:     ", ciphertext)
print("Decrypted text: ", decrypted_text)


