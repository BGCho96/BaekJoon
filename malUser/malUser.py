import re

def is_match(user, banned):
    pattern = "^" + banned.replace("*", ".") + "$"
    return bool(re.match(pattern, user))

def backTracking(depth, banned_id, user_match, visited, same_checker):
    if depth == len(banned_id):  # 모든 banned_id에 대한 조합을 찾았다면
        checker = frozenset(visited)
        if checker not in same_checker:
            same_checker.add(checker)
            return 1
        return 0

    count = 0
    for user in user_match[depth]:
        if user not in visited:  # 이미 방문한 user_id는 제외
            visited.add(user)
            count += backTracking(depth + 1, banned_id, user_match, visited, same_checker)
            visited.remove(user)  # 백트래킹: 상태 복구

    return count

def solution(user_id, banned_id):
    user_match = []  # 각 banned_id에 대해 가능한 user_id 리스트 저장
    for ban in banned_id:
        matches = {user for user in user_id if is_match(user, ban)}
        user_match.append(matches)

    same_checker = set()
    return backTracking(0, banned_id, user_match, set(), same_checker)
