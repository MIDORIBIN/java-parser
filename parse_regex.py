CLASS_TYPE_NAME = r'(class|interface)'
ACCESS_MODIFIER = r'public|private|protected'
STATIC = r'( +static)?'
WARD = r'(\w+)'
ZERO_BLANK = r' *'
ONE_BLANK = r' +'
ANYTHING = '(?: +(.*))?'
PARENTHESES = '\((.*)\)'
TYPE_NAME = '(\w+|\w+<\w+>)'


# public +(class|interface) +(\w+)
CLASS_NAME_LINE = r'public' + ONE_BLANK + CLASS_TYPE_NAME + ONE_BLANK + WARD

# *public | private | protected
ACCESS_MODIFIER_LINE = ZERO_BLANK + ACCESS_MODIFIER

# ( *= *(.+))?
VARIABLE_VALUE = '(' + ZERO_BLANK + '=' + ZERO_BLANK + '(.+))?'

#  *(public|private|protected)( +static)? +(\w+|\w+<\w+>) +(\w+)( *= *(.+))?;
VARIABLE_LINE = ZERO_BLANK + '(' + ACCESS_MODIFIER + ')' + STATIC + ONE_BLANK + TYPE_NAME + ONE_BLANK + WARD + VARIABLE_VALUE + ';'

# *(public|private|protected)( +static)?(?: +(.*))? +(\w+) *\((.*)\)
METHOD_LINE = ZERO_BLANK + '(' + ACCESS_MODIFIER + ')' + STATIC + '(?: ' + TYPE_NAME + ')' + ONE_BLANK + WARD + ZERO_BLANK + PARENTHESES
