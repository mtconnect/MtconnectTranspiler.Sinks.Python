class ProgramEditEnum(MTCEnum):
	
		Active = "   {{block(Controller)}} is in the program edit mode.   "
		
		Ready = "   {{block(Controller)}} is capable of entering the program edit mode and no function is inhibiting a change to that mode.   "
		
		NoTReady = "   {{block(Controller)}} is being inhibited by a function from entering the program edit mode.   "
		