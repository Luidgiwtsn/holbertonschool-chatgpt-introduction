#!/usr/bin/python3
"""
Ce script affiche tous les arguments passés en ligne de commande,
à l'exclusion du nom du script lui-même.
"""

import sys

# On parcourt tous les arguments sauf le premier (le nom du script)
for arg in sys.argv[1:]:
    print(arg)
