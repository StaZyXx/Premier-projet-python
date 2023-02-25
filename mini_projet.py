# -*- coding: utf-8 -*-
def newBoard(n):
    board=[]
    for i in range(n):       
        board.append([0]*n)
    return board

def displayBoard(board,n):
    for i in range (n):
        if i>=9:
            print(i+1,"|",end="")
        if i<=8:
            print(i+1,"","|",end="")
        for j in range(n):
            if board[i][j] == 0:
                print(".","",end=" ")
            elif board[i][j] == 1:
                print("x","",end=" ")
            elif board[i][j] == 2:
                print("o","",end=" ")
        print()
    print(((n*3)+3)*"-")
    print("    ",end="")
    for k in range(len(board)):
        if k<=8:
            print(k+1," ",end="")
        if k>=9:
            print(k+1,"",end="")
            
def displayScore(score):
    print()
    print("Le score est de:",score[0],"à",score[1])
    
def possibleSquare(board,i,j):
        if board[i][j] == 0:
            return True
        return False

def selectSquare(board,n):
   m=0
   while m == 0:
       ij=[]
       horizontal = int(input("Selectionez une ligne: "))-1
       vertical = int(input("Selectionez une colonne: "))-1
       ij.append(horizontal)
       ij.append(vertical)
       if possibleSquare(board,horizontal,vertical):
           return ij
       else:
           return("Numéro invalide")

def updateBoard(board,player,i,j):
    if player == 1:
        board[i][j] = 1
    elif player == 2:
        board[i][j] = 2
    
def updateScore(board, n, player, i, j): 
    point=0
    i_bis = i
    j_bis = j
    if (i == 0 and j == 0) or (i==n-1 and j==n-1):
        i=0
        j=0
        for k in range(n):
            if board[i][j]==player:
                point+=1
            elif board[i][j] == 0:
                return 0
            i,j = i+1,j+1
    elif (i == 0 and j == n-1) or ( i==n-1 and j==0) :
        i=0
        j=n-1
        for k in range(n):
            if board[i][j] == player:
                point+=1
            elif board[i][j] == 0:
                return 0            
            i,j = i+1,j-1
    else:
        somme_point1 = 0
        while i > 0 and j > 0 : 
            i -= 1
            j -= 1
        while i <= n-1 and j <= n-1:
            if board[i][j] == player:
                somme_point1 += 1
            elif board[i][j] == 0:
                somme_point1 = 0
                break
            else :
                pass
            i+=1
            j+=1
        i = i_bis
        j = j_bis
        somme_point2 = 0
        while i > 0 and j < n-1 :
            i -= 1
            j += 1
        while i <= n-1 and j >= 0:
            if board[i][j] == player:
                somme_point2 += 1
            elif board[i][j] == 0:
                somme_point2 = 0
                break
            else :
                pass
            i+=1
            j-=1
        point = somme_point1 + somme_point2
    return point
                      
def again(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return True
    return False

def win(score):
    if score[0]>score[1]:
        print("Le Gagnant est player1")
    elif score[0]==score[1]:
        print("Match nul")
    else:
        print("Le gagnant est player2")        

def diagonals(n):
    player = 1
    score = [0,0]
    board= newBoard(n)
    displayBoard(board, n)
    displayScore(score)
    while again(board, n) == True:
        liste = selectSquare(board, n)
        updateBoard(board, player,liste[0],liste[1])
        m=updateScore(board, n, player,liste[0],liste[1])
        score[player-1] = score[player-1]+m
        displayBoard(board, n)
        displayScore(score)
        if player == 1:
            player += 1
        else:
            player -= 1
    print(win(score))
diagonals(3)
        
        
        
    
    
    