# program to fill in a letter template with name an date
letter = "Dear <|name|>, you are selected! <|date|>"
letter_replace = (letter.replace("<|name|>","Bhoomika").replace("<|date|>","feb 2"))
print(letter_replace)
