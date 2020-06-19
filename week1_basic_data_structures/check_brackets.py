# python3

def find_mismatch(text):
    stack = []
    dict = {")":"(","]":"[","}":"{"}
    
    for i, char in enumerate(text):
        if char not in dict.values() and char not in dict.keys(): continue
        if char in dict.values():
            stack.append((char,i))
        elif not stack:
            return i + 1
        else:
            if dict[char] != stack.pop()[0]:
                return i + 1
    if not stack:
        return -1
    else:
        return stack.pop()[1] + 1

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1: print("Success")
    else: print(mismatch)


if __name__ == "__main__":
    main()
