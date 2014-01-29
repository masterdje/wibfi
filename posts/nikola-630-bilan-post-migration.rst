.. title: Nikola 6.3.0 - bilan post migration
.. slug: nikola-630-bilan-post-migration
.. date: 2014/01/28 21:24:15
.. tags: nikola, vie-du-site, python
.. link: 
.. description: 
.. type: text
.. tribe: python

.. class:: alert alert-info

Un peu plus funky que d'habitude, l'update...

* tickets en cours chez github ...

.. TEASER_END

D'abord
-------

* Mise à jour via :
	
.. code:: bash
	
	# depuis un virtualenv python 2.7...
	sudo pip install nikola --upgrade

Ensuite
-------

* Sans rien toucher, le **nikola build** annonce :

::

[2014-01-26T15:39:19Z] WARNING: Nikola: In order to USE_BUNDLES, you must install the "webassets" Python package.
[2014-01-26T15:39:19Z] WARNING: Nikola: Setting USE_BUNDLES to False.

et plante.

* J'installe *webassets*

.. code:: bash
	
	# depuis un virtualenv python 2.7...
	sudo pip install webassets

* **nikola build** plante lors du scan des posts :

::

Scanning posts.COMPILERS in conf.py does not tell me how to handle '.en' extensions.

* Apres enquête, c'est un fichier qui provoque ce message.

.. code:: bash 
	
	#nom du fichier :
	informations-freebox-rassemblees-en-point-unique.txt
	
	#slug du fichier :
	.. slug: informations-freebox-rassemblees-en-point-unique

* `rapport de bug en cours @ github <https://github.com/getnikola/nikola/issues/1007>`_

* **MAJ** : les experts de nikola se sont penchés sur le cas, et recommendent un gros nettoyage:

.. code:: bash

	rm -rf __pycache__/
	rm -rf cache/
	rm -rf .doit.db
	nikola clean

* Et ça marche !!


Et aussi
--------

* Disparition du **custom.css** intégré/renommé en **all-nocdn.css** ?

	
	
