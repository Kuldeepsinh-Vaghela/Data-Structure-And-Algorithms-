class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_dic = {}
        if len(nums1) > len(nums2):
            for num in nums1:
                map_dic[num] = map_dic.get(num,0) + 1
            common_elements = []
            for num in nums2:
                if num in map_dic and map_dic[num] > 0:
                    common_elements.append(num)
                    map_dic[num] -= 1
            return common_elements
        else:
            for num in nums2:
                map_dic[num] = map_dic.get(num,0) + 1
            common_elements = []
            for num in nums1:
                if num in map_dic and map_dic[num] > 0:
                    common_elements.append(num)
                    map_dic[num] -= 1
            return common_elements


        