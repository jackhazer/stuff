class Solution(object):
    def codinginterview(self, arr):
        """
        :type arr: list
        :rtype: int
        """
        n=len(arr)
        if n<=2:
            return None
        arr.sort()

        biggest=arr.pop(-1)
        if biggest<0:
            return arr[-1]*arr[-2]*arr[-3]

        return max(arr[0]*arr[1]*biggest, arr[-1]*arr[-2]*biggest)

def main():
    solution = Solution()
    result = solution.codinginterview([0, -2, -3, -4, -5])


    return result

print(main())
