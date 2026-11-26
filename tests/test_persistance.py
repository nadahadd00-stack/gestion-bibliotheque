import json
from unittest.mock import mock_open, patch
from bibliotheque.persistance import charger_json, sauvegarder_json


def test_aller_retour_json(biblio, tmp_path):
    fichier = tmp_path / "catalogue.json"

    biblio.rechercher_par_isbn("978-2-07-036822-8").emprunter()

    sauvegarder_json(biblio, fichier)

    relu = charger_json(fichier)

    assert len(relu) == 3
    assert relu.rechercher_par_isbn("978-2-07-036822-8").disponible is False
    assert relu.rechercher_par_isbn("978-2-07-036002-4").disponible is True


def test_contenu_json(biblio, tmp_path):
    fichier = tmp_path / "c.json"

    sauvegarder_json(biblio, fichier)

    donnees = json.loads(fichier.read_text(encoding="utf-8"))

    assert donnees[0]["titre"] == "Le Petit Prince"
    assert "Saint-Exupéry" in fichier.read_text(encoding="utf-8")

def test_charger_avec_open_simule():
    contenu = '[{"isbn": "1", "titre": "T", "auteur": "A", "disponible": false}]'

    with patch("builtins.open", mock_open(read_data=contenu)) as faux_open:
        biblio = charger_json("fichier_qui_n_existe_pas.json")

    faux_open.assert_called_once_with(
        "fichier_qui_n_existe_pas.json",
        encoding="utf-8"
    )

    assert len(biblio) == 1
    assert biblio.rechercher_par_isbn("1").disponible is False

