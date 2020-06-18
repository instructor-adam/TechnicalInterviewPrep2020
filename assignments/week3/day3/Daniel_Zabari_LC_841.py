class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_stack = []
        visited = [0] * len(rooms)
        room_stack.append(0)
        while room_stack != []:
            room = room_stack.pop()
            visited[room] = 1
            for key in rooms[room]:
                if visited[key] == 0:
                    room_stack.append(key)
        for value in visited:
            if value == 0:
                return False
        return True
