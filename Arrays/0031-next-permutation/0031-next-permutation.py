'''
    The 3-Step Logic:
    1. Find the Pivot (i): Traverse the array from right to left to find 
        the first index where nums[i] < nums[i+1]. This element at index 
        i is your pivot. If no such pivot exists (e.g., the array is 
        purely descending like [3, 2, 1]), skip to step 
    
    2.Find the Successor (j): Traverse from right to left again to find 
        the first element at index j that is strictly greater than nums
        [i]. Swap nums[i] and nums[j].
    
    3.Reverse the Suffix: Reverse the subarray from index i + 1 to the 
        end of the array to arrange it in ascending order.

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        pivot = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot==-1:
            nums.reverse()
        else:
            j = n-1
            while nums[j] <= nums[pivot]:
                j-=1
            nums[pivot], nums[j] = nums[j], nums[pivot]

            nums[pivot+1:] = nums[pivot+1:][::-1]
