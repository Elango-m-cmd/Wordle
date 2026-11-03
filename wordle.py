import random 
def words():
    f1=open(r"C:\Users\ADMIN\Downloads\5-letter-words.txt","r")
    words=f1.readlines()
    f1.close()
    return words

def wordle():
    word_list=words()
    word=random.choice(word_list).strip()
    print("Welcome to Wordle!")
    attempts=6
    while attempts>0:
        guess=input("Enter your 5-letter guess: ").strip().lower()
        if guess==word:
            print("🟩 🟩 🟩 🟩 🟩\nCongratulations! You've guessed the word correctly.")
            break
        elif guess+'\n' not in word_list:
            print("Word not found.")
            continue
        else:
            r=['⬛','⬛','⬛','⬛','⬛']
            wl,gl=list(word),list(guess)
            for i in range(5):
                if gl[i]==wl[i]:
                    r[i]='🟩'
                    wl[i]='0'
                    gl[i]='1'
            for i in range(5):   
                if gl[i] in wl:
                    r[i]='🟧'
                    wl[wl.index(gl[i])]='2'              
            print(' '.join(r))
            attempts-=1
            print(f"You have {attempts} attempts left.")
    else:
        print("Sorry, you've run out of attempts. The correct word was '%s'."%word)

#wordle()
print(words())