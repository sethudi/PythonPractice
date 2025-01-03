#!./venv/bin/python
import re
table = """
Day         Electricity     Coffee      Cleaning
Monday      330             10          50
Tuesday     220             12          40
Wednesday   130             14          80
"""

def main():
    cash_spent = re.findall(r"\d+",table)
    total_cash_spent = 0

    for cash in cash_spent:
        total_cash_spent += int(cash)
    
    print(total_cash_spent)

    text = re.sub(r"^\s*\w+\s*","", table, flags=re.MULTILINE)
    print(text)
    
main()