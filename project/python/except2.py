sample = list('abcdefg')
loop = 0
while True:
    loop += 1
    try:
        input_num = int(input('숫자를 입력하세요 : '))
        sample[input_num]
    except IndexError as e:
        print('인덱스 오류!')
        print(e)
    except ValueError as e:
        print('숫자를 입력하세요!')
        print(e)
    else:
        print(sample[input_num])
    finally:
        print('%d번째 루틴 완료' % (loop))

