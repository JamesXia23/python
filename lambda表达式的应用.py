# 实现列表排序
nums = [1, 2, 11, 33, 444, 5, 123, 675, 21, 33]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

infos = [{"id": 2, "name": "zhangsan"}, {"id": 1, "name": "lisi"}, {"id": 5, "name": "wangwu"}]
infos.sort(key=lambda info: info["id"])
print(infos)
infos.sort(key=lambda info: info["name"])
print(infos)