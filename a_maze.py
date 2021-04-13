# -*- coding:utf-8 -*-

from collections import deque
from copy import deepcopy
from my_lib import cal_time


class Maze:
    @classmethod
    @cal_time
    def maze_dfs(self, maze_matrix, x1, y1, x2, y2):
        # cur_point = (x1, y1)
        # stack = []
        # stack.append(cur_point)
        # def touch_around(maze_matrix, stack, p):
        #     if (maze_matrix[p[0] + 1][p[1]] != 1) and ([p[0] + 1, p[1]] not in stack) and (maze_matrix[p[0] + 1][p[1]] != 2):
        #         p = (p[0] + 1, p[1])
        #         stack.append(p)
        #         maze_matrix[p[0]][p[1]] = 2
        #     elif (maze_matrix[p[0]][p[1] + 1] != 1) and ([p[0], p[1] + 1] not in stack) and (maze_matrix[p[0]][p[1] + 1] != 2):
        #         p = (p[0], p[1] + 1)
        #         stack.append(p)
        #         maze_matrix[p[0]][p[1]] = 2
        #     elif (maze_matrix[p[0] - 1][p[1]] != 1) and ([p[0] - 1, p[1]] not in stack) and (maze_matrix[p[0] - 1][p[1]] != 2):
        #         p = (p[0] - 1, p[1])
        #         stack.append(p)
        #         maze_matrix[p[0]][p[1]] = 2
        #     elif (maze_matrix[p[0]][p[1] - 1] != 1) and ([p[0], p[1] - 1] not in stack) and (maze_matrix[p[0]][p[1] - 1] != 2):
        #         p = (p[0], p[1] - 1)
        #         stack.append(p)
        #         maze_matrix[p[0]][p[1]] = 2
        #     else:
        #         p = stack[-1]
        #         stack.pop()
        #     return stack, p
        #
        # while len(stack) > 0:
        #     stack, cur_point = touch_around(maze_matrix, stack, cur_point)
        #     if cur_point == (x2, y2):
        #         return stack
        # return False

        """
        Optimization version
        """
        dirs = [
            lambda x, y: (x + 1, y),
            lambda x, y: (x, y + 1),
            lambda x, y: (x - 1, y),
            lambda x, y: (x, y - 1)
        ]
        cur_point = (x1, y1)
        stack = []
        stack.append(cur_point)

        while len(stack) > 0:
            cur_node = stack[-1]
            for dir in dirs:
                next_node = dir(cur_node[0], cur_node[1])
                if maze_matrix[next_node[0]][next_node[1]] == 0:
                    stack.append(next_node)
                    maze_matrix[next_node[0]][next_node[1]] = 2
                    break
            else:
                if maze_matrix[next_node[0]][next_node[1]] == 0:
                    maze_matrix[next_node[0]][next_node[1]] = 2
                stack.pop()

            if next_node == (x2, y2):
                return stack
        return []

    @classmethod
    @cal_time
    def maze_bfs(self, maze_matrix, x1, y1, x2, y2):
        def print_path(path):
            cur_node = path[-1]
            real_path = []
            while cur_node[2] != -1:
                real_path.append(cur_node[:2])
                cur_node = path[cur_node[2]]
            real_path.append(cur_node[:2])
            return [x for x in reversed(real_path)]

        dirs = [
            lambda x, y: (x + 1, y),
            lambda x, y: (x, y + 1),
            lambda x, y: (x - 1, y),
            lambda x, y: (x, y - 1)
        ]
        cur_node = (x1, y1, -1)
        queue = deque()
        queue.append(cur_node)
        path = []
        while len(queue) > 0:
            cur_node = queue.pop()
            path.append(cur_node)
            if cur_node[0] == x2 and cur_node[1] == y2:
                return print_path(path)
            for dir in dirs:
                next_node = dir(cur_node[0], cur_node[1])
                if maze_matrix[next_node[0]][next_node[1]] == 0:
                    queue.append((next_node[0], next_node[1], len(path) - 1))
                    maze_matrix[next_node[0]][next_node[1]] = 2
        return []


def show(maze, stack):
    for ele in stack:
        maze[ele[0]][ele[1]] = 5
    for ele in maze:
        print(ele)


if __name__ == '__main__':
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    maze1 = deepcopy(maze)
    stack = Maze.maze_dfs(maze1, 1, 1, 8, 8)
    show(maze1, stack)
    maze2 = deepcopy(maze)
    stack = Maze.maze_bfs(maze2, 1, 1, 8, 8)
    show(maze2, stack)
