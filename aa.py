def min_swaps_together(s):
    num_knights=s.count('k')
    min_swaps=float('inf')
    for i in range(len(s)):
        window=s[i:]+s[:i]
        num_swaps=sum(1 for char in window[:num_knights] if char== 'D')
        min_swaps=min(min_swaps,num_swaps)
    return min_swaps
  t=int(input())
for i in range(t):
    input()
    s=input().strip()
    print(min_swaps_together(s))
