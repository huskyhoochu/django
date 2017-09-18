sample_list = list('abcd')
sample_dict = dict(name='Lux', champion_type='Magician')
print('program start')
try:
    print('check dict key')
    sample_dict['Sona']
    print('check list key')
    sample_list[5]
    #여기 이후로는 실행되지 않고 except로 넘어간다.
    print('after sample_list[5]')
except IndexError as e:
    print('sample_list[5] exception!')
    print(e)
except KeyError as e:
    print('sample_dict["Sona"] exception!')
    print(traceback.format_exc())
    print(e)

print('program terminated.')
