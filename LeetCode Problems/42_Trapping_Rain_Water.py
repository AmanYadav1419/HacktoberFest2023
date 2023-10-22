class Solution:
    def trap(self, arr: List[int]) -> int:
        left,right=[],[]
        mx,mx1,n=0,0,len(arr)
        for i in arr:
            mx=max(mx,i)
            left.append(mx)
        for i in range(n-1,-1,-1):
            mx1=max(mx1,arr[i])
            right.append(mx1)
        right=right[::-1]
        list1 = [min(i,j) for i, j in zip(left,right)]
        return sum(list1[i]-arr[i] for i in range(n) if list1[i]-arr[i]>0)