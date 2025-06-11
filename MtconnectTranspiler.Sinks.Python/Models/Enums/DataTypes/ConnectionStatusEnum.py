class ConnectionStatusEnum(MTCEnum):
	
		Closed = "   no connection at all.   "
		
		Listen = "   {{term(agent)}} is waiting for a connection request from an {{term(adapter)}}.   "
		
		Established = "   open connection.  The normal state for the data transfer phase of the connection.   "
		