def solution(progresses, speeds):
    answer = []
    count = 0
    k=0
    for i in range(len(progresses)):
        if progresses[i]<100:  
            while progresses[i]<100:

                for j in range(len(progresses)):

                    progresses[j] += speeds[j]
            count = 0
            k=i
            while progresses[k]>=100:
                count +=1
                if k<len(progresses)-1:
                    k+=1
                else:
                    break
            answer.append(count)  
            
        else:
            continue
    
    return answer