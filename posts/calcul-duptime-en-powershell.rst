.. title: Calcul d'uptime en powershell
.. slug: calcul-duptime-en-powershell
.. date: 2014/02/04 21:27:30
.. tags: powershell, wmi
.. link: 
.. description: 
.. type: text
.. tribe: powershell


.. class:: alert alert-info

*Ah, mais j'l'ai rebooté ou pas ?*... question piège en prod... Solution, trouver l'uptime ...


* Et encore une fois *powershell* encapsule du *wmi* ...

.. TEASER_END

Code
----

.. code:: powershell

	$serveur ="localhost" #ou cible
	$lastboot = (Get-WmiObject -Class Win32_OperatingSystem -computername $serveur).LastBootUpTime
	$uptime = (Get-Date) – [System.Management.ManagementDateTimeconverter]::ToDateTime($lastboot)
	Write-Host "$serveur allumé depuis : " $uptime.days "jours" $uptime.hours "heures" $uptime.minutes "minutes" $uptime.seconds "secondes" 




* Commande bash :

.. code:: bash

	uptime
	 21:41:40 up  8:32,  4 users,  load average: 0,05, 0,13, 0,16

*je pouvais pas résister...*
