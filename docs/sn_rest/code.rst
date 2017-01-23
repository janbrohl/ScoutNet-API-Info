.. _sn_rest_code:

Beispielecode
=============

Getestet mit :term:`Python` 3.5, benötigt :term:`requests`
 
   
Beispielbenutzung
------------------

Events für Gruppe 4 abfragen::

	sn_rest("group/4/events/")
	
Events für Gruppe 4 und 3 abfragen::

	sn_rest("/events/","group_id=? or group_id=?",["4","3"])
	
Events für Gruppe 4 abfragen die vor dem 12.01.2012 liegen::

	sn_rest("group/4/events/", "end_date < ?",["2012-01-12"])

Info über Gruppe 4 abfragen::

	sn_rest("group/4/")
	
Übergeordnete Gruppe zu  Gruppe 4 suchen::

	sn_rest("group/4/parent/")
	
	
Beispielclient
--------------
	
.. literalinclude:: ../../sn_rest.py
   :language: python
   :linenos:
   :caption: sn_rest.py
   :name: sn_rest_py