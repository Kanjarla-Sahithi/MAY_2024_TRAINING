"""ip: [3,5,9,6,8,10] #Height of a building
sun at 6am will be on left side and count the number of building that sun rays will fall
sun at 6pm will  be on right side and count the number of building that sun rays will fall
"""
height=[3,5,9,6,8,10]
left=0
right=len(height)-1
lc,rc=1,1
lm,rm=height[left],height[right]
while left<len(height) and right>=0:
    if height[left]>lm:
        lc+=1
        lm=height[left]
    if height[right]>rm:
        rc+=1
        rm=height[right]
    left+=1
    right-=1
print(lc,rc)
    
    
        




    

        
        
        
        
    
    
