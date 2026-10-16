# Comment se servir du script en 5 étapes (trop facile)
1) Télécharger la PQ "My finds" et la renommer en `My_finds.gpx`
2) Télécharger le script python `AroundTheWorld.py` et le placer dans le même dossier que `My_finds.gpx`
3) Dans un terminal de commande (Powershell sous Windows) : se déplacer dans le dossier où se trouvent `My_finds.gpx` et `AroundTheWorld.py` à l'aide de la commande `cd '<nom complet du dossier>'` (exemple : `cd 'C:\Users\simon\Documents\Geocaching\Challenges Golgaff'`)
4) Encore dans le terminal de commande, installer le module python "Haversine" avec la commande `pip install haversine`
5) Toujours dans le terminal, exécuter le script avec la commande `python AroundTheWorld.py`. Dans le terminal s'affiche alors le code GC de la cache vous ayant permis de valider le challenge de Golgaff GCA11BT.

Le module "Haversine" installé à l'étape 4 est utilisé pour calculer la distance entre chaque cache avec la même méthode que dans le checker de Project-GC.

Si un problème survient aux étapes 4 ou 5, essayez d'installer Python (https://www.python.org/downloads/).
Le script me donne un résultat cohérent, mais je ne garantis pas qu'il vous donne toute la vérité, rien que la vérité. N'hésitez pas à me contacter via la messagerie Geocaching (mon compte : Bonnie_ft_Clyde) en cas de problème.
