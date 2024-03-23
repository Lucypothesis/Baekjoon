n = int(input()) 

for i in range(1, n+1):   
    num = sum((map(int, str(i))))  
    num_sum = i + num  
   
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
      
# num = list(map(int, str(i))) ← 이렇게 하면 216을 [2,1,6]으로 받을 수 있음. 2+1+6 하려면 sum(map(int, str(i))) 하면 됨
# str(i)를 몰라서 개고생을 했다는 걸 깨달았지만 여전히 뿌듯하긴 함 하하하
