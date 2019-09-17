#!usr/bin/python3
#Author Fredrick Pwol
'''
Conversion of color system from one to another e.g from R.G.B to H.S.L
and checking of any color shade given in either hexadecimal or r,g,b
The # symbol can be ommited if you don't want to to include it and can 
also be written with the value.
conversions:
rgb => Hex; Hex => rgb; rgb => hsl; hsl => rgb; hsv => rgb ; rgb => cmyk; cmyk => rgb

and color checking to which return the shade of the color passed in.
list of all color shades:
*red
*green
*blue
*yellow
*orange or brown
*pink
*cyan
*magenta
*red-orange
*orange-yellow
*green-cyan
*cyan-blue
*blue-magenta
*magenta-pink
*pink-red
*grey
*black
*white

'''


#resources:
#http://www.workwithcolor.com/color-names-01.htm
#https://www.wikipedia.org/wiki/HSL_and_HSV


import re
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

def toColor(color :str):
    '''
    Checks color passed in in r,g,b or hex and returns the 
    color range of the value passsed in.
    '''
    hexa = re.compile(r'#?([a-f]|\d){6}',re.I)
    regb =re.compile(r'(\d+)(,\d+){2}')
    if hexa.match(color) or regb.match(color):
        if hexa.match(color):
            form = Hexrgb(color)
            red,green,blue = form
        elif regb.match(color):
            red,green,blue = tuple(color.split(','))
    else:
        print('Sorry no matching color found use Either RGB of hexadecimal colors ')
    red = int(red)
    green = int(green)
    blue = int(blue)
    hue = rgbHsl(red,green,blue)[0]
    bright = rgbHsl(red,green,blue)[2]
    hue =floor(hue)
    rd = list(range(0,11))
    rd.extend(range(355,361))
    if red == 255 and green == 255 and blue == 255:
        return 'white'
    elif red == 0 and green == 0 and blue == 0:
        return 'black'
    elif red == blue == green:
        return 'grey'
    elif red in range(50,256) and green in range(0,195) and blue in range(0,195) and hue in rd:
        return 'red'
    elif red in range(181,256) and green in range(166,256) and blue in range(0,256) and hue in range(51,61):
        return 'yellow'
    elif red in range(0,179) and green in range(72,256) and blue in range(0,176) and hue in range(81,141):
        return 'green'
    elif red in range(0,156) and green in range(79,256) and blue in range(79,256) and hue in range(170,201):
        return 'cyan'
    elif red in range(0,43) and green in range(0,83) and blue in range(102,256) and hue in range(221,241):
        return 'blue'
    elif red in range(93,256) and green in range(0,160) and blue in range(84,256) and hue in range(281,321):
        return 'magenta'
    elif red in range(86,256) and green in range(0,209) and blue in range(25,220) and hue in range(331,346):
        return 'pink'
    elif red in range(109,256) and green in range(53,153) and blue in range(0,123) and hue in range(11,21):
        return 'red-orange'
    elif red in range(61,256) and green in range(43,246) and blue in range(0,239) and hue in range(21,41):
        return 'orange or brown'
    elif red in range(145,256) and green in range(113,249) and blue in range(0,227) and hue in range(41,51):
        return 'orange-yellow'
    elif red in range(75,224) and green in range(83,256) and blue in range(0,131) and hue in range(61,81):
        return 'orange-green' 
    elif red in range(0,179) and green in range(36,256) and blue in range(32,213) and hue in range(141,170):
        return 'green-cyan'
    elif red in range(0,240) and green in range(33,248) and blue in range(71,255) and hue in range(201,221):
        return 'cyan-blue'
    elif red in range(42,192) and green in range(0,149) and blue in range(150,228) and hue in range(241,281):
        return 'blue-magenta'
    elif red in range(97,256) and green in range(0,240) and blue in range(81,246) and hue in range(321,330):
        return 'magenta-pink'
    elif red in range(101,256) and green in range(0,194) and blue in range(11,205) and hue in range(346,356):
        return 'pink-red'
    else:
        if 0.0 <= bright <= 0.15:
            return 'black'
        elif 0.16 <= bright <= 0.84:
            return 'grey'
        elif 0.85 <= bright <= 1.0:
            return 'white'