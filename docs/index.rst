Info zu den ScoutNet.de APIs
============================================

Es gib im Grunde genommen 2 APIs:

* den Webservice der laut Doku_ ":term:`RPC` im :term:`REST`-Stil mit :term:`JSON` als Datenaustauschformat implementiert" - im weiteren Text **SN-REST** genannt
* den anderen Webservice den man per :term:`JSON-RPC` (1.0) über HTTP(S) POST ansprechen kann - im weiteren Text **SN-RPC** genannt


Objekte in den Antworten der APIs enthalten Typhinweise: Bei SN-REST unter dem Namen ``"kind"`` bei SN-RPC unter ``"type"``.



Codebeispiele
---------------

Getestet mit :term:`Python` 3.5 und :term:`requests` 2.12. 

.. literalinclude:: ../sn_clients.py
   :language: python
   :linenos:
   



+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------+
| Ich will                           | SN-REST                                                       | SN-RPC                                                |
+====================================+===============================================================+=======================================================+
| Events für Gruppe 4 abfragen       | ``sn_rest("group/4/events/")``                                | ``sn_rpc_get("4",{"events":{}})``                     |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------+
| Events für Gruppe 4 und 3          | ``sn_rest("/events/","group_id=? or group_id=?",["4","3"])``  | ``sn_rpc_get(["4","3"],{"events":{}})``               |
| abfragen                           |                                                               |                                                       |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------+
| Events für Gruppe 4 abfragen       | ``sn_rest("group/4/events/", "end_date < ?",["2012-01-12"])`` | ``sn_rpc_get("4",{"events":{"before":"12.01.2012"})`` |
| die vor dem 12.01.2012 liegen      |                                                               |                                                       |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------+
| Info über Gruppe 4 abfragen        | ``sn_rest("group/4/")``                                       | ``sn_rpc_get("4",{"index":{}})``                      |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------+
| Übergeordnete Gruppe zu  Gruppe 4  | ``sn_rest("group/4/parent/")``                                | ``sn_rpc_get("4",{"index":{}})``                      |
| suchen                             |                                                               |                                                       |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------+


.. toctree::
   :caption: Inhalt
   :maxdepth: 3
   
   
   sn_rpc/index
   sn_rest/index
   glossary

.. _Doku: https://www.scoutnet.de/api-info/webservice.html


