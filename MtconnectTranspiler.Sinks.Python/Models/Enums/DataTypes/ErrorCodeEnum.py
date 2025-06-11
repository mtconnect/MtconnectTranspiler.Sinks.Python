class ErrorCodeEnum(MTCEnum):
	
		AsseTNoTFound = "   {{term(request)}} for information specifies an {{block(Asset)}} that is not recognized by the {{term(agent)}}.   "
		
		InternaLError = "   {{term(agent)}} experienced an error while attempting to published the requested information.   "
		
		InvaliDRequest = "   {{term(request)}} contains information that was not recognized by the {{term(agent)}}.   "
		
		InvaliDUri = "   {{term(URI)}} provided was incorrect.   "
		
		InvaliDXpath = "   {{term(XPath)}} identified in the {{term(request)}} for information could not be parsed correctly by the {{term(agent)}}.  This could be caused by an invalid syntax or the {{term(XPath)}} did not match a valid identify for any information stored in the {{term(agent)}}.    "
		
		NODevice = "   identity of the {{block(Device)}} specified in the {{term(request)}} for information is not associated with the {{term(agent)}}.   "
		
		OuTOFRange = "   {{term(request)}} for information specifies {{term(streaming data)}} that includes sequence number(s) for pieces of data that are beyond the end of the {{term(buffer)}}.   "
		
		QuerYError = "   {{term(agent)}} was unable to interpret the query.  The query parameters do not contain valid values or include an invalid parameter.   "
		
		ToOMany = "   `count` parameter provided in the {{term(request)}} for information requires either of the following:  * {{term(streaming data)}} that includes more pieces of data than the {{term(agent)}} is capable of organizing in an {{term(MTConnectStreams Response Document)}}.   * {{block(Assets)}} that include more {{block(Asset)}} in an {{term(MTConnectAssets Response Document)}} than the {{term(agent)}} is capable of handling.    "
		
		Unauthorized = "   {{term(requester)}} does not have sufficient permissions to access the requested information.   "
		
		Unsupported = "   valid {{term(request)}} was provided, but the {{term(agent)}} does not support the feature or type of {{term(request)}}.   "
		