class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        A=nums
        for i in range(n):
            while 0 < A[i] <= n and A[A[i] - 1] != A[i]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1