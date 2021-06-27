class textStyles:
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[33m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'


def colorToUse(core):
    if core < 35:
        coreTextColor = textStyles.GREEN
        #print('checking green')
        return coreTextColor
    if core >= 35 and core <= 75:
        coreTextColor = textStyles.YELLOW
        #print('checking yellow')
        return coreTextColor
    if core > 75:
        coreTextColor = textStyles.RED
        #print('checking red')
        return coreTextColor
    else:
        coreTextColor = textStyles.GREEN
        return coreTextColor