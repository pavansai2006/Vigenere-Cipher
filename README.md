# Vigenere-Cipher

Overview:

This project implements the Vigenère Cipher, a classical polyalphabetic substitution technique used for encrypting and decrypting text. The algorithm uses a keyword to shift letters in the plaintext, making it more secure than the simple Caesar cipher.

Features:

1. Encryption and decryption using a keyword.
2. Supports both uppercase and lowercase inputs.
3. Handles spaces and non-alphabetic characters gracefully.
4. Simple and efficient implementation for educational use.

Methodology:

1. Key Expansion: The provided key is repeated or truncated to match the length of the plaintext.
2. Encryption: Each letter of the plaintext is shifted based on the corresponding key character.
3. Decryption: Cipher text is reversed using the same key, recovering the original plaintext.

Applications:

1. Understanding classical cryptography techniques.
2. Educational demonstrations of polyalphabetic ciphers.
3. Foundation for learning modern encryption methods.

Example:

Plaintext: HELLO WORLD
Key: KEY
Ciphertext: RIJVS UYVJN
