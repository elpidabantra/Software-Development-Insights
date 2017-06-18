import sys
import tokenize
import io

def remove_all_comments(text_string):
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    io_obj = io.StringIO(text_string)
    out = ""
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out


f = open("author_contribution_without_comments.txt", 'w')
sys.stdout = f
document_text = open('author_contribution.txt', 'r')
text_string = str(document_text.read().lower())
print(remove_all_comments(text_string))

f.close()





