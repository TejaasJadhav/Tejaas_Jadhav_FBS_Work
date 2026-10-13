#Write a program to input any alphabet and check whether it is vowel or consonant.

a = input("Enter any Alphabet: ")

if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
        print(f"{a} is Vowel")
else:
    print(f"{a} is Consonant")