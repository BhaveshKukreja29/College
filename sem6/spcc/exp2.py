def count_lines(text):
    lines = text.count('\n')
    if text and not text.endswith('\n'):
        lines += 1
    print(f"Total lines: {lines}")


def count_words_chars(text):
    words = len(text.split())
    chars = len(text.replace('\n', ''))
    print(f"Total words: {words}")
    print(f"Total characters (excluding newlines): {chars}")


def identify_vowels_consonants(text):
    vowels = []
    consonants = []
    for ch in text:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
                vowels.append(ch)
            else:
                consonants.append(ch)
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")


def recognize_digits_alphabets(text):
    digits = []
    alphabets = []
    for ch in text:
        if ch.isdigit():
            digits.append(ch)
        elif ch.isalpha():
            alphabets.append(ch)
    print(f"Digits: {digits}")
    print(f"Alphabets: {alphabets}")


def count_digits(text):
    total = sum(1 for ch in text if ch.isdigit())
    print(f"Total digits: {total}")


print("Enter text (type 'END' on a new line to finish):")
lines = []
while True:
    line = input()
    if line.strip() == 'END':
        break
    lines.append(line)
text = '\n'.join(lines)

print("\n--- 1. Count Lines ---")
count_lines(text)

print("\n--- 2. Count Words and Characters ---")
count_words_chars(text)

print("\n--- 3. Vowels and Consonants ---")
identify_vowels_consonants(text)

print("\n--- 4. Digits and Alphabets ---")
recognize_digits_alphabets(text)

print("\n--- 5. Count Digits ---")
count_digits(text)
