class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [1 for i in range(26)]
        
        def findParent(node):
            if node == parent[node]:
                return node
            parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = findParent(node1)
            parent2 = findParent(node2)
            if parent1 == parent2:
                return
            if rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
                rank[parent1] = 0
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
        for a,sign,_,b in equations:
            if sign == "=":
                union(ord(a)-97,ord(b)-97)
        for a,sign,_,b in equations:
            if sign == "!":
                parent1 = findParent(ord(a)-97)
                parent2 = findParent(ord(b)-97)
                if parent1 == parent2:
                    return False
        return True
        