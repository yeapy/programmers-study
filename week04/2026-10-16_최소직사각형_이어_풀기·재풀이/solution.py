"""최소직사각형 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/86491
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""

'''
1. 명함 다 담을 수 잇는 거
2. 명함 눕힐 수 있음(가로 세로 바꿀 수 있다)
3. 그거의 가로 * 세로

명함을 눕힐 수 있으니 그중 가장 긴 값 구하고, 명함 중 가장 긴 값은 그거로 무마되니 작은 값 중 최대값을 구한다
'''

def solution(sizes):
    maximum = 0
    for size in sizes:
        if maximum < max(size):
            maximum = max(size)

    minimum = 0
    for size in sizes:
        if minimum < min(size):
            minimum = min(size)

    return maximum * minimum
    raise NotImplementedError("아직 풀이를 작성하지 않았습니다.")


if __name__ == "__main__":
    # 공식 입출력 예: (함수에 전달할 인자 튜플, 기대 결과)
    test_cases = [(([[60, 50], [30, 70], [60, 30], [80, 40]],), 4000), (([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],), 120), (([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]],), 133)]
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
