def dijkstra(self, source, dest):
            source = self.getVertex(source)
            dest = self.getVertex(dest)
            self.UnVisit()
            path = self.djSearch(source,dest)
            return path

    def djSearch(self,source,dest):
        queue = sq.DSAQueue()
        path = DSALinkedList()

        currNode = source
        currNode.setVisited(True)
        currNode.setDistance(0)
        queue.enqueue(currNode)
        path.insertFirst(currNode)

        while not queue.isEmpty():
            currNode = queue.dequeue()
            edges = currNode.getEdges()
            for edge in edges:
                vert =self.getVertex(edge.getTo())
                if vert.getVisited() is False:
                    vert.setVisited(True)
                    queue.enqueue(vert)
                    distance = currNode.getDistance() + edge.getWeight()
                    if distance < vert.getDistance():
                        vert.setDistance(distance)
                        vert.setPrevious(currNode)
                        path.insertLast((edge.getTo(),edge.getWeight()))
            if currNode == dest:
                break
        shortestPath = DSALinkedList()
        curr = dest
        while curr is not None:
            shortestPath.insertFirst((curr.getLabel(),curr.getDistance()))
            curr = curr.getPrevious()
        return shortestPath