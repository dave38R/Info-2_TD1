import model


def test_lit_etat():
    assert model.lit_etat('Tac') == 'affamé'


def test_lit_etat_nul():
    assert model.lit_etat('Bob') == None


def test_lit_lieu():
    assert model.lit_lieu('Tac') == 'litière'


def test_lit_lieu_nul():
    assert model.lit_lieu('Bob') == None


def test_verifie_disponibilite():
    assert model.verifie_disponibilite('litière') == 'libre'
    assert model.verifie_disponibilite('nid') == 'occupé'


def test_verifie_disponibilite_nul():
    assert model.verifie_disponibilite('nintendo') == None


def test_cherche_occupant():
    assert model.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in model.cherche_occupant('litière')
    assert 'Tac' not in model.cherche_occupant('mangeoire')


def test_cherche_occupant_nul():
    assert model.cherche_occupant('casino') is None


def test_change_état():
    model.change_etat('Totoro', 'fatigué')
    assert model.lit_etat('Totoro') == 'fatigué'
    model.change_etat('Totoro', 'excité comme un pou')
    assert model.lit_etat('Totoro') == 'fatigué'
    model.change_etat('Bob', 'fatigué')
    assert model.lit_etat('Bob') is None


def test_change_lieu():
    model.change_lieu('Totoro', 'roue')
    assert model.lit_lieu('Totoro') == 'roue'
    assert model.verifie_disponibilite('litière') == 'libre'
    assert model.verifie_disponibilite('roue') == 'occupé'


def test_change_lieu_occupé():
    model.change_lieu('Totoro', 'nid')
    assert model.lit_lieu('Totoro') == 'roue'


def test_change_lieu_nul_1():
    model.change_lieu('Totoro', 'casino')
    assert model.lit_lieu('Totoro') == 'roue'


def test_change_lieu_nul_2():
    model.change_lieu('Bob', 'litière')
    assert model.lit_lieu('Bob') == None


import controler


def test_nourrir():
    if model.verifie_disponibilite('mangeoire') == 'libre' and model.lit_etat('Tic') == 'affamé':
        controler.nourrir('Tic')
    assert model.verifie_disponibilite('mangeoire') == 'occupé'
    assert model.lit_etat('Tic') == 'repus'
    assert model.lit_lieu('Tic') == 'mangeoire'
    controler.nourrir('Tac')
    assert model.lit_etat('Tac') == 'affamé'
    assert model.lit_lieu('Tac') == 'litière'
    controler.nourrir('Pocahontas')
    assert model.lit_etat('Pocahontas') == 'endormi'
    assert model.lit_lieu('Pocahontas') == 'nid'
    controler.nourrir('Bob')
    assert model.lit_etat('Bob') is None
    assert model.lit_lieu('Bob') is None
    assert model.verifie_disponibilite('mangeoire') == 'occupé'


def test_reveiller():
    if model.lit_etat('Pocahontas') and model.verifie_disponibilite('litière') == 'libre':
        controler.reveiller('Pocahontas')
    assert model.lit_etat('Pocahontas') == 'affamé'
    assert model.lit_lieu('Pocahontas') == 'litière'
    assert model.verifie_disponibilite('nid') == 'libre'
    assert model.verifie_disponibilite('litière') == 'libre'
    controler.reveiller('Bob')
    assert model.lit_lieu('Bob') is None
    assert model.lit_etat('Bob') is None
    assert model.verifie_disponibilite('litière') == 'libre'


def test_coucher():
    if model.lit_etat('Totoro') and model.verifie_disponibilite('nid') == 'libre':
        controler.coucher('Totoro')
    assert model.lit_etat('Totoro') == 'endormi'
    assert model.lit_lieu('Totoro') == 'nid'
    assert model.verifie_disponibilite('nid') == 'occupé'
    controler.coucher('Bob')
    assert model.lit_lieu('Bob') is None
    assert model.lit_etat('Bob') is None
    assert model.verifie_disponibilite('nid') == 'occupé'


def test_divertir():
    if model.lit_etat('Tic') == 'repus' and model.verifie_disponibilite('roue') == 'libre':
        controler.divertir('Tic')
    assert model.lit_etat('Tic') == 'fatigué'
    assert model.lit_lieu('Tic') == 'roue'
    assert model.verifie_disponibilite('roue') == 'occupé'
    controler.divertir('Bob')
    assert model.lit_lieu('Bob') is None
    assert model.lit_etat('Bob') is None
    assert model.verifie_disponibilite('roue') == 'occupé'
