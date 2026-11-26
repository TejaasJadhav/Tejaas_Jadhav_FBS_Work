li = []

#    for i in range(1,4):
#        for j in range(1,4):
#            li.append([i,j])
#
#    print(li)
newlist=[[i,j] for i in range(1,4) for j in range(1,4)]
print(newlist)

#    s1 = "i am good in coding"
#    vowels = "aeiouAEIOU"
#    vowel_list=[]
#    for char in s1:
#        if char in vowels:
#            vowel_list.append(char)
#    print(vowel_list)



s1 = "i am good in coding"
vowel_list = [char for char in s1 if char.lower() in "aeiou"]
print(vowel_list)
