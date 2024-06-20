height=[2,4,6,2,5,7,5,2]
left=0
right=len(height)-1
lm,rm=height[left],height[right]
w=0
while left<right:
    if lm<rm:
        left+=1
        if lm<height[left]:
            lm=height[left]
        w=w+abs(lm-height[left])
    else:
        right-=1
        if rm<height[right]:
            rm=height[right]
        w=w+abs(rm-height[right])
                            

