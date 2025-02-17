class Solution1:
    def two_sum(self, nums: list[int], target: int) -> list[int] | None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


test = Solution1()

print(test.two_sum([-3, 4, 3, 90], 0))


class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int] | None:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i


print(Solution2().two_sum([-3, 4, 3, 90], 0))
