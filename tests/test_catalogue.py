import pytest

def test_catalogue_vide():
    from bibliotheque.catalogue import Bibliotheque
    assert len(Bibliotheque()) == 0


def test_ajouter(biblio):
    assert len(biblio) == 3


def test_rechercher_par_isbn_trouve(biblio):
    assert biblio.rechercher_par_isbn("978-2-07-036822-8").titre == "La Peste"


def test_rechercher_par_isbn_inconnu(biblio):
    assert biblio.rechercher_par_isbn("000") is None


def test_nombre_disponibles(biblio):
    assert biblio.nombre_disponibles() == 3
    biblio.rechercher_par_isbn("978-2-07-036822-8").emprunter()
    assert biblio.nombre_disponibles() == 2


def test_trier_par_titre(biblio):
    titres = [l.titre for l in biblio.trier_par_titre()]
    assert titres == sorted(titres)


def test_trier_par_titre_inverse(biblio):
    titres = [l.titre for l in biblio.trier_par_titre(inverse=True)]
    assert titres == sorted(titres, reverse=True)


def test_supprimer_existant(biblio):
    assert biblio.supprimer("978-2-07-036822-8") is True
    assert len(biblio) == 2


def test_supprimer_inconnu(biblio):
    assert biblio.supprimer("000") is False
    assert len(biblio) == 3


def test_livres_retourne_une_copie(biblio):
    biblio.livres.clear()
    assert len(biblio) == 3


@pytest.mark.parametrize(
    "auteur, attendu",
    [
        ("Albert Camus", 2),
        ("albert camus", 2),
        ("ALBERT CAMUS", 2),
        ("Antoine de Saint-Exupéry", 1),
        ("Inconnu", 0),
    ],
)
def test_rechercher_par_auteur(biblio, auteur, attendu):
    assert len(biblio.rechercher_par_auteur(auteur)) == attendu


@pytest.mark.parametrize(
    "mot, attendu",
    [("peste", 1), ("PETIT", 1), ("le", 1), ("zzz", 0)],
)
def test_rechercher_par_titre(biblio, mot, attendu):
    assert len(biblio.rechercher_par_titre(mot)) == attendu

@pytest.mark.skip(reason="exemple de marqueur skip : fonctionnalité non prévue")
def test_exemple_skip():
    assert False


@pytest.mark.xfail(reason="exemple de xfail : la recherche ignore les accents (limite connue)")
def test_recherche_sans_accent(biblio):
    assert len(biblio.rechercher_par_titre("etranger")) == 1

def test_nombre_empruntes(biblio):
    assert biblio.nombre_empruntes() == 0

    biblio.rechercher_par_isbn("978-2-07-036822-8").emprunter()

    assert biblio.nombre_empruntes() == 1

def test_livres_disponibles(biblio):
    assert len(biblio.livres_disponibles()) == 3

    biblio.rechercher_par_isbn("978-2-07-036822-8").emprunter()

    livres = biblio.livres_disponibles()

    assert len(livres) == 2
    assert all(livre.disponible for livre in livres)

