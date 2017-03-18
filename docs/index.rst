Info zu den ScoutNet.de APIs
============================================

Es gib im Grunde genommen 5 APIs:

* den Webservice der laut Doku_ ":term:`RPC` im :term:`REST`-Stil mit :term:`JSON` als Datenaustauschformat implementiert" - im weiteren Text :ref:`sn_rest` genannt
* den anderen Webservice den man per :term:`JSON-RPC` (1.0) über HTTP(S) POST ansprechen kann - im weiteren Text :ref:`sn_rpc` genannt
* den CalDAV-Webservice der Lese- und Schreib-Zugriff auf Kalender nach dem :term:`CalDAV`-Protokoll (mit Abweichungen) über HTTP(S) ermöglicht - im weitern Text :ref:`sn_caldav` genannt
* das Pfadi-Archiv-Template-System
* das Kalender-Template-System von show.php

.. toctree::
   :caption: Inhalt
   :maxdepth: 3

         
   sn_rpc/index
   sn_rest/index
   sn_caldav/index
   pfadi_archiv/index
   show_php/index
   glossary

.. _Doku: https://www.scoutnet.de/api-info/webservice.html


