CLASS_TYPE_NAME = r'(class|interface)'
ACCESS_MODIFIER = r'public|private|protected'
STATIC = r'(\s+static)?'
WARD = r'(\w+)'
ZERO_BLANK = r'\s*'
ONE_BLANK = r'\s+'
PARENTHESES = '\((.*)\)'
TYPE_NAME = '(\w+|\w+<\w+>)'

# (\s*=\s*(.+))?
VARIABLE_VALUE = '(' + ZERO_BLANK + '=' + ZERO_BLANK + '(.+))?'
# print(VARIABLE_VALUE)

# public\s+(class|interface)\s+(\w+)
CLASS_NAME_LINE = r'public' + ONE_BLANK + CLASS_TYPE_NAME + ONE_BLANK + WARD
# print(CLASS_NAME_LINE)

# \s*public|private|protected
ACCESS_MODIFIER_LINE = ZERO_BLANK + ACCESS_MODIFIER
# print(ACCESS_MODIFIER_LINE)

# \s*(public|private|protected)(\s+static)?\s+(\w+|\w+<\w+>)\s+(\w+)(\s*=\s*(.+))?;
VARIABLE_LINE = ZERO_BLANK + '(' + ACCESS_MODIFIER + ')' + STATIC + ONE_BLANK + TYPE_NAME + ONE_BLANK + WARD + VARIABLE_VALUE + ';'
# print(VARIABLE_LINE)

# \s*(public|private|protected)(\s+static)?(\s+(\w+|\w+<\w+>))\s+(\w+)\s*\((.*)\)
METHOD_LINE = ZERO_BLANK + '(' + ACCESS_MODIFIER + ')' + STATIC + '(' + ONE_BLANK + TYPE_NAME + ')' + ONE_BLANK + WARD + ZERO_BLANK + PARENTHESES
# print(METHOD_LINE)
