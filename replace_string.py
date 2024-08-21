def replace_str(text, character):
    result = ''
    for i in text:
        if i == " ":
            i = character
        result += i
    return result


message = replace_str("l vey u", "o")
print(message)

