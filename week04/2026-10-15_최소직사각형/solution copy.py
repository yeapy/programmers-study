"""최소직사각형 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/86491
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""


def solution(sizes):
    w = 0
    h = 0
    w_idx = 0
    h_idx = 0
    for idx, size in enumerate(sizes):
        if w < size[0]:
            w = size[0]
            w_idx = idx
        if h < size[1]:
            h = size[1]
            h_idx = idx
    
    # if w == h:
    #     return w * h


    if w > h:
        minimum = sizes[w_idx][1]
        for size in sizes:
            if min(size[0], size[1]) > minimum:
                minimum = min(size[0], size[1])

        return w * minimum

    else:
        minimum = sizes[h_idx][0]
        for size in sizes:
            if min(size[0], size[1]) > minimum:
                minimum = min(size[0], size[1])

        return h * minimum


    #raise NotImplementedError("아직 풀이를 작성하지 않았습니다.")


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
