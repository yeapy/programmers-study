"""모의고사 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/42840
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""

'''
1번: 1 2 3 4 5 순서대로임
2번: 2 1 / 2 3 / 2 4 / 2 5 / 2 1/// 이 순서임
3번: 3 1 2 4 5 두번씩 이 순서임

배열 크기만큼 규칙 이용해 배열 만들기
각 사람별 정답 횟수 담은 변수 만들기
'''
def solution(answers):

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    result = [0,0,0]
    
    for i in range(len(answers)):
        if (answers[i] == one[i % len(one)]):
            result[0] += 1
            
        if (answers[i] == two[i % len(two)]):
            result[1] += 1
        
        if (answers[i] == three[i % len(three)]):
            result[2] += 1
            
    max_val = max(result)
    answer = []
    
    for idx, val in enumerate(result):
        if val == max_val:
            answer.append(idx+1)
            
    
    return answer

    raise NotImplementedError("아직 풀이를 작성하지 않았습니다.")


if __name__ == "__main__":
    # 공식 입출력 예: (함수에 전달할 인자 튜플, 기대 결과)
    test_cases = [(([1, 2, 3, 4, 5],), [1]), (([1, 3, 2, 4, 2],), [1, 2, 3])]
    for index, (args, expected) in enumerate(test_cases, start=1):
        try:
            actual = solution(*args)
        except NotImplementedError as error:
            print(f"미구현: {error}")
            break
        print(f"예제 {index}: 결과={actual!r}, 기대값={expected!r}")
        assert actual == expected, f"예제 {index} 실패"
    else:
        print("공식 예제 통과 (정답 제출 결과와는 별개)")
