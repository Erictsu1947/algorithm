
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    length = len(nums)

    mid = length // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(l, r):
    merged_list = []
    j, k = 0, 0
    while j < len(l) and k < len(r):
        if l[j] < r[k]:
            merged_list.append(l[j])
            j += 1
        else:
            merged_list.append(r[k])
            k += 1
    if len(l) == j:
        for i in r[k:]:
            merged_list.append(i)
    else:
        for i in l[j:]:
            merged_list.append(i)
    return merged_list


nums = [3, 2, 8, 1, 7, 5, 3, 9, 6, 4]
result = merge_sort(nums)
print(result)
