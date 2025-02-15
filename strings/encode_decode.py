def encode(strs):
    encoded = ''
    for word in strs:
        counter = {}
        length=0
        for char in word:
            if not char in counter:
                counter[char] = 0
            counter[char]+=1
            length+=1
        i = 0
        encoded += str(length) + '$'
        while i < length:
            char = word[i]
            dist = counter[char]
            encoded+=str(dist) + '^' + char
            i+=dist
    return encoded

def decode(word):
    output = []
    idx = 0
    length = len(word)
    while idx < length:
        len_word = ''
        while word[idx] != '$':
            len_word+=word[idx]
            idx+=1
        w = ''
        l = 0
        print('word forming -->',int(len_word))
        while l < int(len_word):
            char_len=''
            idx+=1
            while word[idx] != '^':
                char_len+=word[idx]
                idx+=1
            print('char length ->',char_len, word[idx+1])
            idx+=1
            w+=(word[idx]*int(char_len))
            print(w)
            l+=int(char_len)
            print(l)
        output.append(w)
        idx+=1
    return output
test = ["neet","code","love","you"]
en = encode(test)
print(en)
print(decode(en))

test_1 = [
    # Basic ASCII characters (0–127)
    "Hello, World!",  # Common greeting
    "abcXYZ123",       # Lowercase, uppercase, and digits
    "~!@#$%^&*()",     # Special characters
    "Tab\tLine",       # Tab and newline (special whitespace)
    "Space test ",     # Space character
    "1234567890",      # Digits

    # Extended ASCII (128–255)
    "éàöüçøñ¡",        # Accented characters and special symbols
    "¬£¥©®",           # Currency and legal symbols
    "ÿÑÜ",             # Extended Latin and special characters
    "ΓΔΘΛ",            # Greek letters

    # Multilingual Characters
    "السلام عليكم",    # Arabic greeting
    "Привет мир",      # Russian greeting
    "你好，世界",        # Chinese greeting
    "こんにちは世界",   # Japanese greeting
    "안녕하세요 세계",    # Korean greeting

    # Emojis
    "😀😃😄😁😆",        # Smiley faces
    "🐱🐶🦊",            # Animal emojis
    "🌍🌎🌏",            # Globe emojis
    "❤️💔💥",            # Heart and explosion emojis
    "🎉🎶",              # Party and music emojis

    # Additional Special Characters
    "©®™",             # Trademark and copyright symbols
    "✓✔✘✖",            # Check and X marks
    "💻📱🖥️",           # Tech-related emojis (laptop, phone, computer)
    "❤️🖤💜💙",          # Different heart emojis

    # Combined longer test string
    "Hello, World! éàöüçøñ¡ ¬£¥©® ÿÑÜ ΓΔΘΛ السلام عليكم Привет мир 你好，世界 こんにちは世界 안녕하세요 세계 😀😃😄😁😆 🐱🐶🦊 🌍🌎🌏 ❤️💔💥 🎉🎶 ©®™ ✓✔✘✖ 💻📱🖥️ ❤️🖤💜💙"
]
en = encode(test_1)
print(en)
x = decode(en)
print(x)
print(x == en)
