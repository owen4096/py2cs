#研究自 https://openhome.cc/zh-tw/algorithm/basics/maze/ 此網站的open source

class Mouse:
    @staticmethod
    def go(maze, start, end, take):
        Mouse.visit(maze, start, end, [], take)
    
    @staticmethod
    def visit(maze, pt, end, route, take):
        if Mouse.isVisitable(maze, pt, route):
            route.append(pt)
            if Mouse.isEnd(route, end):
                take(maze, route)
            else:
                Mouse.visit(maze, (pt[0], pt[1] + 1), end, route, take)#下
                Mouse.visit(maze, (pt[0] + 1, pt[1]), end, route, take)#右
                Mouse.visit(maze, (pt[0], pt[1] - 1), end, route, take)#上
                Mouse.visit(maze, (pt[0] - 1, pt[1]), end, route, take)#左
            route.pop()
            #簡單的dfs邏輯 一路找 找不到能走的路就pop掉
    
    @staticmethod
    def isVisitable(maze, pt, route):
        return maze[pt[0]][pt[1]] == 0 and pt not in route
        
    @staticmethod
    def isEnd(route, end):
        return end in route

def console(maze, route):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) in route:
                print(".", end="")
            else:
                {
                    0 : lambda: print(" ", end=""),
                    2 : lambda: print("I",end="")
                }[maze[i][j]]()
        print()
   
Mouse.go([
           [2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 2, 0, 2, 2, 0, 2],
           [2, 0, 2, 0, 0, 2, 0, 0, 2],
           [2, 0, 2, 0, 2, 0, 2, 0, 2],
           [2, 0, 0, 0, 0, 0, 2, 0, 2],
           [2, 2, 0, 2, 2, 0, 2, 2, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2]
         ], (1, 1), (7, 7), console)

