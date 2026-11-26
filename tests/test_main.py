from bibliotheque.main import main


def test_main_affiche_le_catalogue(capsys):
    main()
    sortie = capsys.readouterr().out

    assert "=== Bibliothèque ===" in sortie
    assert "3 livres au catalogue" in sortie
    assert "[-] La Peste" in sortie