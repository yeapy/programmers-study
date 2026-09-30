"""배열의 평균값 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/120817
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""


def solution(numbers):
    # TODO: 직접 작성한 풀이로 아래 예외를 교체하세요.
    raise NotImplementedError("아직 풀이를 작성하지 않았습니다.")


if __name__ == "__main__":
    # 공식 입출력 예: (함수에 전달할 인자 튜플, 기대 결과)
    test_cases = [(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],), 5.5), (([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],), 94.0)]
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
