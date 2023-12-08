class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        src = rooms[0]
        queue = deque([(src)])
        visited = set([0])
        

        while queue:
            room = queue.popleft()

            for key in room:
                if key not in visited:
                    queue.append(rooms[key])
                    visited.add(key)

        return len(visited) == len(rooms)
