class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def is_valid_state(state):
            return len(state) == len(nums)
    
        def get_candidates(state):
            if len(state) == 0:
                res = set([num for num in nums])
            else:
                res = set(nums).difference(set(state))
            return res

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        solutions = []
        state = []
        search(state, solutions)
        return solutions
        
