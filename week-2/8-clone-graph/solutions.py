"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Use BFS
        if node is None:
            return None

        result_node = Node(node.val)

        queue = deque([node])
        result_queue = deque([result_node])

        clones_map = {}
        clones_map[result_node.val] = result_node

        visited_map = {}

        while queue and result_queue:
            cur_result_node = result_queue.popleft()
            cur_node = queue.popleft()

            if cur_node.val in visited_map:
                continue

            visited_map[cur_node.val] = True

            result_neighbors = []
            for neighbor in cur_node.neighbors:
                cur_result_neighbor = Node(neighbor.val)

                if neighbor.val in clones_map:
                    cur_result_neighbor = clones_map[neighbor.val]
                else:
                    clones_map[neighbor.val] = cur_result_neighbor

                result_neighbors.append(cur_result_neighbor)

                # Append queue
                queue.append(neighbor)
                result_queue.append(cur_result_neighbor)

            cur_result_node.neighbors = result_neighbors

        return result_node
