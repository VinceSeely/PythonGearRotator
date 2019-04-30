import copy


class BreadthFirstSearch:

    def Run(self, gear_manager):
        return self.breadth_first_search(gear_manager)

    def breadth_first_search(self, gear_manager):
        gears = gear_manager.get_copy_of_gears()
        closed = []
        nodes_to_visit = [[[], gears]]

        while len(nodes_to_visit) != 0:
            currentNode = nodes_to_visit.pop(0)
            gearPositions = []
            for gear in currentNode[1]:
                gearPositions.append(gear.position)

            if closed.__contains__(gearPositions):
                continue

            closed.append(gearPositions)

            if closed.__contains__(gear_manager.get_goal()):
                return currentNode[0]

            for gearToBeRotated in range(len(gears)):
                gearCopy = gear_manager.rotate_and_copy(currentNode[1], gearToBeRotated)
                nodeCopy = copy.deepcopy(currentNode[0])
                nodeCopy.append(gearToBeRotated)
                nodes_to_visit.append([nodeCopy, gearCopy])

        return None
