'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# DP: P(i,j) = true if S[i:j+1] is palindrome
# P(i,j) = P(i+1,j-1) and S[i] == S[j]
# ~O(n^2) in time, ~O(n^2) in space
def longest_palin_substr3(s):
    n = len(s)
    if n == 0: return ''
    P = {}
    for i in range(n): P[(i,i)] = True
    # k = j-i between 0 and n-1
    for k in range(n-1):
        for i in range(n):
            j = i+k
            if j >= n: continue
            if i+1 <= j-1:
                P[(i,j)] = P[(i+1,j-1)] and s[i] == s[j]
                print(P[(i,j)], i, j, k)
            else:
                P[(i,j)] = s[i] == s[j]
            
    start, end = max([k for k in P if P[k]], key=lambda x:x[1]-x[0])
    return s[start:end+1]


if __name__ == '__main__':
	__func__ = longest_palin_substr3
	# print __func__('cabcbaabac')
	print(__func__('abbaaa'))





