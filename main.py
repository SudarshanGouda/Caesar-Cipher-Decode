# Caser_Code
from Caser_function import caesar
from Alphabets import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)