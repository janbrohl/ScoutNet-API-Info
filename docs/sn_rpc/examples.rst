.. _sn_rpc_examples:

Beispiele
=============

Teilweise getestet mit :term:`Python` 3.5, benötigt :term:`Bibliothek requests` und :term:`Bibliothek pycrypto`


Beispielbenutzung
------------------

Aufrufe der Funktionen von :ref:`sn_rpc_py`

.. testsetup:: sn_rpc

    from sn_rpc import *

Events für Gruppe 4 abfragen:

.. testcode:: sn_rpc

    get_data_by_global_id("4",{"events":{}})

Events für Gruppe 4 und 3 abfragen:

.. testcode:: sn_rpc

    get_data_by_global_id(["4","3"],{"events":{}})

Events für Gruppe 4 abfragen die vor dem 12.01.2012 liegen:

.. testcode:: sn_rpc

    get_data_by_global_id("4",{"events":{"before":"12.01.2012"}})

Info über Gruppe 4 abfragen:

.. testcode:: sn_rpc

    get_data_by_global_id("4",{"index":{}})

Übergeordnete Gruppe zu  Gruppe 4 suchen:

.. testcode:: sn_rpc

    get_data_by_global_id("4",{"index":{}})

Beispielclient
--------------

.. literalinclude:: ../../sn_rpc.py
   :language: python
   :linenos:
   :caption: sn_rpc.py
   :name: sn_rpc_py

