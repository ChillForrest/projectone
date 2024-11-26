#子序列检查问题-----变位词
#1
def textfinder (s1,s2):
    alist=list(s2)
    pose1=0
    stillok=True
    while pose1<len(s1) and stillok:
        pose2=0
        found=0
        while pose2<len(alist) and not found:
            if s1[pose1]==alist[pose2]:
                found = True
            else:
                pose2=pose2+1
        if found:
            alist[pose2]=None
        else:
            stillok=False
        pose1=pose1+1
    return stillok

#2
def textfinder2(s1,s2):
    imlist1=list(s1)
    imlist2=list(s2)

    imlist1.sort()
    imlist2.sort()

    pose = 0
    finderflag=True
    while pose<len(s1) and finderflag:
        if imlist1[pose]==imlist2[pose]:
            pose=pose+1
        else:
            finderflag=False
    return finderflag

# #3 ord

# def textfinder3(s1,s2):
    
# s1=input()
# s2=input()
# print(textfinder2(s1,s2))