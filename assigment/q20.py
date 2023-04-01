"""Write a Python function that takes a list of words and returns the length
of the longest one."""

def count_word_length(my_list):
    counter = 0
    for item in my_list:
        if len(item) >= counter:
            counter = len(item)
        return counter
    
    temp_list = ["hello","word","a","long"]
    print("Longest word count is %d" %count_word_length(temp_list))
