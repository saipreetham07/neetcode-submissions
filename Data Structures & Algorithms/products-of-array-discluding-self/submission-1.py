class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=nums[0]
        output=[]
        zero=0
        for i in nums[1:]:
            
            if i!=0:
                product=product*i
            else:
                zero+=1
            
        for i in nums :
            if i!=0 and zero>0:
                output.append(0)
            elif i!=0:
                output.append(int(product/i))
            elif i==0 and zero>1:
                output.append(0)
            else:
                output.append(int(product))

        return output



