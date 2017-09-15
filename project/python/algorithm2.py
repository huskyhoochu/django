def sequential_search_while(s, key):
    i = 0
    while i < len(key):
        if s == key[i]:
            return i
        else:
            i += 1
            continue
    return "만족하는 키가 없습니다."

def sequential_search_for(s, key):
    for i, k in enumerate(key):
        if s == k:
            return i

print(sequential_search_while('u','huskyhoochu'))
print(sequential_search_for('o','huskyhoochu'))
    
