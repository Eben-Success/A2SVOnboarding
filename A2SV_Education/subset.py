class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        def is_valid_state(state):
            return len(state) <= n

        def get_candidates(state):
            if len(state) == 0:
                res = set([num for num in nums])
            else:
                res = set([num for num in nums if num > max(state)])
            return res

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

                for candidate in get_candidates(state):
                    state.add(candidate)
                    search(state, solutions)
                    state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        return solutions
