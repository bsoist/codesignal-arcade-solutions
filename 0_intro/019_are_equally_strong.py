def solution(*args):
    return (min(args[:2]) == min(args[2:]) and
            max(args[:2]) == max(args[2:]))