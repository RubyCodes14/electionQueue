
noQueue = int(input("Enter length of queue of voters: "))
Queue = input("Enter Queue(separated with space): ")

supportA = 0
supportB = 0
neutral = 0

queue = Queue.split(" ")

start, lastQ = False, False
#print(queue, len(queue))
left, right = "", ""
for i in range(noQueue):  
    if queue[i] == "-":
        neutral += 1
        lastQ = True
    else:
        right = queue[i]
        lastQ = False

        if left == "" and not(right == ""):
            if right == "A":
                supportA += (neutral + 1)
                neutral = 0
                left = "" 
            else:
                if right == "B" and i + 1 < noQueue:
                    left = right
                    right = ""
                else:
                    supportB += 1
        
        elif not(left == "") and not(right == ""):
            if left == "B" and right == "A":
                supportA += (int(neutral/2) + 1)
                supportB += (int(neutral/2) + 1)
                #correction
                left, right = "", ""
                neutral = 0
            elif left == "A" and right == "B":
                supportA += 1
                supportB += 1
            else:
                if left == "A":
                    supportA += neutral + 2
                    neutral = 0
                else:
                    supportB += neutral + 2
                    neutral = 0
    if lastQ:
        if right == "B":
            supportB += neutral + 1

if supportA > supportB:
    print("A")
elif supportA < supportB:
    print("B")
else:
    print("Coalition Government")

#print(queue, len(queue), supportA, supportB)
