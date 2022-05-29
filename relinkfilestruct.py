# -*- coding: utf-8 -*-

from construct import *
from pathlib import Path

VersionOneInfo = Struct(
    'mode'/Int16ul,
    'env'/CString('utf8'),
    'repath'/CString('utf8'),
    'abspath'/Default(CString('utf8'), 'none')
)

RELinkFileStruct = Struct(
    'magic'/Const(b'relink'),
    'version'/Enum(Bytes(4), One=b'v1.0'),
    'info'/Switch(
        this.version, {
            'One': VersionOneInfo
        }
    )
)


if __name__ == '__main__':
    info = {'mode': 1, 'env': 'asd asd', 'repath': 'asdasdazcxf'}
    RELinkFileStruct.build_file(dict(version=RELinkFileStruct.version.One, info=info), Path('test.relink'))
