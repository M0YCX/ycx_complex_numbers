[![run pytests](https://github.com/M0YCX/ycx_complex_numbers/actions/workflows/run-tests.yml/badge.svg)](https://github.com/M0YCX/ycx_complex_numbers/actions/workflows/run-tests.yml)

# M0YCX Complex Numbers Library

To make representing complex numbers both in complex and polar
form for my Amateur Radio projects (Jupyter Notebooks)...

Provide classes for 2-Port Node Parameter Networks and their conversions/operations:

Name | Class
---- | -----
ABCD/ABCD` Cascade Parameters | Neta & Netb
Y-Parameters | NetY
Z-Parameters | NetZ
Hybrid Parameters | NetH
S-Parameters | NetS

these are being developed as I learn the math...

For more professional use I would recommend looking at
[scikit-rf](https://scikit-rf.readthedocs.io/en/latest/tutorials/Introduction.html) -
I will probably migrate to a library like this eventually.
See interesting features like:
* [Circuits](https://scikit-rf.readthedocs.io/en/latest/tutorials/Circuit.html)
* [Deembedding](https://scikit-rf.readthedocs.io/en/latest/tutorials/Deembedding.html)
* [VNA integation](https://scikit-rf.readthedocs.io/en/latest/api/vi/vna.html)
* ...

## Disclaimer
Don't use this library in any production development, as I am
developing this for my hobby in Amateur Radio...

## License
[MIT License](LICENSE)