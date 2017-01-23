.. sn_rpc_api:

API
======================


Alle Aufrufe gehen per JSON-RPC (1.0) per HTTP-POST an die selbe URL:

.. http:post:: https://www.scoutnet.de/jsonrpc/server.php

Die Doku zu den Funktionen ist fast direkt kopiert aus dem Server-Code.

.. js:function:: get_data_by_global_id(global_id [, query])

    Return Data

    :param array|string global_id:    Global id for which we want elements
    :param object query:        :ref:`sn_rpc_query` to filter the elements
    :returns: Elemente als Attribute eines Objects - die Namen sind zusammengesetzt aus :ref:`sn_rpc_typen` und IDs

.. js:function:: checkPermission(type, global_id, username, auth)

    Checks if user has permission for object

    :param string type:             type of the record
    :param integer global_id:        global Id of the object to check for
    :param string username:        username of the User
    :param string auth:            JSON-serialized array containing the a timestamp and two hashes(sha1 and md5) of the three other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456

    :return: 0 if object is stored, 1 if user is not allow, 2 if an other error occured


.. js:function:: requestPermission(type, global_id, username, auth)

    Request permission for object

    :param string     type:        Type of Record
    :param integer    global_id:    Global id of Object to request for
    :param string    username:    Username
    :param string    auth:        JSON-serialized array containing the a timestamp and two hashes(sha1 and md5) of the three other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456

    :return: 0 if object is stored

.. js:function:: setData(type,id,object,username,auth

    Writes Data to scoutnet

    :param string  type:     this is the type of the record
    :param integer id:       the unique id of the object (if this is -1 the object is created)
    :param object  object:   the object itself
    :param string  username: the username of the user
    :param string  auth:     JSON-serialized array containing the a timestamp and two hashes(sha1 and md5) of the four other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456

    :return: 0 if object is stored, 1 if user is not allow, 2 if an other error occured

.. js:function:: deleteObject(type,global_id,id,username,auth)

    Deletes object from scoutnet

    :param string  type:     this is the type of the record
    :param integer global_id: the global id for the object
    :param integer id:       the unique id of the object
    :param string  username: the username of the user
    :param string  auth:     JSON-serialized array containing the a timestamp and two hashes(sha1 and md5) of the three other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456

    :return: 0 if object is stored, 1 if user is not allow, 2 if an other error occured




Die Erzeugung des Auth-Strings ist etwas kompliziert aber sie sollte funktionieren wie in :ref:`sn_rpc_py`

