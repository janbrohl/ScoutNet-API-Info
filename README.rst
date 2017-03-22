Doku und Beispiele zu den ScoutNet APIs
========================================

.. image:: https://readthedocs.org/projects/scoutnet-apis/badge/?version=latest
    :target: http://scoutnet-apis.readthedocs.io/de/latest/?badge=latest
    :alt: Documentation Status

Die Version zum Ansehen liegt auf http://scoutnet-apis.readthedocs.io/

Selber bauen
-------------

Um die Doku zu selbst zu bauen solltest Du Python_ 3.5 installiert haben. (Spätere Versionen sollten, frühere könnten funktionieren)

Am besten solltest du mit venv_ arbeiten. Die benötigten Pakete kannst Du dann am besten mit ``pip install --upgrade -r docs-requirements.txt`` installieren.

Erstellen kannst du dann die Doku mit::

    cd docs
    make html
    
Sie liegt dann in ``docs/_build/html``

.. _Python: https://www.python.org/

.. _venv: https://docs.python.org/3/library/venv.html

