'''
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

actually, this kind of question is backtracking.
'''

def permute(nums):
    results = []
    tracks = []

    def do_permute():
        if len(tracks) == len(nums):
            results.append(tuple(tracks))
            return

        for num in nums:
            if tracks.count(num) != 0:
                continue
            tracks.append(num)
            do_permute()
            tracks.pop()

    do_permute()
    return results

print(permute(list(range(4))))