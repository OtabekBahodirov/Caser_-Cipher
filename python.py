def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

# Example usage:
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher_encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)


# caesar_cipher_encrypt funksiya: Bu funksiya shifrlangan matn yaratadi. U matn va o'zgaruvchanni qabul qiladi. Keyinchalik, matndagi har bir belgi uchun yangi belgini hisoblaydi va shifrlangan matnga qo'shadigan sikl yordamida ishlaydi.
#
# caesar_cipher_decrypt funksiya: Bu funksiya shifrlangan matnni unshifrlaydi. U shifrlangan matn va o'zgaruvchan miqdorini qabul qiladi. Shifrlangan matnni unshifrlash uchun caesar_cipher_encrypt funksiyasini ishlatadi, ammo o'zgaruvchan miqdorini manfiy qilib beradi.
#
# text va shift o'zgaruvchanlari: Bu o'zgaruvchanlar asosiy kod qismidagi matn va o'zgaruvchan miqdorini aniqlash uchun ishlatiladi.
#
# encrypted_text va decrypted_text o'zgaruvchanlari: Bu o'zgaruvchanlar shifrlangan va unshifrlangan matnni saqlash uchun ishlatiladi.
#
# print funktsiyalari: Shifrlangan va unshifrlangan matnni konsolga chiqaradi.
