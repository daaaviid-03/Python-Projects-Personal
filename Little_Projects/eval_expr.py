def calc(e):
    if '--' in e:
        while '--' in e: e = e.replace('--','')
    elif '(' in e:
        pos = e.find('(')
        cont, i, ex  = 0, pos, False
        while i < len(e) and not ex:
            if e[i] == '(': cont += 1
            elif e[i] == ')': cont -= 1
            ex = cont == 0
            if not ex: i += 1
        e = e[:pos] + str(calc(e[pos+1:i])) + e[i+1:]
    elif '*' in e or '/' in e:
        i, c = 0, ''
        while not c and i < len(e):
            if e[i] == '*': c = '*'
            elif e[i] == '/': c = '/'
            else: i += 1
        e1, e2 = e[:i][::-1], e[i+1:]
        x,y = '',''
        
        ex = False
        while len(e1) and not ex:
            d = e1[0]
            if d in '1234567890. ' or (d == '-' and not x):
                x += d if d != ' ' else ''
                e1 = e1[1:]
            else:
                ex = True
            
        e1,x = e1[::-1],x[::-1]
        
        ex = False
        while len(e2) and not ex:
            d = e2[0]
            if d in '1234567890. ' or (d == '-' and not y):
                y += d if d != ' ' else ''
                e2 = e2[1:]
            else:
                ex = True
        print(f'Exp: {e1}, x = {x}, c = {c}, y = {y}, {e2}')
        if c == '*':
            e = e1 + f'{(float(x)*float(y)):.2f}' + e2
        else:
            e = e1 + f'{(float(x)/float(y)):.2f}' + e2
        print(e)
    elif '+' in e or '-' in e:
        i, c = 0, ''
        while not c and i < len(e):
            if e[i] == '+': c = '+'
            elif e[i] == '-': c = '-'
            else: i += 1
        e1, e2 = e[:i][::-1], e[i+1:]
        x,y = '',''
        
        ex = False
        while len(e1) and not ex:
            d = e1[0]
            if d in '1234567890. ' or (d == '-' and not x):
                x += d if d != ' ' else ''
                e1 = e1[1:]
            else:
                ex = True
            
        e1,x = e1[::-1],x[::-1]
        
        ex = False
        while len(e2) and not ex:
            d = e2[0]
            if d in '1234567890. ' or (d == '-' and not y):
                y += d if d != ' ' else ''
                e2 = e2[1:]
            else:
                ex = True
        print(f'Exp: {e1}, x = {x}, c = {c}, y = {y}, {e2}')
        if x == '':x = '0'
        if c == '+':
            e = e1 + f'{(float(x)+float(y)):.2f}' + e2
        else:
            e = e1 + f'{(float(x)-float(y)):.2f}' + e2
        print(e)

    
    try:
        return float(e)
    except:
        return calc(e)
        
    
