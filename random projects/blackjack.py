import random


jcounter = 0
kcounter = 0
jscore = 0
kscore = 0
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False 
winner = ""

def is_game_over(k, j):
    if (k == 21 or j > 21):
        winner = "k"
        game_over = True
    elif (j == 21 or k > 21):
        winner = "j"
        game_over = True

def j_move(jscore):
    if jscore < 21:
        return "jh"
    else:
        return "js"

def k_move(kcore):
    if kscore < 21:
        return "kh"
    else:
        return "ks"   

def get_card():
    value = 0
    j = random.randint(0, 51)
    if x[j] != None:
        value = x[j]
    else:
        while (not x[j]):
            j = random.randint(0, 51)
        value = x[j]
    x[j] = None 
    return value
    
    
    
if __name__ == "__main__":
    
    for i in xrange(1, 1000):

        jscore = 0
        kscore = 0
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        game_over = False 
        winner = ""
        
        turn = random.randint(0, 1)
        if turn == 0:
            input = k_move(kscore)
        else:
            input = j_move(jscore)
     
       
        
        while not game_over:   
            if (input == "kh"):
                is_game_over(kscore, jscore)
                if game_over:
                    break
                card = get_card()
                kscore+= card
                input = k_move(kscore)
            elif (input == "ks"):
                input = j_move(jscore)
                if (input == "js"):
                    if (kscore > jscore):
                        winner = "k"
                        game_over = True
                        break
                    else:
                        winner = "j"
                        game_over = True   
                        break
            elif (input == "jh"):
                is_game_over(kscore, jscore)
                if game_over:
                    break
                card = get_card()
                jscore+= card
                input = j_move(jscore)
            elif (input == "js"):
                input = k_move(kscore)
                if (input == "ks"):
                    if (kscore > jscore):
                        winner = "k"
                        game_over = True
                        break
                    else:
                        winner = "j"
                        game_over = True  
                        break
        print "karan",kscore
        print "jack",jscore
        print winner
        #print winner, "won! - KO!"
        if winner == "k":
            kcounter += 1
        else:
            jcounter += 1
        
    print "Karan's wins = ", kcounter
    print "Jack's wins = ", jcounter