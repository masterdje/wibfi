.. title: Activer les archives mensuelles d'un site nikola multilangue
.. slug: activer-les-archives-mensuelles-dun-site-nikola-multilangue
.. date: 2014/02/01 14:42:42
.. tags: nikola, python, tips, vie-du-site
.. link: 
.. description: 
.. type: text
.. tribe: tips

.. class:: alert alert-info

Un pseudo-bug rencontré lors du passage en multilangue bloquait le build si on était en mode *archives mensuelles*

* encore un problème de *locale*

J'avais ce méchant message :
 
.. code:: python

	[2014-02-01T11:52:07Z] WARNING: Nikola: Could not guess locale for language en, using locale C
	Scanning posts....done!
	Traceback (most recent call last):
	File "/home/dje/.virtualenvs/env2/lib/python2.7/site-packages/doit/doit_cmd.py", line 105, in run
		return self.sub_cmds[command].parse_execute(args)
	...
	...
	File "/home/dje/.virtualenvs/env2/lib/python2.7/site-packages/nikola/plugins/task/archive.py", line 85, in gen_tasks
		context["items"] = [[nikola.utils.LocaleBorg().get_month_name(int(month), lang), month] for month in months]
	File "/home/dje/.virtualenvs/env2/lib/python2.7/site-packages/nikola/utils.py", line 752, in get_month_name
		s = s.decode(self.encodings[lang])
	TypeError: decode() argument 1 must be string, not None

* Y a un truc vide, et c'est la variable contenant les mois en anglais... 

.. TEASER_END

D'abord
-------

* Vérifier la cohérence des locales

.. code:: bash

	locale
	LANG=fr_FR.utf8
	LC_CTYPE="fr_FR.utf8"
	LC_NUMERIC="fr_FR.utf8"
	LC_TIME="fr_FR.utf8"
	LC_COLLATE="fr_FR.utf8"
	LC_MONETARY="fr_FR.utf8"
	LC_MESSAGES="fr_FR.utf8"
	LC_PAPER="fr_FR.utf8"
	LC_NAME="fr_FR.utf8"
	LC_ADDRESS="fr_FR.utf8"
	LC_TELEPHONE="fr_FR.utf8"
	LC_MEASUREMENT="fr_FR.utf8"
	LC_IDENTIFICATION="fr_FR.utf8"
	LC_ALL=

	locale -a
	C
	fr_FR.utf8
	POSIX

Contournement
-------------

* Rajouter la locale **en_US.utf8** : il suffit de la décommenter

.. code:: bash

	vi /etc/locale.gen
	
* Recompiler les locales

.. code:: bash
	
	sudo locale-gen

A noter
-------

* @kpolska verrait bien une correction plus propre ... 
