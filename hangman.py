import random

             
def hangman():  
               
                guesses=["jack","apple","abdullah","muawia","banana"]
                hanger_body={1:"O",2:"|",3:"/",4:"\\",5:"/",6:"\\"}
        
                hangman=f"  ___\n |   |\n |   1\n |  324 \n |  5 6\n___"
               
                print(hangman)
                #---------------------------------------    
                chooser=random.choice(guesses)
                user="-"*len(chooser)
                print(user)
                hanger=0
                detected=[]
             
                while  hanger<6 and "-" in user:
                 input_=str(input())
                 input_=input_.lower()
                 if input_ in detected:
                    print(f"{input_} is already used \n try something else . . .")
                 else:
                    if input_ in chooser:
                        for i in range(chooser.count(input_)):
                          detected.append(input_)
                          index=int(chooser.index(input_))
                          user=user[:index]+input_+user[index+1:]
                          chooser=chooser[:index]+"."+chooser[index+1:]
                    
                          print(hangman)
                          print(user)
                    else:
                          hanger+=1
                          detected.append(input_)
                          hangman=hangman.replace(str(hanger),hanger_body[hanger])
                          print(hangman)    
                          print(user)
                if hanger==6:
                    print(f"your player is hanged the word was {chooser}" )
                else:
                    print("you Won")   

   
                #print(detected)   


     
if __name__=="__main__":

 hangman()
