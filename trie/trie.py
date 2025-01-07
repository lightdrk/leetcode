class TrieNode:
    def __init__(self):
        self.child = [None] *128
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self,word):
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if node.child[index] is None:
                node.child[index] = TrieNode()
            node = node.child[index]
        node.end = True

    def search(self, word):
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if node.child[index] is None:
                return False
            node = node.child[index]
        return node.end

    def starts_with(self,prefix):
        node = self.root
        for char in prefix:
            index = self._char_to_index(char)
            if node.child[index] is None:
                return False
            node = node.child[index]
        return True

class TrieNoDe:
    def __init__(self):
        self.child = {}
        self.end = False


class TriE:
    def __init__(self):
        self.root = TrieNoDe()

    def insert(self, word):
        node = self.root
        for char in word:
            if not node.child.get(char):
                node.child[char] = TrieNoDe()
            node = node.child[char]
        node.end = True

    def search(self, word):
        node = self.root
        for char in word:
            if not node.child.get(char):
                return False
            node = node.child[char]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if not node.child.get(char):
                return False
            node = node.child[char]
        return True


words = ["mono", "dict", "hello", "thor", "repo", "dump", "!@#$0"]
print(f"words List {words}")
print("Trie with Array []")
t1 = Trie()

for word in words:
    t1.insert(word)

print("Testing ...")
for word in words:
    print(f"'{word}' inTrie ?", t1.search(word))
    print(f"['{word[:2]}'] isPrefix ?", t1.starts_with(word[:2]))

print()

print("Trie with dict {}")
t2 = TriE()

for word in words:
    t2.insert(word)

print("Testing ...")
for word in words:
    print(f"['{word}'] inTrie ?", t2.search(word))
    print(f"[{word[:2]}] isPrefix ?", t2.starts_with(word[:2]))

print()

print(t1.search("xan"))
print(t2.search("xan"))

