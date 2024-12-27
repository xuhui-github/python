import fileinput, re

field_pat = re.compile(r"\[(.+?)\]")

scope = {}  # collect variables in this

# this is used in re.sub


def replacement(match):
    code = match.group(1)
    try:
        print(code)
        return str(eval(code, scope))

    except SyntaxError:
        return ""


lines = []
for line in fileinput.input():
    lines.append(line)

text = "".join(lines)

print(field_pat.sub(replacement, text))
