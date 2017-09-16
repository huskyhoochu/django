sample = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]

def selection_sort(seq):
    new_seq = seq.copy()
    #인자로 받은 시퀀스를 새 변수에 복사한다.
    seq_len = len(new_seq)
    #시퀀스의 길이값을 갖는 변수를 만든다.

    for i in range(seq_len - 1):
        #0부터 전체 갯수-1만큼 i값을 증가시키며 순회
        print('루프[%d], 현재 리스트: %s' % (i, new_seq))
        min_index = i
        min_value = new_seq[min_index]
        print('루프[%d]의 최소 인덱스: %d, 최소값: %d' % (i, min_index, min_value))

        for j in range(i, seq_len):
            #순회 중인 i값부터 시작해서 시퀀스의 길이값까지를 다시 순회.
            #이렇게 해야 정렬을 마칠 때까지 계속 돌 수 있다.
            if new_seq[j] < min_value:
                #만일 j값을 인덱스로 갖는 시퀀스 값이 최소값보다 작다면
                print('인덱스[%d](%d)가 현재 최소값(%d)보다 작습니다. 최소값을 교체합니다.' % (j, new_seq[j], min_value))
                min_index = j
                min_value = new_seq[min_index]
                #최소 인덱스와 최소값을 현재값으로 바꾼다.

        print('%d차 내부 검사 완료. 최소값이 바뀌었다면 리스트의 맨 앞으로 보냅니다.' % (i+1))
        if i == min_index:
            #j 순회를 통해 최소 인덱스를 바꾼 다음 i 순회의 조건문을 실행한다.
            #i값과 최소 인덱스가 같다면, 즉 현재 검사하고 있는 값이 시퀀스 중에서 가장 작은 값이라면 통과한다.
            print('바꿀 내용이 없음\n')
        else:
            #그게 아니라면, 즉 i값이 최소 인덱스보다 크다면 교체를 벌인다.
            print('최소값이 바뀌었습니다. 인덱스[%d]와 인덱스[%d]를 교체합니다.\n' % (i, min_index))
            new_seq[i], new_seq[min_index] = new_seq[min_index], new_seq[i]

    return new_seq

if __name__ == '__main__':
    result = selection_sort(sample)
    print('start: ', sample)
    print('result: ', result)
