class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def dfs(city):
            visited.add(city)
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] and neighbor not in visited:
                    dfs(neighbor)

        numOfProvinces = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                numOfProvinces += 1
                dfs(city)

        return numOfProvinces
