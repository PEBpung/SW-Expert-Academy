# Algorithm / Data Structure
효율적인 코드 구현을 위해 알고리즘과 자료구조를 공부하고 이를 기록한 내용입니다.

**알고리즘이란?**
- 알고리즘은 어떠한 문제를 해결하기 위한 일련의 절차를 공식화한 형태로 표현한 것. 

**자료구조란?**
-  데이터 사이의 관계를 반영한 저장구조 및 그 조작 방법.

## 1. DFS/BFS

### 1-1. DFS
- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
> 넓게(wide) 탐색하기 전에 깊게(deep) 탐색함 
> 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함
> 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 좀 더 간단함
> 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느림

### 1-2. BFS
- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법
> 깊게(deep) 탐색하기 전에 넓게(wide) 탐색함
> 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택함
> BFS 는 방문한 노드들을 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐(Queue)를 사용함
> 즉 선입선출(FIFO) 원칙으로 탐색
