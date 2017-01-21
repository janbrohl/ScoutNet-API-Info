.. sn_rpc:

Spezifisches zu SN-RPC
======================

hier gibt es noch nichts zu sehen aber möglicherweise hilft ein Blick auf https://github.com/scoutnet/plugins.sn_webservice/blob/master/class.tx_shscoutnetwebservice_sn.php

Alle Aufrufe gehen an die selbe URL:

.. http:post:: https://www.scoutnet.de/jsonrpc/server.php


Die Doku zu den Funktionen ist noch direkt kopiert vom Server-Code...

.. js:function:: get_data_by_global_id(globalId, [query])

	Return Data
	 
	:param array|string globalId:	Global id for which we want elements
	:param array query:		Query to filter the elements (dict: '<type>'=>array('key' = attribute to be filtered e.g. 'uid', 'afterDate', 'beforeDate'))
	 
	:returns: mixed Elements as object with structure : {'type':<type>,'content':<object>} where <object> could be {'eventName':<name>,'eventDate':<date>,...} where <object> could be {'eventName':<name>,'eventDate':<date>,...}

.. js:function:: checkPermission(type, globalid, username, auth)

	Checks if user has permission for object
	
	:param string type: 			is the type of the record
	:param integer globalid:		is the globalid of the object to check for
	:param string username:		username of the User
	:param string auth:			is an json containing the a timestamp and two hashes(sha1 and md5) of the three other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456
	 
	:return array: 0 if object is stored, 1 if user is not allow, 2 if an other error occured


.. js:function:: requestPermission(type, globalid, username, auth)
	
	Request permission for object
	
	:param string 	type:		Type of Record
	:param integer	globalid:	Globalid of Object to request for
	:param string	username:	Username
	:param string	auth:		is an array containing the a timestamp and two hashes(sha1 and md5) of the three other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456

	:return array: 0 if object is stored

.. js:function:: setData(type,id,object,username,auth
	
	Writes Data to scoutnet
	
	:param string  type:     this is the type of the record
	:param integer id:       the unique id of the object (if this is -1 the object is created)
	:param object  object:   the object itself
	:param string  username: the username of the user
	:param string  auth:     this is an array containing the a timestamp and two hashes(sha1 and md5) of the four other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456
	
	:return array: 0 if object is stored, 1 if user is not allow, 2 if an other error occured

.. js:function:: deleteObject(type,globalid,id,username,auth)
	
	Deletes object from scoutnet
	
	:param string  type:     this is the type of the record
	:param integer globalid: the globalid for the object
	:param integer id:       the unique id of the object
	:param string  username: the username of the user
	:param string  auth:     this is an array containing the a timestamp and two hashes(sha1 and md5) of the three other parameters which is encrypted with AES-CBC with the Users Api key and IV=1234567890123456
	
	:return array: 0 if object is stored, 1 if user is not allow, 2 if an other error occured
