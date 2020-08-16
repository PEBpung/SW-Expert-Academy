'''
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''


import heapq
def solution(scoville, K):
    answer = 0
    # 받은 리스트를 힙으로 만든다.
    heapq.heapify(scoville)
    mix = 0
    # Heap의 크기만큼 순회한다.
    while len(scoville) > 1 and scoville[0] < K:
        # 최소값을 뽑아낸다.
        min = heapq.heappop(scoville)
        # 만약 최솟값이 K보다 작다면?
        if(min < K):
            # 최솟값과 두번째 최솟값*2를 더해준다.
            mix = min + heapq.heappop(scoville)*2
            # 더한 값을 다시 리스트에 넣어준다.
            heapq.heappush(scoville, mix)
            # answer+1을 해준다.
            answer += 1
        # 최솟값이 K보다 작지 않다면 ?
        else:
            # 루프를 탈출한다.
            break
    # 스코빌 지수를 K 이상으로 만들 수 없으면 -1을 return한다.
    if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer
