#!/usr/bin/env python3


def minTimeToVisitAllPoints(points):
    time = 0

    for point_i in range(len(points)):
        if points[point_i] == points[len(points) - 1]:
            return time
        else:
            compare_point = points[point_i + 1]
            shortest_dist = max(abs(compare_point[1] - points[point_i][1]),
                                abs(compare_point[0] - points[point_i][0]))
            time += shortest_dist