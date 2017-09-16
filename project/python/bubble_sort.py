sample = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]

def bubble_sort(seq):
    seq = seq.copy()
    len_seq = len(seq)
    #시퀀스의 길이 값을 변수로 잡는다.
    for i in range(len_seq - 1):
        #0부터 시퀀스 길이 값 -1 만큼을 순회한다.
        print("\n현재 시퀀스 상태 : ", seq)
        print("{}차 순회 시작.".format(i+1))
        for j in range(len_seq - i - 1):
            #순회 루틴 안에서 루틴을 돌아야 한다.
            if seq[j] > seq[j+1]:
                #시퀀스 앞 요소가 더 크면 요소를 바꾼다.
                print("{}가 {}보다 큽니다. 요소를 바꿉니다.".format(seq[j], seq[j+1]))
                seq[j], seq[j+1] = seq[j+1], seq[j]
                print(seq)

    return seq

if __name__ == '__main__':
    result = bubble_sort(sample)
    print('시작 : ', sample)
    print('완료 : ', result)
