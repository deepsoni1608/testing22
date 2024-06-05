"""string = input("enter: ")
string.lower()
freq = {}
if len(string)>3:
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    result = max(freq)
print(result)


string = input("Enter a string: ")
string = string.lower()
freq = {}

if len(string) > 3:
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    max_freq_char = max(freq, key=freq.get)
    max_freq = freq[max_freq_char]
    max_freq.sort(reverse = true)
#    print(max_freq_char,max_freq)

#i added here comment for checking git

##3rd program
n = int(input("Enter the value of n: "))
l = []
l2=[]
l3=[]
counter = 0
cc=0
freq=[]
for i in range(n):
    string = input("Enter the string: ")
    l.append(string)
for x in l:
    if x not in l2:   #or can use set
        l2.append(x)
        counter+=1
print(counter)
for char in set(string):
    freq.append(string.count(char))
freq.sort(key=lambda x: -[x])
for count in freq:
    print(count)
"""

