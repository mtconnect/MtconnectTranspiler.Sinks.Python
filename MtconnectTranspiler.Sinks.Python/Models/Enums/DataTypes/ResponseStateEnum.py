class ResponseStateEnum(MTCEnum):
	
		NoTReady = "   {{term(responder)}} is not ready to perform a service.   "
		
		Ready = "   {{term(responder)}} is prepared to react to a {{term(request)}}, but no {{term(request)}} for service has been detected.   "
		
		Active = "   {{term(responder)}} has detected and accepted a {{term(request)}} for a service and is in the process of performing the service, but the service has not yet been completed.   "
		
		Complete = "   {{term(responder)}} has completed the actions required to perform the service.   "
		
		Fail = "   {{term(responder)}} has detected a failure condition.   "
		