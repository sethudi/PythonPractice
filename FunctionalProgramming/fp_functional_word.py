#!./venv/bin/python

def main():
    guesses = set('aeiou')
    word = "fascinate"

    # - a - - i - a - e 
    new_guesses = list(map(lambda x: x if x in guesses else "-", word))
    print(" ".join(new_guesses))


    

if __name__ == "__main__":  
    main()