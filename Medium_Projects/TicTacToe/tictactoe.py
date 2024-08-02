import random#,keyboard
class TicTacToe():
    def printTable(self):print(('\nO'+'-'*11+'O\n')+('\n|'+('-'*3+'+')*2+'---|\n').join('|'+'|'.join(i)+'|'for i in[[str(i).center(3,' ')for i in j] for j in self.tab])+('\nO'+'-'*11+'O\n'))
    def tras(self,tab):return [[tab[j][i] for j in range(len(tab[0]))]for i in range(len(tab))]
    def __init__(self):
        self.tab = [[' ']*3 for i in range(3)]
        self.end = False
    def playerMove(self,pos):
        if pos>=0 and pos<=8 and self.tab[pos//3][pos%3] == ' ':
            self.tab[pos//3][pos%3] = 'X'
            self.printTable()
            self.aiMove()
        else:print('Positional Error.')  
    def checkRows(self):
        for k in 'XO':
            if sum(1 for i in self.tab if i.count(k)==3)+sum(1 for i in range(3) if sum(1 for j in self.tab if j[i]==k)==3)+ (1 if [self.tab[i][i] for i in range(3)].count(k)==3 or [self.tab[i][2-i] for i in range(3)].count(k)==3 else 0) > 0:
                print('The Winner Is: ' + k + ' !!!')
                self.end = True
                return k
        if sum(i.count(' ') for i in self.tab) == 0:
            print('There Has Been A Tie!!!')
            self.end = True
            return 'Tie'
    def check2InRow(self):
        for k in 'OX':
            tabT = self.tras(self.tab[:])
            diag1 = [self.tab[i][i] for i in range(3)]
            diag2 = [self.tab[i][2-i] for i in range(3)]
            for i in range(3):
                if self.tab[i].count(k) == 2 and ' ' in self.tab[i]:return [i,self.tab[i].index(' ')]
            for i in range(3):
                if tabT[i].count(k) == 2 and ' ' in tabT[i]:return [tabT[i].index(' '),i]
            if diag1.count(k)==2 and ' ' in diag1:return [diag1.index(' '),diag1.index(' ')]
            if diag2.count(k)==2 and ' ' in diag2:return [diag2.index(' '),2-diag2.index(' ')]
    def aiMove(self):
        if self.checkRows() != None: return
        if sum(i.count('X') for i in self.tab) == 1:
            if self.tab[1][1] == ' ': self.tab[1][1] = 'O'
            else:
                ran=2
                while ran==2:ran=random.randint(0,4)
                ran*=2
                self.tab[ran//3][ran%3] = 'O'
        else:
            pos = self.check2InRow()
            if pos != None: self.tab[pos[0]][pos[1]] = 'O'
            else:
                done = False
                for i in range(5):
                    if self.tab[(i*2)//3][(i*2)%3] == ' ' and not done:
                        self.tab[(i*2)//3][(i*2)%3] = 'O'
                        done = True
                for i in range(1,8,2):
                    if self.tab[i//3][i%3] == ' ' and not done:
                        self.tab[i//3][i%3] = 'O'
                        done = True
        self.printTable()
        self.checkRows()
while True:
    print('\n\n===== NEW GAME =====\n\n')
    t = TicTacToe()
    while not t.end:
        resp = input('New Position:   ')
        if resp.isdigit() and int(resp)>= 1 and int(resp)<= 9: resp = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}[int(resp)]
        else: resp = -1
        '''
        print('New Position:   ')
        resp = keyboard.read_key()
        if resp.isdigit() and int(resp)>= 1 and int(resp)<= 9: resp = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}[int(resp)]
        else: resp = -1
        '''
        t.playerMove(resp)
        






























            
            
        
