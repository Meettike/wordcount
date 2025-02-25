def count_word(s):
    string = s.split()
    count = 0
    for i in range(len(string)):
        count+=1
    print('Number of words in the string is: ',count)
count_word('Hello world meet')