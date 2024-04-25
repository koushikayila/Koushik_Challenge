import re

def validate_credit_card(number):
    # check for patterns
    # starting with 4,5,6 and either 16 digits or 4 digits seperated by '-'
    # no other characters apart from numbers or '-' allowed
    pattern = r'(^[456]\d{3}-\d{4}-\d{4}-\d{4}$)|(^[456]\d{15})'
    
    if re.match(pattern, number):
        # check for same number repeating 4 or more times consectively
        number = number.replace('-', '')
        if re.search(r'(\d)\1{3,}', number):
            return "Invalid"
        return "Valid"
    else:
        return "Invalid"

def main():
    n = int(input())

    for _ in range(n):
        # take each string input
        number = input().strip()
        print(validate_credit_card(number))

if __name__ == "__main__":
    main()