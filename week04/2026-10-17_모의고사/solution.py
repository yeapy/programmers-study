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
    size = len(answers)
    one = []
    two = []
    three = []
    i = 0
    while(i < size):
        one.append(i % 5 + 1)

        if i % 2 == 0:
            two.append(2)
        elif i % 8 == 1:
            two.append(1)
        elif i % 8 == 3:
            two.append(3)
        elif i % 8 == 5: 
            two.append(4)
        elif i % 8 == 7:
            two.append(5)

        if i % 10 == 0 or i % 10 == 1:
            three.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            three.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            three.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            three.append(4)
        elif i % 10 == 8 or i % 10 == 9:
            three.append(5)

        i += 1

    #print(one)
    #print(two)
    #print(three)
    # result_dict = {1 : 0, 2: 0, 3: 0}

    # for j in range(0,size):
    #     if (one[j] == answers[j]):
    #         result_dict[1] += 1
    #     if (two[j] == answers[j]):
    #         result_dict[2] += 1
    #     if (three[j] == answers[j]):
    #         result_dict[3] += 1

    results = [0,0,0]
    for j in range(0,size):
        if (one[j] == answers[j]):
            results[0] += 1
        if (two[j] == answers[j]):
            results[1] += 1
        if (three[j] == answers[j]):
            results[2] += 1

    #print(result)
    answer = []
    max_val = max(results)
    for idx, result in enumerate(results):
        if result == max_val:
            answer.append(idx + 1)
    
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
