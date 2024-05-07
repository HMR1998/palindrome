from User import user
from Palindrome import palindrome

if __name__ == '__main__':
    
    palin_obj = palindrome()
    
    og_palin, rev_palin_list = palin_obj.create_reverse()
    result = palin_obj.is_palindrome(og_palin, rev_palin_list)
    print(result)
    