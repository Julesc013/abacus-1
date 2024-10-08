t010 = {
    '0000':'null',
    '0001':['io','mi'],
    '0010':['io','mi'],
    '0011':['io','mi'],
    '0100':['io','mi'],
    '0101':['io','ai'],
    '0110':['io','j'],
    '0111':['io','jc'],
    '1000':['io','jz'],
    '1001':['io','mi'],
    '1010':['io','mi'],
    '1011':['io','mi'],
    '1100':['io','mi'],
    '1101':['fo','ai'],
    '1110':['ao','oi'],
    '1111':'hlt',
    }
t011 = {
    '0000':'null',
    '0001':['ro','ai'],
    '0010':['ro','bi'],
    '0011':['ro','bi'],
    '0100':['ao','ri'],
    '0101':'null',
    '0110':'null',
    '0111':'null',
    '1000':'null',
    '1001':['ro','bi'],
    '1010':['ro','bi'],
    '1011':['ro','bi'],
    '1100':['ro','bi'],
    '1101':'null',
    '1110':'null',
    '1111':'null',
    }
t100 = {
    '0000':'null',
    '0001':'null',
    '0010':['eo','ai','fi'],
    '0011':['eo','ai','su','fi'],
    '0100':'null',
    '0101':'null',
    '0110':'null',
    '0111':'null',
    '1000':'null',
    '1001':['eo','ai','xr','fi'],
    '1010':['eo','ai','an','fi'],
    '1011':['eo','ai','or','fi'],
    '1100':['eo','ai','nt','fi'],
    '1101':'null',
    '1110':'null',
    '1111':'null',
    }

def zeroes(string,figures):
    figures = figures-len(string)
    return '0'*int(figures)+string

def signals(*signals):
    hlt,mi,ri,ro,io,ii,ai,ao,eo,su,bi,oi,ce,co,j,fi,xr,an,ore,nt,fo,jc,jz = '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    if 'hlt' in signals:
        hlt = '1'
    if 'mi' in signals:
        mi = '1'
    if 'ri' in signals:
        ri = '1'
    if 'ro' in signals:
        ro = '1'
    if 'io' in signals:
        io = '1'
    if 'ii' in signals:
        ii = '1'
    if 'ai' in signals:
        ai = '1'
    if 'ao' in signals:
        ao = '1'
    if 'eo' in signals:
        eo = '1'
    if 'su' in signals:
        su = '1'
    if 'bi' in signals:
        bi = '1'
    if 'oi' in signals:
        oi = '1'
    if 'ce' in signals:
        ce = '1'
    if 'co' in signals:
        co = '1'
    if 'j' in signals:
        j = '1'
    if 'fi' in signals:
        fi = '1'
    if 'xr' in signals:
        xr = '1'
    if 'an' in signals:
        an = '1'
    if 'ore' in signals:
        ore = '1'
    if 'nt' in signals:
        nt = '1'
    if 'fo' in signals:
        fo = '1'
    if 'jc' in signals:
        jc = '1'
    if 'jz' in signals:
        jz = '1'
    return jz+jc+fo+nt+ore+an+xr+fi+j+co+ce+oi+bi+su+eo+ao+ai+ii+io+ro+ri+mi+hlt

def control(inst,time):
    if time == '000':
        return signals('mi','co')
    elif time == '001':
        return signals('ro','ii','ce')
    elif time == '010':
        if type(t010[inst]) is list or tuple:
            return signals(*t010[inst])
        elif type(t010[inst]) is str:
            return signals(t010[inst])
    elif time == '011':
        if type(t011[inst]) is list or tuple:
            return signals(*t011[inst])
        elif type(t011[inst]) is str:
            return signals(t010[inst])
    elif time == '100':
        if type(t100[inst]) is list or tuple:
            return signals(*t100[inst])
        elif type(t100[inst]) is str:
            return signals(t100[inst])
    else:
        return '0000'

def program(address):
    address = zeroes(bin(address)[2:],7)
    time = address[-3:]
    inst = address[:4]
    return zeroes(hex(int(control(inst,time),2))[2:],6)

with open('Logisim Microcode','w+') as output:
    output.write('v2.0 raw\n')
    for index in range(0,128):
        line = program(index)
        print(zeroes(hex(index)[2:].upper(),2)+') '+line)
        output.write(line+'\n')
