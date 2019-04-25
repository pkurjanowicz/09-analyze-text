# Remember to reach out for help after your own due diligence

def remove_special_chars(text):
    special_chars = "!,'; 0)"
    no_special_chars = ""
    if text.isalpha():
        return text
    else:
        for each_char in text:
            if each_char not in special_chars:
                no_special_chars = no_special_chars + each_char
        return no_special_chars
            

def analyze_text(text):
    text = remove_special_chars(text)
    num_of_char = len(text)
    letter_e = 'e'
    letter_E = 'E'
    total_es = text.count(letter_E) + text.count(letter_e)
    text.isalpha()
    num = (total_es/num_of_char)/1.0
    percentage = "{:.2%}".format(num)
    return ("The text contains {} alphabetic characters, of which {} ({}) are 'e'." .format(num_of_char, total_es, percentage))
