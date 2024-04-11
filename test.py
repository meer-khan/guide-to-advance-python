# l1 =  [value for value in range(0,5000000)]
# import time

# startTime = time.time()
# l2 = l1[:]
# endTime = time.time()
# print((endTime - startTime))

# # l2[0] =555
# # print(l1)
# # print(l2)

# startTime2 = time.time()
# l3 = l1.copy()
# endTime2 = time.time()
# print((endTime2-startTime2))



def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sums = []
        
        for index, val in enumerate(nums): 
            
            for i in range(index+1,len(nums)):
                sum = 0
                sum = val + nums[i]
                if sum == target:
                    sums.extend([index,i])
                    return sums
                
# print(twoSum(nums = [3,2,3], target = 6))

# print( type(3.96) is float)
# import math 

# x = math.modf(len([1,2,3,4,5])/2)
# print(x)

# y = len([1,2,3,4])/2
# z = int(len([1,2,3,4])/2)
# print('y is: ', y)
# yz = y-z
# if yz != 0.0:
#      print(yz)
#      median = math.ceil(y)
#      print("median", median)
# else:
#     #  print("OK", yz)
#     median = z
#     print("median ok ", median, median+1)



import math
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = nums1+nums2
        length = len(num3)/2
        intLength = int(len(num3)/2)
        difference = length - intLength
        if difference != 0.0:
            median = num3[math.ceil(length)]/1
        else: 
            median = (num3[intLength-1] +  num3[intLength])/2
        
        return median

# print(float(findMedianSortedArrays([1,2],[3,4])))





def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # lastIndex = len(nums)-1
        # if lastIndex == 1:
        #      return False
        # jumpIndex = 1
        # jumpedIndex = 0
        # while True: 
        #     if jumpedIndex == lastIndex:
        #         return True
        #     elif jumpedIndex > lastIndex:
        #         return False
        #     jumpVal = nums[jumpIndex]
        #     if jumpVal == 0:
        #          return False
        #     jumpIndex = jumpVal
        #     jumpedIndex += jumpVal

        lastIndex = len(nums)-1
        if lastIndex == 0:
             return True
        if nums == []:
            return False
        jumpIndex = 1
        jumpedIndex = 1
        while True: 
            
            jumpVal = nums[jumpIndex]
            jumpIndex += jumpVal
            if jumpVal == 0:
                return False
            if jumpVal == 0 and jumpedIndex != lastIndex:
                 return False
            if jumpedIndex == lastIndex:
                return True
            elif jumpedIndex > lastIndex:
                return False
            jumpedIndex += jumpVal
# print(canJump([2,3,1,1,4]))

# print(canJump([1,2]))

print(canJump([0,1]))

# print(canJump([3,2,1,0,4]))




