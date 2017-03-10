.. _sn_caldav_examples:

Beispiele
=============

Ausprobiert mit :term:`Python` 3.5, benötigt :term:`Bibliothek iCalendar` und :term:`Bibliothek caldav`

Funktioniert aber leider nur in sehr einfachen Fällen - Sonderzeichen im :term:`JSON`-String im Description-Feld machen Probleme. 
Über Korrekturvorschläge würde ich mich freuen. 

Demo für :ref:`sn_caldav_py`


.. literalinclude:: ../../sn_caldav.py
   :language: python
   :dedent: 4
   :linenos:
   :start-after: "__main__":


Beispielclient
--------------

.. literalinclude:: ../../sn_caldav.py
   :language: python
   :linenos:
   :caption: sn_caldav.py
   :name: sn_caldav_py
   :end-before: if __name__

