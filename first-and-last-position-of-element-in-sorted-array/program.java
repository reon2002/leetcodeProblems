class Solution {
    public int[] searchRange(int[] nums, int target) 
    {
        int i=findFirst(nums,target);
        int j=findLast(nums,target);
        int result[]={i,j};
        return result;
    }
    public int findFirst(int nums[], int target)
    {
        int k=-1;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target)
            {
                k=i;
                break;
            }
        }
        return k;
    }
    public int findLast(int nums[], int target)
    {
        int k=-1;
        for(int i=nums.length-1;i>=0;i--)
        {
            if(nums[i]==target)
            {
                k=i;
                break;
            }
        }
        return k;
    }
}