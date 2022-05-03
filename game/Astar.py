
class AStar:
    def __init__(this, screen, stage, goalX, goalY) -> None:
        this.stage = stage
        this.screen = screen
        this.goalX = goalX
        this.goalY = goalY
        this.queue = []
        this.visited = []
        this.path = []

    def start(this, x, y):
        this.queue = [ Node(x, y, 0, this.goalX, this.goalY) ]
        this.visited = []
        this.path = this.run()
        
    def run(this):
        while len(this.queue) > 0:

            this.queue.sort(key=getF)
            node = this.queue.pop(0)
            if node.x == this.goalX and node.y == this.goalY:
                return this.createPath(node)

            this.visited.append(node)

            for neighbor in this.neighbors(node):
                if this.notIn(neighbor, this.visited):
                    if this.notIn(neighbor, this.queue):
                        this.queue.append(neighbor)
                    else:
                        # update g of neighbor that is already in queue
                        for q in this.queue:
                            if q.x == neighbor.x and q.y == neighbor.y:
                                if neighbor.g < q.g:
                                    q.g = neighbor.g
                                    q.parent = neighbor.parent
                                break

        else:
            print('Empty queue, no path')
            return []
        
    def notIn(this, node, list):
        for n in list:
            if n.x == node.x and n.y == node.y:
                return False
        return True

    def createPath(this, node):
        path = []
        path.append(node)
        while node.parent is not None:
            path.append(node.parent)
            node = node.parent
        i = 0
        print('- Path found: ' + str(len(path)-1) + ' steps to exit -')
        path.reverse()
        for p in path:
            print(str(i) + ': ('+ str(p.x)+','+str(p.y)+')')
            i+=1
        return path

    def neighbors(this, node):
        neighbors = []

        #left
        if node.x > 0 and 'r' in this.stage[node.y][node.x-1]:
            neighbors.append(Node(node.x-1, node.y, node.g+1, this.goalX, this.goalY))
        #up
        if node.y > 0 and 'd' in this.stage[node.y-1][node.x]:
            neighbors.append(Node(node.x, node.y-1, node.g+1, this.goalX, this.goalY))
        #right
        if node.x < len(this.stage[0]) and 'r' in this.stage[node.y][node.x]:
            neighbors.append(Node(node.x+1, node.y, node.g+1, this.goalX, this.goalY))
        #down
        if node.y < len(this.stage) and 'd' in this.stage[node.y][node.x]:
            neighbors.append(Node(node.x, node.y+1, node.g+1, this.goalX, this.goalY))
        for n in neighbors:
            n.parent = node
        return neighbors

# for list sorting
def getF(node):
    return node.f()

class Node:
    def __init__(this, x, y, g, goalX, goalY) -> None:
        this.x = x
        this.y = y
        this.g = g
        this.goalX = goalX
        this.goalY = goalY
        this.children = []
        this.parent = None

        # uses Manhattan distance heuristic
    def f(this):
        return this.g + abs(this.x-this.goalX)+abs(this.y-this.goalY)