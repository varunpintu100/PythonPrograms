def costToSwap(word1,word2):
    result=0
    l=len(word1)
    for i in range(0,l):
        result=result+ord(word1[i])-ord(word2[i])
    return result
def main():
    word1=input()
    word2=input()
    cost = costToSwap(word1, word2)
    print(cost)
main()