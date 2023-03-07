from lingua.spanish_translations import SpanishTranslation


def test_split_float():
    sp = SpanishTranslation()
    result = sp.split_float(3.14159)
    assert 3 == result[0]
    assert 1 == result[1]

    result = sp.split_float(99.99)
    assert 100 == result[0]
    assert 0 == result[1]

    result = sp.split_float(165.25678)
    assert 165 == result[0]
    assert 3 == result[1]

    result = sp.split_float(-1000.26)
    assert -1000 == result[0]
    assert 3 == result[1]

    result = sp.split_float(1000.26)
    assert 1000 == result[0]
    assert 3 == result[1]


def test_num_to_spanish_negative():
    sp = SpanishTranslation()
    assert sp.int_to_spanish(-2505) == "menos dos mil quinientos cinco"


def test_float_to_spanish():
    sp = SpanishTranslation()
    assert sp.float_to_spanish(3.1415) == "tres punto uno"
    assert sp.float_to_spanish(-235.0) == "menos doscientos treinta y cinco"
    assert sp.float_to_spanish(123456.0) == \
        "ciento veintitrés mil cuatrocientos cincuenta y seis"
    assert sp.float_to_spanish(-1000.26) == "menos mil punto tres"


def test_int_to_spanish():
    sp = SpanishTranslation()

    assert sp.int_to_spanish(0) == "cero"
    assert sp.int_to_spanish(1) == "uno"
    assert sp.int_to_spanish(2) == "dos"
    assert sp.int_to_spanish(3) == "tres"
    assert sp.int_to_spanish(4) == "cuatro"
    assert sp.int_to_spanish(5) == "cinco"
    assert sp.int_to_spanish(6) == "seis"
    assert sp.int_to_spanish(7) == "siete"
    assert sp.int_to_spanish(8) == "ocho"
    assert sp.int_to_spanish(9) == "nueve"
    assert sp.int_to_spanish(10) == "diez"
    assert sp.int_to_spanish(11) == "once"
    assert sp.int_to_spanish(12) == "doce"
    assert sp.int_to_spanish(13) == "trece"
    assert sp.int_to_spanish(14) == "catorce"
    assert sp.int_to_spanish(15) == "quince"
    assert sp.int_to_spanish(16) == "dieciséis"
    assert sp.int_to_spanish(17) == "diecisiete"
    assert sp.int_to_spanish(18) == "dieciocho"
    assert sp.int_to_spanish(19) == "diecinueve"
    assert sp.int_to_spanish(20) == "veinte"
    assert sp.int_to_spanish(21) == "veintiuno"
    assert sp.int_to_spanish(22) == "veintidós"
    assert sp.int_to_spanish(23) == "veintitrés"
    assert sp.int_to_spanish(24) == "veinticuatro"
    assert sp.int_to_spanish(25) == "veinticinco"
    assert sp.int_to_spanish(26) == "veintiséis"
    assert sp.int_to_spanish(27) == "veintisiete"
    assert sp.int_to_spanish(28) == "veintiocho"
    assert sp.int_to_spanish(29) == "veintinueve"
    assert sp.int_to_spanish(30) == "treinta"
    assert sp.int_to_spanish(31) == "treinta y uno"
    assert sp.int_to_spanish(32) == "treinta y dos"
    assert sp.int_to_spanish(33) == "treinta y tres"
    assert sp.int_to_spanish(34) == "treinta y cuatro"
    assert sp.int_to_spanish(35) == "treinta y cinco"
    assert sp.int_to_spanish(36) == "treinta y seis"
    assert sp.int_to_spanish(37) == "treinta y siete"
    assert sp.int_to_spanish(38) == "treinta y ocho"
    assert sp.int_to_spanish(39) == "treinta y nueve"
    assert sp.int_to_spanish(40) == "cuarenta"
    assert sp.int_to_spanish(44) == "cuarenta y cuatro"
    assert sp.int_to_spanish(50) == "cincuenta"
    assert sp.int_to_spanish(60) == "sesenta"
    assert sp.int_to_spanish(70) == "setenta"
    assert sp.int_to_spanish(77) == "setenta y siete"
    assert sp.int_to_spanish(80) == "ochenta"
    assert sp.int_to_spanish(90) == "noventa"
    assert sp.int_to_spanish(99) == "noventa y nueve"
    assert sp.int_to_spanish(100) == "cien"
    assert sp.int_to_spanish(165) == "ciento sesenta y cinco"
    assert sp.int_to_spanish(200) == "doscientos"
    assert sp.int_to_spanish(240) == "doscientos cuarenta"
    assert sp.int_to_spanish(266) == "doscientos sesenta y seis"
    assert sp.int_to_spanish(300) == "trescientos"
    assert sp.int_to_spanish(400) == "cuatrocientos"
    assert sp.int_to_spanish(500) == "quinientos"
    assert sp.int_to_spanish(600) == "seiscientos"
    assert sp.int_to_spanish(700) == "setecientos"
    assert sp.int_to_spanish(800) == "ochocientos"
    assert sp.int_to_spanish(900) == "novecientos"
    assert sp.int_to_spanish(999) == "novecientos noventa y nueve"
    assert sp.int_to_spanish(1000) == "mil"
    assert sp.int_to_spanish(1978) == "mil novecientos setenta y ocho"
    assert sp.int_to_spanish(2023) == "dos mil veintitrés"
    assert sp.int_to_spanish(10000) == "diez mil"
    assert sp.int_to_spanish(11111) == "once mil ciento once"
    assert sp.int_to_spanish(100000) == "cien mil"
    assert sp.int_to_spanish(999999) == \
        "novecientos noventa y nueve mil novecientos noventa y nueve"
    assert sp.int_to_spanish(1000000) == "un millón"
    assert sp.int_to_spanish(10000000) == "diez millones"
    assert sp.int_to_spanish(100000000) == "cien millones"
    assert sp.int_to_spanish(1000000000) == "mil millones"
    assert sp.int_to_spanish(10000000000) == "diez mil millones"
    assert sp.int_to_spanish(100000000000) == "cien mil millones"
    assert sp.int_to_spanish(1000000000000) == "un billón"
