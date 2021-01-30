'''
implement Pascal's triangle by using generator
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1


https://en.wikipedia.org/wiki/Pascal%27s_triangle
'''

def triangles(n, line_nums = []):
    for _ in range(n):
        l = len(line_nums)
        line_nums = [1 if i == 0 or i == l else line_nums[i - 1] + line_nums[i] for i in range(l + 1)]
        yield line_nums

if __name__ == '__main__':
    n = 10
    for nums in triangles(n):
        print(' '.join(map(str, nums)).center(n * 4), end='\n\n')
