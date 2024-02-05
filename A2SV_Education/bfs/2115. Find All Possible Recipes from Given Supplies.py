from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        outdegree, indegree = self.buildGraph(recipes, ingredients, supplies)

        queue = deque()
        res = []

        for recipe in recipes:
            if indegree[recipe] == 0:
                queue.append(recipe)

        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in outdegree[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return res

    def buildGraph(self, recipes, ingredients, supplies):

        outdegree = defaultdict(list)
        indegree = defaultdict(int)
        supplies = set(supplies)
        n = len(recipes)

        for i in range(n):
            indegree[recipes[i]] = 0

        for i in range(n):
            for ing in ingredients[i]:
                if ing not in supplies:
                    outdegree[ing].append(recipes[i])
                if ing not in supplies:
                    indegree[recipes[i]] += 1

        return outdegree, indegree


    
       
        
