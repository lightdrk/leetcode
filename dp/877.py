'''
stone game

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


'''

'''
So, essentially we want to make it so... Okay, okay, that's a bit tricky. So, first thing I first thought I came to my mind is that we would need to check if Alice can get maximum number of stones. So, essentially she would be taking maximum at every point. But here's a catch. Like, if we do something like that, right? And we have a scenario where, let's say, we have an array which starts... Starting value is 5, 3, and last value is 5. Right? And as we know, Alice starts first. So, Alice takes 5 from, like, both sides are 5. So, essentially, like... And as I was thinking, Bob would take 3, but no. As it has said, like, both of them play optimally. That means Bob will also take maximum between starting and ending. That means Bob also takes 5. And in the end, only 3 left. That would be for Alice. So, that needs to be checked out. Here's, like, kind of an observation I'm talking about here.
[5,3,3,5] 
alice takes 5 [3,3,5]
bod takes 5 [3,3]

'''
'''
Interesting. Okay, so so essentially what we are doing here is this at every point we are taking maximum right and essentially we are adding we are adding Alice's choices and checking if we get maximum so here we could do some like from this alone I'm thinking of we could probably use DP here as we have only two choices to make either take first and second but we can also expand it towards greedy because in this choice we can produce an optimal choice because whatever we have that is greater between these two can or will always be taken


    '''

def stoneGame():
