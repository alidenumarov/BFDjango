if __name__ == '__main__':
    s = input()
    
    print(True in [True if el.isalnum() else False for el in s])
    print(True in [True if el.isalpha() else False for el in s])
    print(True in [True if el.isdigit() else False for el in s])
    print(True in [True if el.islower() else False for el in s])
    print(True in [True if el.isupper() else False for el in s])
        
