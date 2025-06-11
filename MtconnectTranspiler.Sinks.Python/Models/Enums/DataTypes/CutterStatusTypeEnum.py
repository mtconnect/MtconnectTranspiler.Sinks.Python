class CutterStatusTypeEnum(MTCEnum):
	
		New = "   new tool that has not been used or first use.   Marks the start of the tool history.   "
		
		Available = "   tool is available for use.   If this is not present, the tool is currently not ready to be used.   "
		
		Unavailable = "   tool is unavailable for use in metal removal.    "
		
		Allocated = "   tool is has been committed to a piece of equipment for use and is not available for use in any other piece of equipment.   "
		
		Unallocated = "   tool has not been committed to a process and can be allocated.   "
		
		Measured = "   tool has been measured.    "
		
		Reconditioned = "   tool has been reconditioned.   "
		
		Used = "   tool is in process and has remaining tool life.   "
		
		Expired = "   tool has reached the end of its useful life.   "
		
		Broken = "   premature tool failure.   "
		
		NoTRegistered = "   tool cannot be used until it is entered into the system.   "
		
		Unknown = "   tool is an indeterminate state. This is the default value.   "
		