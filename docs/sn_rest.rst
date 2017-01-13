Spezifisches zu SN-REST
========================

Noch gibt es hier viel zu sehen aber es gibt schon eine Doku auf https://www.scoutnet.de/api-info/webservice.html


Gruppen
--------

.. http:get:: https://www.scoutnet.de/api/0.2/group/

    Eine Gruppe abrufen.

    :query JSON-Array json: PfadiQL-Anfrage


.. http:get:: https://www.scoutnet.de/api/0.2/groups/

    Eine Sammlung von Gruppen abrufen.

    :query JSON-Array json: PfadiQL-Anfrage


.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/

    Eine Gruppe abrufen.

    :param group_id: ID der Gruppe


.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/events/

    Events zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/children/

    Untergeordnete Gruppen zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/parent/

    Direkt übergeordnete Gruppe zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe
    
.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/parent/(layer)/

    Übergeordnete Gruppe zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe
    :param layer: Ebene der übergeordneten Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/parents/

    Sammlung übergeordneter Gruppen zu einer Gruppe abrufen.
    
    .. todo:: was bedeutet der options-parameter?

    :param group_id: ID der Gruppe
    
    

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/urls/

    Sammlung von URLs zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/urls/

    Sammlung von Stufen zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe


Events
-------

.. http:get:: https://www.scoutnet.de/api/0.2/event/

    Event abrufen.

    :query JSON-Array json: PfadiQL-Anfrage



.. http:get:: https://www.scoutnet.de/api/0.2/events/

    Eine Sammlung von Events abrufen.

    :query JSON-Array json: PfadiQL-Anfrage

.. http:get:: https://www.scoutnet.de/api/0.2/event/(event_id)/

    Event abrufen.

    :param event_id: ID des Events

.. http:get:: https://www.scoutnet.de/api/0.2/event/(event_id)/group/

    Gruppe zu Event abrufen.

    :param event_id: ID des Events

URLs
-----

.. http:get:: https://www.scoutnet.de/api/0.2/url/

    URL abrufen.

    :query JSON-Array json: PfadiQL-Anfrage



.. http:get:: https://www.scoutnet.de/api/0.2/urls/

    Eine Sammlung von URLs abrufen.

    :query JSON-Array json: PfadiQL-Anfrage

.. http:get:: https://www.scoutnet.de/api/0.2/url/(url_id)/

    URL abrufen.

    :param url_id: ID der URL


Stufen
-------

.. http:get:: https://www.scoutnet.de/api/0.2/section/

    Stufe abrufen.

    :query JSON-Array json: PfadiQL-Anfrage


.. http:get:: https://www.scoutnet.de/api/0.2/sections/

    Eine Sammlung von Stufen abrufen.

    :query JSON-Array json: PfadiQL-Anfrage

.. http:get:: https://www.scoutnet.de/api/0.2/section/(section_id)/

    Stufe abrufen.

    :param section_id: ID der Stufe