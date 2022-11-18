#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")

from Alphabets import alphabet


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            new_position = position - shift_amount
        else:
            new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the result: {end_text}")
