import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

N = int(input())


text = list(input())
M = len(text)
pre_text = text
same_char = text


for _ in range(N-1) :
    text = list(input())
    for i in range(len(text)) :
        if pre_text :
            if pre_text[i] == text[i] :
                if text[i] == same_char[i] :
                    same_char[i] = text[i]
                else :
                    same_char[i] =  '?'
            else :
                same_char[i] =  '?'
    
    pre_text = text

ans = ''.join(same_char)
print(ans)

