"""
Time Complexity:  O(n^2)
Space Complexity: O(n)

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]"""


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        """Using example of "[[0,0],[1,0],[2,0]])"  """

        result = 0
        for point_a in points:
            distances = {}
            for point_b in points:
                distance = (point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2   #calculate the distance between point a and each point in points_list. 
                distances[distance] = distances.get(distance, 0) + 1                         #creating a dictionary of distance(key) and the frequence of occurence of
                                                                                             #this key, using hash table method
            
            print(distances)
            result += sum(item * (item - 1) for item in distances.values())                  #using n*(n-1) combination
            print(result)    
        return result

a = Solution()
print(a.numberOfBoomerangs([[0,0],[1,0],[1,0],[0,1],[-1,0]]))
