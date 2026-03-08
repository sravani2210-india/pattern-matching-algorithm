text = input("Enter the main text: ")
pattern = input("Enter the pattern to search: ")

text_length = len(text)
pattern_length = len(pattern)

found = False

for i in range(text_length - pattern_length + 1):
    if text[i:i+pattern_length] == pattern:
        print("Pattern found at index:", i)
        found = True
        break

if not found:
    print("Pattern not found")
