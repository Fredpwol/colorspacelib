#!usr/bin/python3
import re
from colorspacelib import converter
from math import floor

class NoColorError(Exception):pass # Color Exception.

class Color():

    def __init__(self,color:str):
        self.__hexa = re.compile(r'#?([a-f]|\d){6}',re.I)
        self.__regb =re.compile(r'(\d+)(,\d+){2}')
        # validity Checker.
        if self.__hexa.match(color):
            if color.startswith('#'):
                tempcolor = color[1:]
                if len(tempcolor) != 6:
                    raise NoColorError('Hexadecimal colors must be 6 values.')   
            else:
                tempcolor = color
                if len(tempcolor) != 6:
                    raise NoColorError('Hexadecimal colors must be 6 values.')
        elif self.__regb.match(color):
            tempcolor = tuple(map(int,color.split(',')))
            for values in tempcolor:
                if values not in range(0,256):
                    raise NoColorError('Color range must be inbetween 0 - 255.')
        self.color = color
        if self.__regb.match(self.color):
            self.rgbcolor = tuple(map(int,self.color.split(',')))


    def __add__(self,other):
        # Additive color mixer.
        if self.__hexa.match(self.color) or self.__hexa.match(other.color):
            first = self.toRgb()
            second = other.toRgb()
        elif self.__regb.match(self.color) and self.__regb.match(other.color):
            first = self.rgbcolor
            second = other.rgbcolor
        
        newcolor = list(map(lambda val: val%255,[int((x+y)/2) for x,y in list(zip(first,second))]))
        newcolor = list(map(str,newcolor))
        colorparse = ','.join(newcolor)
        return Color(colorparse)



    def __str__(self):
        return str(self.color)

    def shade(self):
        '''
        Checks color passed in in r,g,b or hex and returns the 
        color range of the value passsed in.
        '''
        if self.__hexa.match(self.color) or self.__regb.match(self.color):
            if self.__hexa.match(self.color):
                form = converter.Hexrgb(self.color)
                red,green,blue = form
            elif self.__regb.match(self.color):
                red,green,blue = tuple(self.color.split(','))
        else:
            print('Sorry no matching color found use Either RGB of hexadecimal colors ')
        red = int(red)
        green = int(green)
        blue = int(blue)
        hue = converter.rgbHsl(red,green,blue)[0]
        bright = converter.rgbHsl(red,green,blue)[2]
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
            return 'yellow-green' 
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


    def toRgb(self):
        '''
        hex to rgb converter
        Arguments: dec = hexadecimal color to convert
        retuns a string of rgb color.
        '''
        if self.__regb.match(self.color):
            return self.rgbcolor

        assert self.color == str(self.color)
        if self.color.startswith('#'):
            self.color = self.color[1:]
        
        r=int(self.color[0:2],base=16)
        g=int(self.color[2:4],base=16)
        b=int(self.color[4:6],base=16)
        color=(r,g,b)
        return color


    def toHex(self):
        '''
        rgb to hex converter
        Arguments: r = red channel
                g = green channel
                b = blue channel

        Pass in the Value sequentialy
        '''
        if self.__hexa.match(self.color):
            return self.color
        r,g,b = self.rgbcolor
        assert r <= 255 and r >= 0 
        assert g <= 255 and g >= 0 
        assert b <= 255 and b >= 0 
        r=format(r,'x').zfill(2)
        g=format(g,'x').zfill(2)
        b=format(b,'x').zfill(2)
        hex_string='#%s%s%s'%(r,g,b)
        return hex_string


    def toHsl(self):
        if self.__hexa.match(self.color):
            red,green,blue = self.toRgb()
        else:
            red,green,blue = self.rgbcolor
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


