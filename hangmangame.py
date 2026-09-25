 
import random
import word_file
random_word = random.choice(word_file.words)
choice = 6
list = []
print(random_word)
for i in range(len(random_word)):
    list += '_'
print(list)
game_over = False
while not game_over:
     guessed_letter =  input("Guess a letter:").lower()  
     print(f"you have {choice} choices")
     
     
     for position in range(len(random_word)):
         
         letter = random_word[position]

         if letter == guessed_letter:
             list[position] = guessed_letter
         
     print(list)
     
     

             
     if guessed_letter not in random_word:
         choice -= 1
         if choice == 0:
             game_over=True
             print("You lose!")

     if '_' not in list:
         game_over=True
         print("You win")
             
     
             
             
             
            



# for letter in range(1,len(random_word)+1):
#       if  letter == guessed_letter:
#          list = list[letter].replace(guessed_letter[letter])
# print(list)
        
       
      
      