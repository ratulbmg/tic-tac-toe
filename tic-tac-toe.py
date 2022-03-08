# TIC-TAC-TOE
import numpy
array=[['_','_','_'],['_','_','_'],['_','_','_']]
p1='o' ; p2='x'

def row_chq(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if array[r][c]==symbol:
                count+=1
    if count==3:
        return True
    else:
        return False


def col_chq(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if array[r][c]==symbol:
                count+=1
    if count==3:
        return True
    else:
        return False


def right_dig_chq(symbol):
    for i in range(3):
        count=0
        if array[i][2-i]==symbol: #[n-i-1]
            count+=1
    if count==3:
        return True
    else:
        return False


def left_dig_chq(symbol):
    count=0
    for i in range(3):
            if array[i][i]==symbol:
                count+=1
    if count==3:
        return True
    else:
        return False


def won(symbol):
    if row_chq(symbol) or col_chq(symbol) or right_dig_chq(symbol) or left_dig_chq(symbol):
        return True
    else:
        return False

def pos(symbol):
    print(numpy.matrix(array))
    while True:
        r=int(input('please enter row - 1 or 2 or 3 : '))
        c=int(input('please enter row - 1 or 2 or 3 : '))
        if array[r-1][c-1]=='_' and c>0 and c<4 and r>0 and r<4 :
            break
        else:
            print('your input is wrong')
    array[r-1][c-1]=symbol


def play():
    for turn in range(9):
        if turn%2==0:
            print('it is your turn {}'.format(p1))
            pos(p1)
            if won(p1):
                print('you won {}'.format(p1))
                break
        else:
            print('it is your turn {}'.format(p2))
            pos(p2)
            if won(p2):
                print('you won {}'.format(p2))
                break
        if not won(p2) and not won(p1):
            print('match draw')  
if __name__=='__main__':
    play()