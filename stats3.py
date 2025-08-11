def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lowered = text.lower()
    frequency = {}
    for char in lowered:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sort_on(items):
    return items["num"]

def get_sorted_dict(freq):
    final_list = []
    for each in freq:
        if each.isalpha():
            temp_dict = {}
            temp_dict["char"] = each
            temp_dict["num"] = freq[each]
            final_list.append(temp_dict)
    final_list.sort(reverse=True, key=sort_on)
    actual_final_list=[]
    for each in final_list:
        actual_final_list.append(f"{each["char"]}: {each["num"]}")
    return actual_final_list
    
    