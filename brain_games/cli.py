import prompt

def welcome_user(who):
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')

def main():
    welcome_user()

if __name__ == '__main__':
    main()



