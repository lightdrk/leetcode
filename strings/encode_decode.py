def encode(strs):
    encoded = ''
    for word in strs:
        length=0
        prev = word[0]
        count = 0
        encode = ''
        for char in word:
            if prev != char:
                encode+=str(count) +'^'+prev
                prev = char
                count = 1
            else:
                count+=1
            length+=1
        encode = str(length) + '$' + encode + str(count) + '^' + prev
        encoded+=encode
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
        while l < int(len_word):
            char_len=''
            idx+=1
            while word[idx] != '^':
                char_len+=word[idx]
                idx+=1
            idx+=1
            w+=(word[idx]*int(char_len))
            l+=int(char_len)
        output.append(w)
        idx+=1
    return output
test = ["neet","code","love","you"]
en = encode(test)
print(en)
print(test == decode(en))
test_1 = [
    # Basic Latin Letters
    [['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']],
    
    # Digits
    [['I', 'have', '2', 'apples', 'and', '3', 'bananas']],
    
    # Space (representing space character within the sentence)
    [['This', 'is', 'a', 'sentence', 'with', 'a', 'space', 'character']],
    
    # Currency Symbols
    [['The', 'total', 'cost', 'is', '$50', '€40', '¥500', 'and', '£30']],
    
    # Punctuation Marks
    [['Hello', 'how', 'are', 'you', '?', 'I', 'am', 'doing', 'great', '!']],
    
    # Mathematical Symbols
    [['5', '+', '3', '=', '8', ',', 'and', '10', '÷', '2', '=', '5']],
    
    # Arrows
    [['Move', 'forward', '→', 'then', 'turn', 'left', '←', 'and', 'go', 'up', '↑']],
    
    # Greek Letters
    [['The', 'angle', 'θ', 'in', 'the', 'triangle', 'is', '90', '°']],
    
    # Emojis
    [['I', 'am', 'feeling', 'so', 'happy', 'today', '😀', '❤️']],
    
    # CJK (Chinese, Japanese, Korean) Characters
    [['This', 'is', 'a', 'Chinese', 'sentence', '我喜欢学习']],
    
    # Miscellaneous Symbols
    [['The', 'sun', '☀', 'is', 'shining', 'and', 'the', 'clouds', '☁', 'are', 'moving']],
    
    # Mathematical and Scientific Symbols
    [['The', 'sum', 'of', '∑', 'from', '1', 'to', '10', 'is', '55']],
    
    # Box-drawing Characters
    [['The', 'table', 'is', 'like', 'this', ':', '─┼┼┼┼┼┼║']]
]


for [test] in test_1:
    en = encode(test)
    print(en)
    x = decode(en)
    print(x)
    print(x == test)

t = utf8_char_list = [
    'The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog',  # Basic Latin Letters
    'I', 'have', '2', 'apples', 'and', '3', 'bananas',  # Digits
    'This', 'is', 'a', 'sentence', 'with', 'a', 'space', 'character',  # Space
    'The', 'total', 'cost', 'is', '$50', '€40', '¥500', 'and', '£30',  # Currency Symbols
    'Hello', 'how', 'are', 'you', '?', 'I', 'am', 'doing', 'great', '!',  # Punctuation Marks
    '5', '+', '3', '=', '8', ',', 'and', '10', '÷', '2', '=', '5',  # Mathematical Symbols
    'Move', 'forward', '→', 'then', 'turn', 'left', '←', 'and', 'go', 'up', '↑',  # Arrows
    'The', 'angle', 'θ', 'in', 'the', 'triangle', 'is', '90', '°',  # Greek Letters
    'I', 'am', 'feeling', 'so', 'happy', 'today', '😀', '❤️',  # Emojis
    'This', 'is', 'a', 'Chinese', 'sentence', '我喜欢学习',  # CJK Characters
    'The', 'sun', '☀', 'is', 'shining', 'and', 'the', 'clouds', '☁', 'are', 'moving',  # Miscellaneous Symbols
    'The', 'sum', 'of', '∑', 'from', '1', 'to', '10', 'is', '55',  # Mathematical and Scientific Symbols
    'The', 'table', 'is', 'like', 'this', ':', '─┼┼┼┼┼┼║',  # Box-drawing Characters
    
    # Adding more sentences and repetition for more than 1000 words
    'It', 'was', 'a', 'bright', 'and', 'sunny', 'day', '☀', 'as', 'we', 'watched', 'the', 'clouds', '☁', 'float', 'by', 'above', 'us', '.',
    'He', 'said', 'I', 'am', 'feeling', 'so', 'awesome', 'today', '😀', 'and', 'I', 'hope', 'you', 'do', 'too', '❤️', '.',
    'We', 'were', 'celebrating', 'the', 'birthday', 'of', 'our', 'friend', 'who', 'is', 'turning', '21', 'years', 'old', '.',
    'They', 'played', 'games', 'and', 'shared', 'stories', 'all', 'day', 'long', 'until', 'the', 'night', 'fell', 'down', '⚡', '.',
    'On', 'the', 'journey', 'to', 'the', 'mountain', 'we', 'found', 'a', 'small', 'village', 'where', 'everyone', 'was', 'helping', 'each', 'other', '.',
    'The', 'town', 'was', 'filled', 'with', 'smiles', 'as', 'they', 'worked', 'together', 'to', 'build', 'the', 'village', 'stronger', 'for', 'the', 'future', '.',
    'Some', 'people', 'walked', 'in', 'the', 'streets', 'while', 'others', 'enjoyed', 'the', 'art', 'on', 'the', 'walls', 'of', 'the', 'buildings', '🖼️', '.',
    'We', 'learned', 'so', 'much', 'about', 'the', 'local', 'culture', 'and', 'history', 'through', 'the', 'stories', 'and', 'traditions', 'of', 'the', 'village', '.',
    'There', 'was', 'a', 'festival', 'that', 'night', 'with', 'dancing', 'and', 'fireworks', '🎆', 'lighting', 'up', 'the', 'sky', 'and', 'making', 'everyone', 'cheer', 'with', 'joy', '.',
    'The', 'next', 'day', 'we', 'hiked', 'up', 'the', 'mountain', '⛰️', 'and', 'saw', 'an', 'incredible', 'view', 'of', 'the', 'valley', 'below', '.',
    'On', 'our', 'way', 'down', 'we', 'saw', 'a', 'herd', 'of', 'deer', 'running', 'through', 'the', 'forest', '🌳', 'and', 'we', 'stopped', 'to', 'watch', 'them', 'for', 'a', 'few', 'minutes', '.',
    'As', 'we', 'reached', 'the', 'bottom', 'of', 'the', 'mountain', 'we', 'realized', 'we', 'had', 'forgotten', 'to', 'bring', 'water', '💧', 'but', 'we', 'found', 'a', 'stream', 'and', 'drank', 'from', 'it', 'to', 'replenish', 'ourselves', '.',
    'We', 'finally', 'made', 'it', 'back', 'to', 'the', 'hotel', 'in', 'the', 'evening', 'and', 'relaxed', 'after', 'an', 'eventful', 'day', 'in', 'nature', '.',
    'The', 'next', 'morning', 'we', 'packed', 'our', 'bags', 'and', 'left', 'the', 'village', 'with', 'memories', 'that', 'would', 'last', 'a', 'lifetime', '.',
    'The', 'trip', 'was', 'so', 'memorable', 'that', 'I', 'still', 'talk', 'about', 'it', 'with', 'my', 'friends', 'whenever', 'I', 'see', 'them', '🗣️', '.',
    
    # Repeating for more words
    'The', 'students', 'were', 'learning', 'to', 'speak', 'French', 'and', 'Spanish', 'while', 'playing', 'games', 'and', 'having', 'fun', 'in', 'class', '.',
    'We', 'celebrated', 'the', 'holiday', 'with', 'family', 'and', 'friends', 'by', 'sharing', 'food', '🍽️', 'and', 'laughing', 'together', '.',
    'She', 'loved', 'to', 'read', 'books', 'about', 'history', 'and', 'philosophy', '📚', 'and', 'often', 'discussed', 'them', 'with', 'her', 'peers', '.',
    'They', 'brought', 'their', 'favorite', 'games', 'to', 'the', 'party', '🎉', 'and', 'everyone', 'enjoyed', 'playing', 'together', '.',
    'He', 'received', 'an', 'award', 'for', 'his', 'excellence', 'in', 'mathematics', 'and', 'science', '🔬', 'and', 'was', 'celebrated', 'by', 'his', 'teachers', '.',
    'The', 'kids', 'enjoyed', 'playing', 'outside', 'with', 'their', 'toys', 'and', 'pets', '🐶', 'all', 'day', 'long', '.',
    'They', 'ate', 'their', 'lunch', 'at', 'the', 'park', 'under', 'a', 'tree', '🌳', 'and', 'watched', 'the', 'clouds', 'float', 'by', '.',
    'The', 'team', 'practiced', 'hard', 'every', 'day', 'and', 'finally', 'won', 'the', 'championship', '🏆', 'after', 'months', 'of', 'training', '.',
    'The', 'weather', 'was', 'perfect', 'for', 'a', 'beach', 'trip', '🌊', 'and', 'we', 'spent', 'the', 'day', 'playing', 'in', 'the', 'sand', 'and', 'swimming', '.',
    'We', 'toured', 'the', 'city', 'and', 'visited', 'museums', '🎨', 'and', 'historical', 'sites', 'to', 'learn', 'about', 'the', 'past', '.',
    'In', 'the', 'evening', 'we', 'went', 'to', 'a', 'concert', '🎶', 'and', 'enjoyed', 'the', 'live', 'performance', 'under', 'the', 'stars', '✨', '.'
]
x  = encode(t)
print(x)
print(decode(x) == t)
