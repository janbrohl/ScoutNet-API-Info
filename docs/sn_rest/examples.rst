.. _sn_rest_examples:

Beispiele
=============

Getestet mit :term:`Python` 3.5, benötigt :term:`requests`


Beispielbenutzung
------------------

Aufrufe der Funktionen von :ref:`sn_rest_py`

.. testsetup:: sn_rest

    from sn_rest import *

Events für Gruppe 4 abfragen:

.. testcode:: sn_rest

    sn_rest("group/4/events/")

Events für Gruppe 4 und 3 abfragen:

.. testcode:: sn_rest

    sn_rest("/events/","group_id=? or group_id=?",["4","3"])

Events für Gruppe 4 abfragen die vor dem 12.01.2012 liegen:

.. testcode:: sn_rest

    sn_rest("group/4/events/", "end_date < ?",["2012-01-12"])

Info über Gruppe 4 abfragen:

.. testcode:: sn_rest

    sn_rest("group/4/")

Übergeordnete Gruppe zu  Gruppe 4 suchen:

.. testcode:: sn_rest

    sn_rest("group/4/parent/")


Beispielclient
--------------

.. literalinclude:: ../../sn_rest.py
   :language: python
   :linenos:
   :caption: sn_rest.py
   :name: sn_rest_py

