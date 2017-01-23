.. _sn_rpc_code:

Beispielcode
=============
	
Teilweise getestet mit :term:`Python` 3.5, benötigt :term:`requests` und :term:`pycrypto`


Beispielbenutzung
------------------

Events für Gruppe 4 abfragen::

	get_data_by_global_id("4",{"events":{}})
	
Events für Gruppe 4 und 3 abfragen::

	get_data_by_global_id(["4","3"],{"events":{}})
	
Events für Gruppe 4 abfragen die vor dem 12.01.2012 liegen::

	get_data_by_global_id("4",{"events":{"before":"12.01.2012"})

Info über Gruppe 4 abfragen::

	get_data_by_global_id("4",{"index":{}})
	
Übergeordnete Gruppe zu  Gruppe 4 suchen::

	get_data_by_global_id("4",{"index":{}})
	
Beispielclient
--------------

.. literalinclude:: ../../sn_rpc.py
   :language: python
   :linenos:
   :caption: sn_rpc.py
   :name: sn_rpc_py
