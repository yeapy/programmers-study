"""K번째수 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/42748
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""


def solution(array, commands):
    # TODO: 직접 작성한 풀이로 아래 예외를 교체하세요.
    raise NotImplementedError("아직 풀이를 작성하지 않았습니다.")


if __name__ == "__main__":
    # 공식 입출력 예: (함수에 전달할 인자 튜플, 기대 결과)
    test_cases = [(([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5, 6, 3])]
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
