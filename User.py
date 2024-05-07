import typing

class user:
    def userInput(self) -> int or str:
        c_input = input("Enter 's' for string input and 'i' for an integer input or 'q' to quit: ")
        
        while True:
            if c_input == 's':
                str_input = input('Enter your string input here: ')
                print(f'You have entered: {str_input}')
                return str_input
            elif c_input == 'i':
                int_input = int(input('Enter your interger input here: '))
                print(f'You have entered: {int_input}')
                return int_input
            elif c_input == 'q':
                print('Exiting.......')
                return None
            else:
                print('That is not an option, Pick again.')
                return None
