class ProcessStateEnum(MTCEnum):
	
		Initializing = "   device is preparing to execute the process occurrence.   "
		
		Ready = "   process occurrence is ready to be executed.   "
		
		Active = "   process occurrence is actively executing.   "
		
		Complete = "   process occurrence is now finished.   "
		
		Interrupted = "   process occurrence has been stopped and may be resumed.   "
		
		Aborted = "   process occurrence has come to a premature end and cannot be resumed.   "
		