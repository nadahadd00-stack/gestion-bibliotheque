import pytest


def test_nouveau_livre_est_disponible(livre):
    assert livre.disponible is True


def test_emprunter_rend_indisponible(livre):
    livre.emprunter()
    assert livre.disponible is False


def test_emprunter_deux_fois_leve_une_erreur(livre):
    livre.emprunter()
    with pytest.raises(ValueError, match="déjà emprunté"):
        livre.emprunter()


def test_rendre_remet_disponible(livre):
    livre.emprunter()
    livre.rendre()
    assert livre.disponible


def test_str_disponible(livre):
    assert str(livre) == "[+] L'Étranger par Albert Camus (ISBN 978-2-07-036002-4)"


def test_str_emprunte(livre):
    livre.emprunter()
    assert str(livre).startswith("[-] ")
