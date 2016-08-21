total = 0
count = 0

try:
    while True:
        line = input("An integer, or `ENTER` to end input: ")
        if line == "":
            break
        try:
            total += int(line)
            count += 1
        except ValueError:
            print(line, "is not a valid input")
        else:
            pass
except:
    print("Ended getting data")
finally:
    try:
        print("\nAvg: %.2f" % (total / float(count)))
        print("Sum: %d" % total)
    except:
        print("\nNo Data")
