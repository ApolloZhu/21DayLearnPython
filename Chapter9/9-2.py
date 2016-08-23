def track(function):
    def wrapped(*args, **kwargs):
        print("start...")
        function(*args, **kwargs)
        print("end.")
    return wrapped

if __name__ == "__main__":
    @track
    def hello(name):
        print("Hello", name)
    hello("Main")
