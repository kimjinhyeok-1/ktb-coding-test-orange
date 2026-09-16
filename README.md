# KTB Coding Test Study

카카오테크 부트캠프 코딩테스트 오렌지 스터디입니다.

## 진행 방식

- 총 4명
- 2명씩 한 조로 구성
- 각 조는 매주 4문제를 풀이
- 같은 문제를 2명이 각각 풀이
- 풀이 후 접근 방식과 시간복잡도를 비교
- 매주 알고리즘 주제를 정해 학습
- PR을 통해 풀이 과정과 코드 리뷰 진행

## 주차별 주제

| 주차 | 알고리즘 |
|---|---|
| 1주차 | BFS / DFS |
| 2주차 | DP |
| 3주차 | Heap / Greedy |
| 4주차 | Binary Search  |
| 5주차 | Two Pointer |

## 풀이 규칙

1. 문제를 먼저 혼자 풀이합니다.
2. 제한 시간 내 해결하지 못하면 힌트 또는 풀이를 참고합니다.
3. 풀이 후 시간복잡도를 작성합니다.
4. PR에 접근 과정과 어려웠던 점을 기록합니다.
5. 같은 문제를 푼 팀원의 풀이와 비교합니다.

## 브랜치 규칙

```text
이름/weekXX-문제명
```

## Git 사용 방법

문제 풀이 시 아래 순서대로 진행합니다.

### 1. 최신 main 브랜치 받기

작업 시작 전에 항상 `main` 브랜치를 최신 상태로 맞춥니다.

```bash
git checkout main
git pull origin main
```
### 2. 사용자별(혹은 주차별 - 이건 자유) 브랜치 생성

```bash
git checkout -b jay/week01
```
### 3. 문제 풀이 후 커밋
```bash
git add .
git commit -m "solve: week01 타겟 넘버"
```
### 4. 깃허브에서 PR 생성
### 5. PR에 간단하게 문제에 대한 리뷰 남기기 

## 정리
주차 시작 전에
```bash
git checkout main
git pull origin main

git checkout jinhyeok
git merge main
```

만약 주차별로 관리하고 있다면 -b 붙여서 새로 만들고
아니라면 그냥 브랜치만 이동해서 진행