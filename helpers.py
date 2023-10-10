import re


def remove_comments(source_code, file_ext):
    if file_ext == ('js' or 'cpp' or 'java' or 'c' or 'cs'):
        # Remove single-line comments
        code = re.sub(r'//.*', '', source_code)
        # Remove multi-line comments
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        return code

    elif file_ext == "py":
        # Remove multiline comments
        code = re.sub(r'(?s)""".*?"""', '', source_code)
        code = re.sub(r"(?s)'''.*?'''", '', source_code)
        # Remove single-line comments
        lines = code.split('\n')
        code = ''
        for line in lines:
            if '#' in line:
                code += line[:line.index('#')] + '\n'
            else:
                code += line + '\n'
        return code

    elif file_ext == "pas":
        lines = source_code.split('\n')
        code = ''
        in_comment = False
        for line in lines:
            if in_comment:
                if '*)' in line:
                    in_comment = False
                    code += line[line.index('*)') + 2:] + '\n'
            else:
                if '(*' in line:
                    in_comment = True
                    code += line[:line.index('(*')] + '\n'
                else:
                    code += line + '\n'
        return code
