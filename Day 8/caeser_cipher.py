from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_prompt = ""

def caesar(original_text, shift_amount, encode_decode):
    output = ""

    if encode_decode == "decode":
            shift_amount *= -1

    for shift_text in original_text:
        if shift_text not in alphabet:
            output += shift_text
        else:    
            output += alphabet[((alphabet.index(shift_text)) + shift_amount) % len(alphabet)]

    print(f"Here is the {encode_decode}d string: {output}")


print(logo)
while continue_prompt != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    continue_prompt = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

print("Goodbye!")

# def encrypt(original_text, shift_amount):
#     encoded = ""
#     for shift_text in original_text:
#         encoded += alphabet[((alphabet.index(shift_text)) + shift_amount) % len(alphabet)]

#     print(f"Here is the encoded string: {encoded}")

# def decrypt(original_text, shift_amount):
#     decoded = ""
#     for shift_text in original_text:
#         decoded += alphabet[((alphabet.index(shift_text)) - shift_amount) % len(alphabet)]

#     print(f"Here is the decoded string: {decoded}")