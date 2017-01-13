Info zu den ScoutNet.de APIs
============================================

Es gib im Grunde genommen 2 APIs:

* den Webservice der laut Doku_ "RPC_ im REST_-Stil mit JSON_ als Datenaustauschformat implementiert" - im weiteren Text **SN-REST** genannt
* den anderen Webservice den man per JSON-RPC_ (1.0) über HTTP(S) POST ansprechen kann - im weiteren Text **SN-RPC** genannt


Objekte in den Antworten der APIs enthalten Typhinweise: Bei SN-REST unter dem Namen ``"kind"`` bei SN-RPC unter ``"type"``.



Codebeispiele
---------------

Getestet mit Python_ 3.5 und requests_ 2.12. 

.. include:: ../sn_clients.py
   :code: python



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

Inhalt
----------

.. toctree::
   :maxdepth: 2
   
   sn_rest
   sn_rpc

.. _RPC: https://en.wikipedia.org/wiki/Remote_procedure_call

.. _REST: https://en.wikipedia.org/wiki/Representational_state_transfer

.. _JSON: https://en.wikipedia.org/wiki/JSON

.. _JSON-RPC: https://en.wikipedia.org/wiki/JSON-RPC

.. _Doku: https://www.scoutnet.de/api-info/webservice.html

.. _requests: http://docs.python-requests.org/en/master/

.. _Python: https://www.python.org/


