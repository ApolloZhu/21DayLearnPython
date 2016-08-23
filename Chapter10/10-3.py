def closure(expression):
    def wrapped(*args, **kwargs):
        return expression(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    addition = closure(lambda lhs, rhs: lhs + rhs)
    print(addition(1,2))
