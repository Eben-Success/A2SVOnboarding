class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        """
        1. Use stack
        2. Append [char, freq] on to the stack.
        3. If freq == k:
        4. Pop from stack
        5. Else: Append to stack.
        6. Iterate over elements in stack, add the occurence of elements onto a string variable and return.
        """

        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)

                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append((char, 1))

        res = []
        for char, num in stack:
            res.append(char * num)

        return "".join(res)
