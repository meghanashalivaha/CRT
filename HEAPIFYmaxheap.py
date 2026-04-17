def heapifyDown(nums,value):
    largest=index
    leftchild=2*index+1
    rightchild=2*index+2
    if(leftchild<len(nums) and nums[leftchild]> nums[largest]):
        largest=leftchild 
    if(rightchild<len(nums) and nums[rightchild]> nums[largest]):
       largest=rightchild
    if(largest!=index):
        nums[index],nums[largest]=nums[largest],nums[index]
        heapifyDown(nums,largest) 
def heapifyUp(nums,index):
    if(index>0):
        parent=(index-1)//2
        if(nums[index]>nums[parent]):
            nums[index],nums[parent]=nums[parent],nums[index]
            heapifyUp(nums,parent)
nums=[]
l=int(input())
for i in range(l):
    num=int(input())
    nums.append(na)
n=int(input())
for _ in range(0,n):
    index=int(input())
    value=int(input())

    if(nums[index]>value):
        nums[index]=value
        heapifyDown(nums,value)
    if(nums[index]<value):
        nums[index]=value
        heapifyUp(nums,index)
    print(nums)
