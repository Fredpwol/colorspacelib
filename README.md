# ColorSpaceLib

ColorSpaceLib is a python color library designed to make working with color much easier and Intresting with python.

## Installation

```bash
pip install colorspacelib
```

## Usage

```python
>>> from colorspacelib.colorspace import Color
>>> mygreen = Color('#7CFC00')
>>> mygreen.shade()
'green'
>>> myorange = Color('255,179,71')
>>> myorange.shade()
'orange or brown'
>>> myred = Color('D73B3E')
>>> myred.shade()
'red'
```

The Colorspacelib package comes with some predifined colors which can be imported and used in your script.

```python
>>> import colorspacelib as csl
>>> print(csl.black)
#000000
>>> print(csl.green)
#00ff00
>>> print(csl.blue.toRgb())
(0, 0, 255)
```
Color Instances also supports mixing of two color using The [additive](https://www.wikipedia.org/wiki/RGB_color_model) color mixing.

```python
>>> import colorspacelib as csl
>>> new_col = csl.green + csl.yellow
>>> print(new_col)
127,191,0
>>> new_col.shade()
'yellow-green'
```
There is also a converter module inside the colorspacelib that contains function for convertion of a color format to another. The functions are listed as follows :

- Hexrgb
- rgbHex
- rgbHsv
- hsvRgb
- rgbHsl
- hslRgb
- rgbCmyk
- cmykRgb

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This Project is under The [MIT](https://opensource.org/licenses/MIT) License.