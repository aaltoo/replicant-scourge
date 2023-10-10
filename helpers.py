import re


def remove_comments(string, lang_extension):
    if lang_extension == ('js' or 'cpp' or 'java' or 'c'):
        pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"  # C-like comment pattern
        regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

        def _replacer(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)
        return regex.sub(_replacer, string)

