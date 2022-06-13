N,M = map(int,input().split())
S = [input() for i in range(2*N)]
rank = [[0,i] for i in range(2*N)]
# rank[i] = [x,y]  -> i位なのは -x勝で人y

print(rank)
def judge(a,b):
    # 引き分けなら-1,前者勝ちなら0,後者勝ちなら1
    if a==b: return -1
    if a=='G' and b=='P': return 1
    if a=='C' and b=='G': return 1
    if a=='P' and b=='C': return 1
    return 0

for j in range(M):
    print(rank)
    for i in range(N):
        player1 = rank[2*i][1]
        player2 = rank[2*i+1][1]
        result = judge(S[player1][j], S[player2][j])
        if result !=-1: rank[2*i+result][0] -= 1
    rank.sort()
print(rank)
for _,i in rank: print(i+1)
