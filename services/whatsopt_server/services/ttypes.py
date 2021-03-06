#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class SurrogateKind(object):
    SMT_KRIGING = 0
    SMT_KPLS = 1
    SMT_KPLSK = 2
    SMT_LS = 3
    SMT_QP = 4
    OPENTURNS_PCE = 5

    _VALUES_TO_NAMES = {
        0: "SMT_KRIGING",
        1: "SMT_KPLS",
        2: "SMT_KPLSK",
        3: "SMT_LS",
        4: "SMT_QP",
        5: "OPENTURNS_PCE",
    }

    _NAMES_TO_VALUES = {
        "SMT_KRIGING": 0,
        "SMT_KPLS": 1,
        "SMT_KPLSK": 2,
        "SMT_LS": 3,
        "SMT_QP": 4,
        "OPENTURNS_PCE": 5,
    }


class OptimizerKind(object):
    SEGOMOE = 0

    _VALUES_TO_NAMES = {
        0: "SEGOMOE",
    }

    _NAMES_TO_VALUES = {
        "SEGOMOE": 0,
    }


class ConstraintType(object):
    LESS = 0
    EQUAL = 1
    GREATER = 2

    _VALUES_TO_NAMES = {
        0: "LESS",
        1: "EQUAL",
        2: "GREATER",
    }

    _NAMES_TO_VALUES = {
        "LESS": 0,
        "EQUAL": 1,
        "GREATER": 2,
    }


class OptionValue(object):
    """
    Attributes:
     - integer
     - number
     - vector
     - matrix
     - str
    """


    def __init__(self, integer=None, number=None, vector=None, matrix=None, str=None,):
        self.integer = integer
        self.number = number
        self.vector = vector
        self.matrix = matrix
        self.str = str

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.integer = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.number = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.vector = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readDouble()
                        self.vector.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.matrix = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = []
                        (_etype15, _size12) = iprot.readListBegin()
                        for _i16 in range(_size12):
                            _elem17 = iprot.readDouble()
                            _elem11.append(_elem17)
                        iprot.readListEnd()
                        self.matrix.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.str = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('OptionValue')
        if self.integer is not None:
            oprot.writeFieldBegin('integer', TType.I64, 1)
            oprot.writeI64(self.integer)
            oprot.writeFieldEnd()
        if self.number is not None:
            oprot.writeFieldBegin('number', TType.DOUBLE, 2)
            oprot.writeDouble(self.number)
            oprot.writeFieldEnd()
        if self.vector is not None:
            oprot.writeFieldBegin('vector', TType.LIST, 3)
            oprot.writeListBegin(TType.DOUBLE, len(self.vector))
            for iter18 in self.vector:
                oprot.writeDouble(iter18)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.matrix is not None:
            oprot.writeFieldBegin('matrix', TType.LIST, 4)
            oprot.writeListBegin(TType.LIST, len(self.matrix))
            for iter19 in self.matrix:
                oprot.writeListBegin(TType.DOUBLE, len(iter19))
                for iter20 in iter19:
                    oprot.writeDouble(iter20)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.str is not None:
            oprot.writeFieldBegin('str', TType.STRING, 5)
            oprot.writeString(self.str.encode('utf-8') if sys.version_info[0] == 2 else self.str)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SurrogateException(TException):
    """
    Attributes:
     - msg
    """


    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('SurrogateException')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class OptimizerException(TException):
    """
    Attributes:
     - msg
    """


    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('OptimizerException')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SurrogateQualification(object):
    """
    Attributes:
     - r2
     - yp
    """


    def __init__(self, r2=None, yp=None,):
        self.r2 = r2
        self.yp = yp

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.r2 = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.yp = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = iprot.readDouble()
                        self.yp.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('SurrogateQualification')
        if self.r2 is not None:
            oprot.writeFieldBegin('r2', TType.DOUBLE, 1)
            oprot.writeDouble(self.r2)
            oprot.writeFieldEnd()
        if self.yp is not None:
            oprot.writeFieldBegin('yp', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.yp))
            for iter27 in self.yp:
                oprot.writeDouble(iter27)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SobolIndices(object):
    """
    Attributes:
     - S1
     - ST
    """


    def __init__(self, S1=None, ST=None,):
        self.S1 = S1
        self.ST = ST

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.S1 = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = iprot.readDouble()
                        self.S1.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.ST = []
                    (_etype37, _size34) = iprot.readListBegin()
                    for _i38 in range(_size34):
                        _elem39 = iprot.readDouble()
                        self.ST.append(_elem39)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('SobolIndices')
        if self.S1 is not None:
            oprot.writeFieldBegin('S1', TType.LIST, 1)
            oprot.writeListBegin(TType.DOUBLE, len(self.S1))
            for iter40 in self.S1:
                oprot.writeDouble(iter40)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.ST is not None:
            oprot.writeFieldBegin('ST', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.ST))
            for iter41 in self.ST:
                oprot.writeDouble(iter41)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Distribution(object):
    """
    Attributes:
     - name
     - kwargs
    """


    def __init__(self, name=None, kwargs=None,):
        self.name = name
        self.kwargs = kwargs

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.kwargs = {}
                    (_ktype43, _vtype44, _size42) = iprot.readMapBegin()
                    for _i46 in range(_size42):
                        _key47 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val48 = iprot.readDouble()
                        self.kwargs[_key47] = _val48
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Distribution')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.kwargs is not None:
            oprot.writeFieldBegin('kwargs', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.DOUBLE, len(self.kwargs))
            for kiter49, viter50 in self.kwargs.items():
                oprot.writeString(kiter49.encode('utf-8') if sys.version_info[0] == 2 else kiter49)
                oprot.writeDouble(viter50)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class OptimizerResult(object):
    """
    Attributes:
     - status
     - x_suggested
    """


    def __init__(self, status=None, x_suggested=None,):
        self.status = status
        self.x_suggested = x_suggested

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.status = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.x_suggested = []
                    (_etype54, _size51) = iprot.readListBegin()
                    for _i55 in range(_size51):
                        _elem56 = iprot.readDouble()
                        self.x_suggested.append(_elem56)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('OptimizerResult')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I64, 1)
            oprot.writeI64(self.status)
            oprot.writeFieldEnd()
        if self.x_suggested is not None:
            oprot.writeFieldBegin('x_suggested', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.x_suggested))
            for iter57 in self.x_suggested:
                oprot.writeDouble(iter57)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ConstraintSpec(object):
    """
    Attributes:
     - type
     - bound
    """


    def __init__(self, type=None, bound=None,):
        self.type = type
        self.bound = bound

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.bound = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ConstraintSpec')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.bound is not None:
            oprot.writeFieldBegin('bound', TType.DOUBLE, 2)
            oprot.writeDouble(self.bound)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(OptionValue)
OptionValue.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'integer', None, None, ),  # 1
    (2, TType.DOUBLE, 'number', None, None, ),  # 2
    (3, TType.LIST, 'vector', (TType.DOUBLE, None, False), None, ),  # 3
    (4, TType.LIST, 'matrix', (TType.LIST, (TType.DOUBLE, None, False), False), None, ),  # 4
    (5, TType.STRING, 'str', 'UTF8', None, ),  # 5
)
all_structs.append(SurrogateException)
SurrogateException.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
)
all_structs.append(OptimizerException)
OptimizerException.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
)
all_structs.append(SurrogateQualification)
SurrogateQualification.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'r2', None, None, ),  # 1
    (2, TType.LIST, 'yp', (TType.DOUBLE, None, False), None, ),  # 2
)
all_structs.append(SobolIndices)
SobolIndices.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'S1', (TType.DOUBLE, None, False), None, ),  # 1
    (2, TType.LIST, 'ST', (TType.DOUBLE, None, False), None, ),  # 2
)
all_structs.append(Distribution)
Distribution.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.MAP, 'kwargs', (TType.STRING, 'UTF8', TType.DOUBLE, None, False), None, ),  # 2
)
all_structs.append(OptimizerResult)
OptimizerResult.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'status', None, None, ),  # 1
    (2, TType.LIST, 'x_suggested', (TType.DOUBLE, None, False), None, ),  # 2
)
all_structs.append(ConstraintSpec)
ConstraintSpec.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'type', None, None, ),  # 1
    (2, TType.DOUBLE, 'bound', None, None, ),  # 2
)
fix_spec(all_structs)
del all_structs
