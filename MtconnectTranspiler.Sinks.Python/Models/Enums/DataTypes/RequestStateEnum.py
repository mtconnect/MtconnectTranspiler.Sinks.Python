class RequestStateEnum(MTCEnum):
	
		NoTReady = "   {{term(requester)}} is not ready to make a {{term(request)}}.   "
		
		Ready = "   {{term(requester)}} is prepared to make a {{term(request)}}, but no {{term(request)}} for service is required.   "
		
		Active = "   {{term(requester)}} has initiated a {{term(request)}} for a service and the service has not yet been completed by the {{term(responder)}}.   "
		
		Fail = "   {{term(requester)}} has detected a failure condition.   "
		