class FilterEnum(MTCEnum):
	
		MinimuMDelta = "   new value **MUST NOT** be reported for a data item unless the measured value has changed from the last reported value by at least the delta given as the value of this element.  The value of {{block(Filter)}} **MUST** be an absolute value using the same units as the reported data.   "
		
		Period = "   data reported for a data item is provided on a periodic basis. The `PERIOD` for reporting data is defined in the value of the {{block(Filter)}}.  The value of {{block(Filter)}} **MUST** be an absolute value reported in seconds representing the time between reported samples of the value of the data item.   "
		