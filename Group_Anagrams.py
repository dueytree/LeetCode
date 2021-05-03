# Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# 애너그램은 문자열을 재배열해서 다른 뜻을 가진 단어로 바꾸는 것을 말한다.
# 애너그램을 판별하는 방법은 정렬하여 비교하는 것이 가장 간단해 보인다. 정렬하는 방법은 sorted 함수를 사용해 준다.
# 정렬되어 나온 값은 리스트 형태이기 때문에 join 으로 합쳐서 이 값을 키로 딕셔너리를 만들어 준다.
# 만약 없는 키를 넣어줄 경우 keyerror가 생겨 에러가 나지 않도록 defaultdict()으로 정리하고,
# 매번 키 여부를 확인하지 않고 간단하게 해결한다.

import collections


def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

def test_solution():
    assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) != [["bat"], ["nat","tan"], ["ate", "eat", "tea"]]
    assert groupAnagrams([""]) != [[""]]
    assert groupAnagrams(["a"]) != [["a"]]