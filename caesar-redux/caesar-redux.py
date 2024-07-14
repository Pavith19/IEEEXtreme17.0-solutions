def caesar_cipher_encrypt(ciphertext, shift): # ciphertext is the text to be encrypted, shift is the number of letters to shift by
    encrypted_text = ""
    
    for char in ciphertext: # iterate through each character in the ciphertext
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_cipher_decrypt(plaintext, shift): # plaintext is the text to be decrypted, shift is the number of letters to shift by
    decrypted_text = ""
    
    for char in plaintext: # iterate through each character in the plaintext
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.lower()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

num_msgs = int(input())

if 1 <= num_msgs <= 25:

    for i in range(num_msgs):
        shift = int(input())
        if 1 <= shift <= 25:
            text = input()
            if 1 <= len(list(text)) <= 300:
        
                if ' the ' in text:
                    encrypted_text = caesar_cipher_encrypt(text, shift)
                    print(encrypted_text)
                        
                if ' the ' not in text:
                    decrypted_text = caesar_cipher_decrypt(text, shift)
                    print(decrypted_text)
            

    
