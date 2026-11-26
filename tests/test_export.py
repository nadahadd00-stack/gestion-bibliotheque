import csv
from unittest.mock import Mock
from bibliotheque.export import exporter_csv


def test_exporter_csv(biblio, tmp_path):
    fichier = tmp_path / "export.csv"
    exporter_csv(biblio, fichier)

    with open(fichier, newline="", encoding="utf-8") as f:
        lignes = list(csv.reader(f))

    assert lignes[0] == ["isbn", "titre", "auteur", "disponible"]
    assert len(lignes) == 4


def test_exporter_csv_avec_faux_catalogue(tmp_path):
    faux = Mock()
    faux.livres = []

    fichier = tmp_path / "vide.csv"
    exporter_csv(faux, fichier)

    assert fichier.read_text(encoding="utf-8").strip() == "isbn,titre,auteur,disponible"
