"""폰켓몬 — 정답 풀이 없이 시작하는 연습 틀.
출처: https://school.programmers.co.kr/learn/courses/30/lessons/1845
함수 매개변수와 공식 입출력 예 확인: 2026-09-30.
"""


def solution(nums):
    # TODO: 직접 작성한 풀이로 아래 예외를 교체하세요.
    # setlist = set(nums)
    # print(setlist) # 세트 생성(중복제거)
    # 딕셔너리 생성

    # dictlist = {}
    # for i in nums:
    #     if dictlist == None:
    #         dictlist = {i:0}

    #     else:
    #         for k, v in dictlist:
    #             print("들어옴?")
    #             if i == k:
    #                 v += 1
    #             else:
    #                 dictlist.update(i = 0)
    # print(dictlist)

    answer = 0
    maxcount = len(nums) // 2
    my_dict = {}

    # 리스트 값들 딕셔너리로 변환
    for num in nums:
        if num in my_dict:
            my_dict[num] += 1
        else:
            #my_dict.update(num = 0) 왜 update는 못쓰지??
            my_dict[num] = 1
    # print(my_dict)
    
    # 딕셔너리 개수 세는 것도 len 활용
    while(answer == 0):
        if maxcount == len(my_dict):
            answer = maxcount
        elif maxcount > len(my_dict):
            maxcount -= 1 
        elif maxcount < len(my_dict):
            answer = maxcount
    
    return answer
    
    # raise NotImplementedError("아직 풀이를 작성하지 않았습니다.")


if __name__ == "__main__":
    # 공식 입출력 예: (함수에 전달할 인자 튜플, 기대 결과)
    test_cases = [(([3, 1, 2, 3],), 2), (([3, 3, 3, 2, 2, 4],), 3), (([3, 3, 3, 2, 2, 2],), 2)]
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
