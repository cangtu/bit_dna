# -*- coding: utf-8 -*-
#
# Copyright @ CangTu.
#
# 16-8-23 4:10PM licangtu@gmail.com
#
# Distributed under terms of the MIT License
import struct


BASE2INT = {'A': 0b00, 'T': 0b01, 'C': 0b10, 'G': 0b11}
INT2BASE = {0b00: 'A', 0b01: 'T', 0b10: 'C', 0b11: 'G'}
DNA_FRAG_SIZE = 32
BYTE_SIZE = 8


class IntList(object):
    def __init__(self, *args):
        self._int_list = list(args)

    def append(self, _int):
        self._int_list.append(_int)

    def __iter__(self):
        return iter(self._int_list)

    def __getitem__(self, item):
        return self._int_list[item]

    def __len__(self):
        return len(self._int_list)

    def __repr__(self):
        return repr(self._int_list)

    def to_byte_stream(self):
        return struct.pack('q'*len(self._int_list), *self._int_list) if self._int_list else ''

    @classmethod
    def from_byte_stream(cls, byte_stream):
        return cls(*struct.unpack('q'*(len(byte_stream)/BYTE_SIZE), byte_stream))


def _seq_to_int(seq):
    """
    convert sequence whose length is less than or equal to 32, do not use it directly.
    :param seq: sequence
    :return: a int
    """
    return sum((BASE2INT[base] << 2*i) for i, base in enumerate(seq))


def dna_to_int_list(dna):
    """
    convert the whole sequence to an int list
    :param dna: the whole sequence
    :return: int list
    """
    int_list = IntList()
    length = len(dna)
    int_list.append(length)

    for start in xrange(0, length, DNA_FRAG_SIZE):
        end = min(length, start + DNA_FRAG_SIZE)
        int_list.append(_seq_to_int(dna[start: end]))
    return int_list


def _int_to_seq(_int, eff_bits):
    """
    convert int to sequence whose length is less than or equal to 32, don't use it directly.
    :param _int: the int number
    :param eff_bits: effective bits means how many bases this int contains
    :return: sequence
    """
    seq = []
    for i in xrange(eff_bits):
        (_int & (0b11 << (2*i))) >> i


def int_list_to_dna(int_list):
    pass
