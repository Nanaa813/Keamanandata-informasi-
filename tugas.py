def vigenere_encrypt(plaintext, key):
        plaintext = plaintext.upper().replace(" ", "")
            key = key.upper()
                
                    ciphertext = ""
                        key_index = 0
                            
                                for char in plaintext:
                                        if char.isalpha():
                                                    p = ord(char) - ord('A')
                                                                k = ord(key[key_index % len(key)]) - ord('A')
                                                                            
                                                                                        c = (p + k) % 26
                                                                                                    ciphertext += chr(c + ord('A'))
                                                                                                                
                                                                                                                            key_index += 1
                                                                                                                                    else:
                                                                                                                                                ciphertext += char
                                                                                                                                                    
                                                                                                                                                        return ciphertext


                                                                                                                                                        # INPUT
                                                                                                                                                        plaintext = input("Masukkan plaintext: ")
                                                                                                                                                        key = input("Masukkan key: ")

                                                                                                                                                        # PROSES
                                                                                                                                                        ciphertext = vigenere_encrypt(plaintext, key)

                                                                                                                                                        # OUTPUT
                                                                                                                                                        print("Ciphertext:", ciphertext) 