nums = list(map(int, input().split(maxsplit=4)))
def min(a,b,c,d):
    if a<=b and a<=c and a<=d:
        return a
    elif b<=a and b<=c and b<=d:
        return b
    elif c<=a and c<=b and c<=d:
        return c
    else:
        return d

print(min (nums[0],nums[1],nums[2],nums[3]))