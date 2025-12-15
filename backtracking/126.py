from collections import deque

def findLadders(beginWord: str, endWord: str, wordList: list) -> list[list[str]]:
    wordList = set(wordList)
    if endWord not in wordList:
        return []
    l = len(beginWord)
    local_min = float('inf')
    ans = []
    que = deque([(1,beginWord, beginWord)])
    while que:
        t,p,node = que.popleft()
        visited = set(p.split(','))
        n = node
        if n == endWord:
            if local_min > t:
                local_min = t
            if local_min == t:
                ans.append(p.split(','))
        for i in range(l):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = node[:i]+char+node[i+1:]
                if next_word in wordList and not next_word in visited:
                    que.append((t+1,p+','+next_word,next_word))
    return ans


test = [["hit","cog",["hot","dot","dog","lot","log","cog"]],['qa','sq',["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]]]
for t in test:
    print(findLadders(t[0],t[1],t[2]))


