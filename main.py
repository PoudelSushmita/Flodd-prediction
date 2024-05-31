def main():
    print('This is main function')
    helper_function() # i am from main branch
    helper_function() # hello there

def helper_function():
    print("This is helper function")

if __name__ == '__main__':
    main()