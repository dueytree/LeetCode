# Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

# 입력받은 로그를 가독성 좋게 깔끔하게 정리하여 출력하기 원하는 문제다.
# 문자로 되어있는 로그가 숫자보다 더 앞으로 오고, 숫자 로그는 입력 순서대로 나온다.
# 문자와 숫자를 구별하고, 숫자는 뒤에 이어 붙인다. 숫자 로그든 문자로그든 둘다 문자열로 지정되어 있어
# isdigit 함수로 숫자 여부인지 판별한다. 판별한 이후 각각 빈 리스트에 넣어준 뒤 sort(lambda) 를 이용해
# 정렬한 뒤 마지막 두 값을 더해 return 해준다.

def reorderLogFiles(logs):
    char, num = [], []
    for element in logs:
        if element.split()[1].isdigit():
            num.append(element)
        else:
            char.append(element)
    char.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return char + num

def test_solution():
    assert reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]) == \
           ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    assert reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]) == \
           ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]