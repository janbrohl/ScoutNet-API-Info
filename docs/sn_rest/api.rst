.. _sn_rest_api:

API
=========


Gruppen
--------

.. http:get:: https://www.scoutnet.de/api/0.2/group/

    Eine Gruppe (:ref:`sn_rest_group`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage


.. http:get:: https://www.scoutnet.de/api/0.2/groups/

    Eine Sammlung (:ref:`sn_rest_collection`) von Gruppen (:ref:`sn_rest_group`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage


.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/

    Eine Gruppe (:ref:`sn_rest_group`) abrufen.

    :param group_id: ID der Gruppe


.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/events/

    Sammlung (:ref:`sn_rest_collection`) von Events (:ref:`sn_rest_event`) zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/children/

    Sammlung (:ref:`sn_rest_collection`) von untergeordneten Gruppen (:ref:`sn_rest_group`) zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/parent/

    Direkt übergeordnete Gruppe (:ref:`sn_rest_group`) zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/parent/(layer)/

    Übergeordnete Gruppe (:ref:`sn_rest_group`) zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe
    :param layer: Ebene der übergeordneten Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/parents/

    Sammlung (:ref:`sn_rest_collection`) übergeordneter Gruppen (:ref:`sn_rest_group`) zu einer Gruppe abrufen.

    .. todo:: was bedeutet der options-parameter?

    :param group_id: ID der Gruppe



.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/urls/

    Sammlung (:ref:`sn_rest_collection`) von URLs (:ref:`sn_rest_url`) zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/sections/

    Sammlung (:ref:`sn_rest_collection`) von Stufen (:ref:`sn_rest_section`) zu einer Gruppe abrufen.

    :param group_id: ID der Gruppe


Events
-------

.. http:get:: https://www.scoutnet.de/api/0.2/event/

    Event (:ref:`sn_rest_event`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage



.. http:get:: https://www.scoutnet.de/api/0.2/events/

    Eine Sammlung (:ref:`sn_rest_collection`) von Events (:ref:`sn_rest_event`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage

.. http:get:: https://www.scoutnet.de/api/0.2/event/(event_id)/

    Event (:ref:`sn_rest_event`) abrufen.

    :param event_id: ID des Events

.. http:get:: https://www.scoutnet.de/api/0.2/event/(event_id)/group/

    Gruppe (:ref:`sn_rest_group`) zu Event abrufen.

    :param event_id: ID des Events

URLs
-----

.. http:get:: https://www.scoutnet.de/api/0.2/url/

    URL (:ref:`sn_rest_url`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage



.. http:get:: https://www.scoutnet.de/api/0.2/urls/

    Eine Sammlung (:ref:`sn_rest_collection`) von URLs (:ref:`sn_rest_url`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage

.. http:get:: https://www.scoutnet.de/api/0.2/url/(url_id)/

    URL (:ref:`sn_rest_url`) abrufen.

    :param url_id: ID der URL


Stufen
-------

.. http:get:: https://www.scoutnet.de/api/0.2/section/

    Stufe (:ref:`sn_rest_section`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage


.. http:get:: https://www.scoutnet.de/api/0.2/sections/

    Eine Sammlung (:ref:`sn_rest_collection`) von Stufen (:ref:`sn_rest_section`) abrufen.

    :query JSON-Array json: :ref:`pfadiql`-Anfrage

.. http:get:: https://www.scoutnet.de/api/0.2/section/(section_id)/

    Stufe (:ref:`sn_rest_section`) abrufen.

    :param section_id: ID der Stufe

