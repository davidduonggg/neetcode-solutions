class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars traveling to the same destination
        # given two arrays of integers
        # position[i]
        # speed[i]
        # destination is at position target miles

        # a car cannot pass another car. it can only catch up

        # a car fleet is a non-empty set of cars driving same position and speed

        # if a car catches up to a car fleet
        # moment it reaches destination, then the car is considered to be part of it

        cars = list(zip(position, speed))
        cars.sort()
        fleets = 0

        stk = []
        for i in range(len(cars) - 1, -1, -1):
            # traverse backwards
            time = (target - cars[i][0]) / cars[i][1]
            if not stk or time > stk[-1]:
                stk.append(time)

        return len(stk)