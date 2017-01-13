Spezifisches zu SN-REST
========================

Noch gibt es hier nichts zu sehen aber es gibt schon eine Doku auf https://www.scoutnet.de/api-info/webservice.html


.. http:get:: https://www.scoutnet.de/api/0.2/group/
   
    Eine Gruppe abrufen.
	
	:query json: JSON-Kodierte PfadiQL-Anfrage
	
	
.. http:get:: https://www.scoutnet.de/api/0.2/groups/
   
    Eine Sammlung von Gruppen abrufen.
	
	:query json: JSON-Kodierte PfadiQL-Anfrage
	

.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/
   
    Eine Gruppe abrufen.
	   
    :arg group_id: ID der Gruppe
	   
			
.. http:get:: https://www.scoutnet.de/api/0.2/group/(group_id)/events/
   
    Events zu einer Gruppe abrufen.
   
    :arg group_id: ID der Gruppe
	
			
.. http:get:: https://www.scoutnet.de/api/0.2/event/
    
	Event abrufen.
	
	:query json: JSON-Kodierte PfadiQL-Anfrage
	


.. http:get:: https://www.scoutnet.de/api/0.2/events/
    
	Eine Sammlung von Events abrufen.
	
	:query json: JSON-Kodierte PfadiQL-Anfrage
		
.. http:get:: https://www.scoutnet.de/api/0.2/event/(event_id)/
   
    Event abrufen.
	   
    :arg event_id: ID des Events		
