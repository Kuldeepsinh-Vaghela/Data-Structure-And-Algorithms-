class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # map_dic = {}
        # cntr = 0
        # while cntr <= len(nums)-1:
        #     if nums[cntr] not in map_dic:
        #         map_dic[nums[cntr]] = cntr
        #         cntr += 1
        #     else:
        #         if (cntr - map_dic[nums[cntr]])<= k:
        #             return True
        #         else:
        #             map_dic[nums[cntr]] = cntr
        #             cntr += 1 
        # return False
        map_dic = {}
        for i, num in enumerate(nums):
            if num not in map_dic:
                map_dic[num] = i
            else:
                if (i - map_dic[num])<= k:
                    return True
                else:
                    map_dic[num] = i
        return False


        