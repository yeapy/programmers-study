"""최소직사각형 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/86491
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""


def solution(sizes):
    # TODO: 직접 작성한 풀이로 아래 예외를 교체하세요.
    # for idx,size in enumerate(sizes):
    #     if idx == 0:
    #         max_w = size[0]
    #         max_h = size[0]
    #         continue
    #     if max_w < size[0]:
    #         max_w = size[0]
    #         # w_idx = idx
    #     if max_h < size[1]:
    #         max_h = size[1]
    #         # h_idx = idx



    # w_idx = sorted(sizes, key = lambda x: (-x[0], -x[1]))
    # h_idx = sorted(sizes, key = lambda x: (-x[1], -x[0]))
    # max_w = 0
    # max_h = 0
    # if w_idx[max_w][0] == h_idx[max_h][1]:
    #      return w_idx[max_w][0] * h_idx[max_h][1]
    
    # if w_idx[max_w][0] > h_idx[max_h][1]:
    #     maximum = w_idx[max_w][0]
    #     minimum = w_idx[max_w][1]
    #     max_w += 1
    #     for idx in (max_w, len(w_idx) - 1):
    #         if min(w_idx[idx][0], w_idx[idx][1]) > minimum:
    #             minimum = min(w_idx[idx][0], w_idx[idx][1])
    #     return maximum * minimum

    # if w_idx[max_w][0] < h_idx[max_h][1]:
    #     maximum = h_idx[max_h][0]
    #     minimum = h_idx[max_h][1]
    #     max_h += 1
    #     for idx in (max_h, len(h_idx) - 1):
    #         if min(h_idx[idx][0], h_idx[idx][1]) > minimum:
    #             minimum = min(h_idx[idx][0], h_idx[idx][1])
    #     return maximum * minimum

    #print(max_w, max_h)
    # #print(w_idx, h_idx)
    # idx = 0
    # if w_idx[max_w][0] == h_idx[max_h][1]:
    #     return w_idx[max_w][0] * h_idx[max_h][1]
    # while True:
    #     if max(w_idx[max_w][0], w_idx[max_w][1]) > max(h_idx[max_h][0], h_idx[max_h][1]):
    #         if min(w_idx[max_w][0], w_idx[max_w][1]) > min(h_idx[max_h][0], h_idx[max_h][1]):
    #             max_h += 1
    #         else:
    #             return w_idx[max_w][0] * min(h_idx[max_h][0], h_idx[max_h][1])
    #     else:
    #         if min(w_idx[max_w][0], w_idx[max_w][1]) < min(h_idx[max_h][0], h_idx[max_h][1]):
    #             max_w += 1
    #         else:
    #             return h_idx[max_h][1] * min(w_idx[max_w][0], w_idx[max_w][1])
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
