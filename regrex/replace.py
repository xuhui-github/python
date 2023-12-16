import re
emphasis_pattern=re.compile(r'''
                            \*
                            (
                            [^\*]+
                            )
                            \*
                            ''',re.VERBOSE)
print(re.sub(emphasis_pattern,r'<em>\1</em>','Hello, *world*!'))

emphasis_pattern=re.compile(r'\*\*(.+?)\*\*')
print(re.sub(emphasis_pattern,r'<em>\1</em>','**this** is **it**!'))
