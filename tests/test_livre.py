
import pytest

from bibliotheque.livre import Livre


def test_nouveau_livre_est_disponible():
    livre = Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus")
    assert livre.disponible is True


def test_emprunter_rend_indisponible():
    livre = Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus")
    livre.emprunter()
    assert livre.disponible is False


def test_emprunter_deux_fois_leve_une_erreur():
    livre = Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus")
    livre.emprunter()
    with pytest.raises(ValueError, match="déjà emprunté"):
        livre.emprunter()


def test_rendre_remet_disponible():
    livre = Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus")
    livre.emprunter()
    livre.rendre()
    assert livre.disponible

