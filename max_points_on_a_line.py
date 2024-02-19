class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # get each pair, find number of points on line
        number_of_points = len(points)
        if number_of_points <= 2:
            return number_of_points
        
        visited_points = []
        line_values = []
        for i in points:
            visited_points.append(i)
            for j in points:
                line_value = 0
                if j not in visited_points:
                    if i[0] == j[0]:
                        line_value += len([k for k in points if k[0] == i[0]])
                    else:
                        slope_numerator = i[1]-j[1]
                        slope_denominator = i[0] - j[0]
                        line_value += len([k for k in points if k[1] - i[1] == ((k[0] - i[0])/slope_denominator) * slope_numerator])
                    line_values.append(line_value)
                
        return max(line_values)
