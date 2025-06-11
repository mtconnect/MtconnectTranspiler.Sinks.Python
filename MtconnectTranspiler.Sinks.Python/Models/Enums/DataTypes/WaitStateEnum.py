class WaitStateEnum(MTCEnum):
	
		PowerinGUp = "   execution is waiting while the equipment is powering up and is not currently available to begin producing parts or products.   "
		
		PowerinGDown = "   execution is waiting while the equipment is powering down but has not fully reached a stopped state.   "
		
		ParTLoad = "   execution is waiting while one or more discrete workpieces are being loaded.   "
		
		ParTUnload = "   execution is waiting while one or more discrete workpieces are being unloaded.   "
		
		TooLLoad = "   execution is waiting while a tool or tooling is being loaded.   "
		
		TooLUnload = "   execution is waiting while a tool or tooling is being unloaded.   "
		
		MateriaLLoad = "   execution is waiting while material is being loaded.   "
		
		MateriaLUnload = "   execution is waiting while material is being unloaded.   "
		
		SecondarYProcess = "   execution is waiting while another process is completed before the execution can resume.   "
		
		Pausing = "   execution is waiting while the equipment is pausing but the piece of equipment has not yet reached a fully paused state.   "
		
		Resuming = "   execution is waiting while the equipment is resuming the production cycle but has not yet resumed execution.   "
		