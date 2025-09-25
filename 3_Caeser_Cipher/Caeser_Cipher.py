
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesorcipher(original_text, shift_value, encode_or_decode):
    output = ""
    if encode_or_decode == 'decode':
        shift_value *= -1
    for letter in original_text:
        if letter not in original_text:
            output += letter
        else:
            shifted_position = alphabets.index(letter) + shift_value
            shifted_position %= len(alphabets)
            output += alphabets[shifted_position]
    print(f"Here is {encode_or_decode}d result: {output}")
    
should_continue = True
while should_continue:
    user_choice = input("Type 'encode' to encrypt & 'decode' to decrypt:\n").lower()
    text = input("Type your message:").lower()
    shift = int(input("Type shift number:"))
    caesorcipher(original_text=text, shift_value = shift, encode_or_decode=user_choice)
    restart = input("Type yes if you want to do again, otherwise no\n").lower()
    if restart == 'no':
        should_continue = False
        print("See you later")





        