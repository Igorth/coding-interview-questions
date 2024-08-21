#You are provided with a large string and a dictionary of the words.
# You have to find if the input string can be segmented into words using the dictionary or not.

def can_segment_str(my_string, my_dict):
    for i in range(1, len(my_string) + 1):
        first_str = my_string[0:i]
        print("first", first_str)
        if first_str in my_dict:
            second_str = my_string[i:]
            print("second", second_str)
            if not second_str or second_str in my_dict or can_segment_str(second_str, my_dict):
                return True
    return False



s = "lackcamping"
dictionary = ["data", "camp", "cam", "lack"]
print(can_segment_str(s, dictionary))