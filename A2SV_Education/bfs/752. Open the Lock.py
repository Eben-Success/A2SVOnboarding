class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        src = "0000"

        if src in deadends:
            return -1

        n = [-1, 1]
        queue = deque([(src, 0)])

        while queue:
            node, turns = queue.popleft()

            if node == target:
                return turns
            
            if node in visited:
                continue
            visited.add(node)
            
            for i in range(4):
                for j in n:
                    var = (int(node[i]) + j) % 10
                    num = node[:i] + str(var) + node[i+1:]

                    if num not in visited:
                        queue.append((num, turns + 1))

        return -1
