from User import user
from typing import List

class palindrome:
    def __init__(self) -> None:
        self.u_input = user()
    
    def create_reverse(self) -> List[str]:
        u_output = self.u_input.userInput()
        print(u_output)
        og_palin = []
        
        if isinstance(u_output, int) == True:
            palin = str(self.u_input)
        else: 
            palin = u_output
            
        for char in palin:
            og_palin.append(char)
        rev_palin = reversed(og_palin)
        rev_palin_list = list(rev_palin)
        print(og_palin)
        print(rev_palin_list)
        
        return og_palin, rev_palin_list
    
    def is_palindrome(self, og_palin:List[str], rev_palin_list: List[str]) -> str:
        if og_palin == rev_palin_list:
            return 'This is a palindrome'
        else:
            return 'This is not a palindrome'
        
if __name__ == '__main__':
    palin_obj = palindrome()
    og_palin, rev_palin_list = palin_obj.create_reverse()
    result = palin_obj.is_palindrome(og_palin, rev_palin_list)
    print(result)
        

        
        