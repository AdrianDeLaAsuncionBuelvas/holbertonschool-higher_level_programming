 #!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of\
 these characters: ., ? and :
"""



def text_indentation(text):
    """
    text_indentation -- print a text with 2 new lines after each of\
    these characters
    text -- recibe the Text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    """
    removes space only when it finds a matching character
    """
    tok = 0
    for i in text:
        """
        if it found a character it removes the space continues
        """
        if tok == 1 and i is ' ':
            print('', end='')
            tok = 0
            continue
        if i is '.' or i is '?' or i is ':':
            print("{}\n".format(i))
            tok = 1
        else:
            print(i, end='')
            tok = 0
