from math import floor


def rgbHex(r,g,b :int):
    '''
    rgb to hex converter
    Arguments: r = red channel
               g = green channel
               b = blue channel

    Pass in the Value sequentialy
    '''
    assert r <= 255 and r >= 0 
    assert g <= 255 and g >= 0 
    assert b <= 255 and b >= 0 
    r=format(r,'x').zfill(2)
    g=format(g,'x').zfill(2)
    b=format(b,'x').zfill(2)
    hex_string='#%s%s%s'%(r,g,b)
    return hex_string



def Hexrgb(dec):
    '''
    hex to rgb converter
    Arguments: dec = hexadecimal color to convert
    retuns a string of rgb color.
    '''
    assert dec == str(dec)
    if dec.startswith('#'):
        dec = dec[1:]
    
    r=int(dec[0:2],base=16)
    g=int(dec[2:4],base=16)
    b=int(dec[4:6],base=16)
    color=(r,g,b)
    return color

def hsvRgb(hue,sat,val):
    '''
    converts hue,saturation and value passed in to rgb 
    '''
    assert 0 <= hue <= 360 
    assert 0 <= sat <= 100
    assert 0 <= val <= 100
    sat /= 100
    val /= 100
    chroma = val * sat
    h = hue/60
    x = chroma *(1-(h%2-1))
    if 0 <= h <= 1:
        R1,G1,B1 = (chroma,x,0)
    elif 1 <= h <= 2:
        R1,G1,B1 = (x,chroma,0)
    elif 2 <= h <= 3:
        R1,G1,B1 = (0,chroma,x)
    elif 3 <= h <= 4:
        R1,G1,B1 = (0,x,chroma) 
    elif 4 <= h <= 5:
        R1,G1,B1 = (x,0,chroma)
    elif 5 <= h <= 6:
        R1,G1,B1 = (chroma,0,x) 
    else:
        R1,G1,B1 = (0,0,0)
    m = val-chroma
    R,G,B = ((R1+m)*255,(G1+m)*255,(B1+m)*255)
    if R > 255:
        R=R % 255
    elif G > 255:
        G=G%255
    elif B > 255:
        B=B%255
    return floor(R),floor(G),floor(B) 


def rgbHsv(red,green,blue):
    r =red/255
    g = green/255
    b = blue/255
    cmax = max(r,g,b)
    cmin = min(r,g,b)
    delta = cmax - cmin
    if cmax == cmin:
        hue = 0
    elif cmax == r:
        hue = 60*((g-b)/delta )%360
    elif cmax == g:
        hue = 60*((b-r)/delta + 2)
    elif cmax == b:
        hue = 60*((r-g)/delta + 4)
    

    if cmax == 0:
        sat = 0
    else:
        sat = delta/cmax
    val = cmax

    sat *= 100
    val *= 100

    return round(hue,2),round(sat,2),round(val,2)


def hslRgb(hue,sat,lum):
    assert 0 <= hue <= 360
    assert 0 <= sat <= 100
    assert 0 <= lum <= 100
    sat /= 100
    lum /= 100
    chroma = (1-(2*lum -1)) * sat
    h = hue/60
    x = chroma *(1-(h%2-1))
    if 0 <= hue <= 60:
        R1,G1,B1 = (chroma,x,0)
    elif 60 <= hue <= 120:
        R1,G1,B1 = (x,chroma,0)
    elif 120 <= hue <=180:
        R1,G1,B1 = (0,chroma,x)
    elif 180 <= hue <= 240:
        R1,G1,B1 = (0,x,chroma) 
    elif 240 <= hue <= 300:
        R1,G1,B1 = (x,0,chroma)
    elif 300 <= hue <= 360:
        R1,G1,B1 = (chroma,0,x) 
    else:
        R1,G1,B1 = (0,0,0)
    m = lum-chroma/2
    R,G,B = ((R1+m)*255,(G1+m)*255,(B1+m)*255)
    return floor(R),floor(G),floor(B)    


def rgbHsl(red,green,blue):

    r =round(red/255,2)
    g = round(green/255,2)
    b = round(blue/255,2)
    cmax = max(r,g,b)
    cmin = min(r,g,b)
    delta = round(cmax - cmin,2)
    if delta == 0 :
        hue = 0
    elif cmax == r:
        hue = (g-b)/delta % 6
    elif cmax == g:
        hue = (b-r)/delta + 2
    elif cmax == b:
        hue = (r-g)/delta + 4

    hue *= 60

    lum = (cmax + cmin)/2


    if delta == 0:
        sat = 0
    elif lum <= 0.5:
        sat = delta/(cmax+cmin)
    else:
        sat = delta/(2-cmax-cmin)

    return round(hue,2),round(sat,2),round(lum,2)



def rgbCmyk(red,green,blue):
    '''
    converts rgb to cmyk arguments range from 0 - 255
    values returned range from 0-100%
    '''
    r = red/255
    g = green/255
    b = blue/255

    k = 1-max(r,g,b)
    
    c = (1-r-k)/(1-k)*100
    m = (1-g-k)/(1-k)*100
    y = (1-b-k)/(1-k)*100
    k *= 100
    return floor(c),floor(m),floor(y),floor(k)


def cmykRgb(c,m,y,k):
    '''
    converts cmyk to rgb all aurguments range from 0 to 100%
    '''
    assert 0 <= c <= 100
    assert 0 <= m <= 100
    assert 0 <= y <= 100
    assert 0 <= k <= 100
    c /=100
    m /= 100
    y /= 100
    k /= 100
    red = 255*(1-c)*(1-k)
    green =255*(1-m)*(1-k)
    blue = 255*(1-y) * (1-k)

    return floor(red),floor(green),floor(blue)
