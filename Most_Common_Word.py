# Most Common Word
# https://leetcode.com/problems/most-common-word/

# 이번 문제는 금지된 단어를 제외하고 가장 많은 횟수로 등장하는 단어를 찾는 문제다.
# 입력값에 대소문자, 쉼표 등이 섞여있어 입력값을 한번 전처리 해줘야 문제 해결이 수월해
# 정규식을 섞어 써야한다. 정규표현식을 공부하고 이 문제를 풀었다.
# 정규식에서 \w는 단어 문자를 뜻하고 ^은 not을 의미, 따라서 단어 문자가 아닌 모든 문자를 공백으로 치환하는 것이다.
# 소문자, 구두점을 제외하고 banned를 제외한 단어 목록이 list comprehension 조건에 저장된다.
# 갯수를 담아두는 변수는 딕셔너리를 사용하고 counter 모듈을 이용해 처리한다.


import collections
import re


def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

def test_solution():
    assert mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    assert mostCommonWord("a.", [])