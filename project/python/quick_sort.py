def quick_sort(seq, start, end):
    seq = seq.copy()
    #재귀함수이기 때문에 탈출 조건이 필요하다
    if start >= end:
        return

    #start와 end에 left, right 변수값을 준다.
    left = start
    right = end
    #정렬의 기준점이 되는 pivot값을 left와 right를 이용해 결정한다.
    #pivot은 시퀀스 인덱스의 중앙값으로 맞춘다.
    pivot = seq[(left + right) // 2]

    print("시작번호 : {}, 끝번호 : {}, 피벗 : {}".format(left, right, pivot))

    #left와 right가 교차할 때까지 순회
    while left <= right:
        print("\n순회 시작: {}\n".format(seq))
        #left의 데이터가 pivot보다 크거나 같으면 멈춘다.
        while seq[left] < pivot:
            print("좌측값 {}이 pivot {}보다 작습니다. 시작번호를 올립니다.".format(seq[left], pivot))
            left += 1
            print("시작번호 : {}, 끝번호 : {}".format(left, right))


        #right의 데이터가 pivot보다 작거나 같으면 멈춘다.
        while seq[right] > pivot:
            print("우측값 {}이 pivot {}보다 큽니다. 끝번호를 내립니다.".format(seq[right], pivot))
            right -= 1
            print("시작번호 : {}, 끝번호 : {}".format(left, right))


        #left와 right가 교차하지 않았다면 데이터를 맞교환
        if left <= right:
            print("pivot을 기준으로 {}과 {}를 교환합니다.".format(seq[left], seq[right]))
            seq[left], seq[right] = seq[right], seq[left]
            left += 1
            right -= 1
            print("교환한 숫자 안쪽을 비교하기 위해 시작번호와 끝번호를 좁힙니다.")
            print("시작번호 : {}, 끝번호 : {}".format(left, right))

        # quick_sort(seq, start, right)
        # quick_sort(seq, left, end)

    return seq


if __name__ == '__main__':
    sample = [3,1,0,2,4]
    result = quick_sort(sample, 0, len(sample) - 1)
    print("시작 : ", sample)
    print("완료 : ", result)
