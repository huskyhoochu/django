sample = [9,1,6,8,4,3,2,0,5,7]

def selection_sort(seq):
    #시작 리스트를 출력
    print('start :', seq)
    #정렬할 리스트의 길이
    seq_len = len(seq)
    #최소값과 최소값의 index 변수
    min_value = seq[0]
    min_index = 0
    #전체 리스트를 순회하며 최소값을 판단
    for i in range(seq_len):
        cur_item = sample[i]
        print('index[%d], value[%d]' % (i, cur_item))
        if cur_item < min_value:
            min_value = cur_item
            min_index = i
            print('index[%d]는 현재 min_value(%s)보다 작음.' % (i, min_value))
            print('변경된 min_value: %d' % min_value)
            print('변경된 min_index: %d' % min_index)
    #한 번의 순회 후 min_index와 맨 앞의 요소를 치환
    seq[0], seq[min_index] = seq[min_index], seq[0]
    return seq

def sequential_search(seq):
    seq_len = len(seq)
    #0부터 전체갯수 -1만큼 i값을 증가시키며 순회
    for i in range(seq_len-1):
        print('Loop[%d], Current list: %s' % (i, seq))
        min_index = i
        min_value = seq[i]
        print('Loop[%d]의 min_index: %d, min_value: %d' % (i, min_index, min_value))

        for j in range(i, seq_len):
            if seq[j] < min_value:
                print('index[%d](%d)는 현재 min_value(%d)' % (j, seq[j], min_value))
                min_index = j
                min_value = seq[min_index]
        
        if i == min_index:
            print('바꿀 내용이 없음')
        else:
            print('index[%d]와 index[%d]를 교체' % )
        seq[i], seq[min_index] = seq[min_index], seq[i]

print('start: ', seq)
print(

#selection_sort(sample)
sequential_search(sample)
