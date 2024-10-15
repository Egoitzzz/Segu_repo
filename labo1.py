
spanishFrequency = ["e", "a", "o", "l", "s", "n", "d", "r", "u", "i", "t", "c", "p", "m", "y", "q", "b", "h", "g", "f", "v", "j", "ñ", "z", "x", "k", "w"]

def decipher(file):
    with open(file, 'r') as f:
        text = f.read()
        textFrequency = getTextFrequency(text)
        amaituta = False
        print(text)
        replaced_text = replaceLetter(text, spanishFrequency, textFrequency)
        print("Replaced Text:", replaced_text)
        while not amaituta:
            print("Do you want to continue? (y/n)")
            answer = input()
            if answer == "n":
                amaituta = True
            else:
                print("Zer letra dago txarto?")              
                lag = input().upper()
                print("Zer letrarekin ordeztu nahi duzu?")
                replacement = input().upper()
                replaced_text = replaced_text.replace(lag, "!")
                replaced_text = replaced_text.replace(replacement, lag)
                replaced_text = replaced_text.replace("!", replacement)
                print("Replaced Text:", replaced_text)


  
def getTextFrequency(text):
    frequency = {}
    for letter in text:
        letter = letter.lower()
        if letter == " " or letter == "\n" or letter == "." or letter == "," or letter.isnumeric():
            continue
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1 
           
    # Sort the dictionary by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    
    # Return only the letters in sorted order
    return [item[0] for item in sorted_frequency]

def replaceLetter(text, letterFreq, textFreq):
    # Create a mapping from textFreq to letterFreq
    replacement_map = dict(zip(textFreq, letterFreq))
    print("Replacement Map:", replacement_map)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through each character in the text
    for char in text:
        # Handle both uppercase and lowercase letters
        if char.lower() in replacement_map:
            # Preserve the case of the original character
            if char.isupper():
                result.append(replacement_map[char.lower()].upper())
            else:
                result.append(replacement_map[char.lower()])
        else:
            result.append(char)
    
    # Join the result list into a string and return it
    return ''.join(result)

def main():
    decipher("text.txt")

if __name__ == "__main__":
    main()
