class ControllerModeEnum(MTCEnum):
	
		Automatic = "   {{block(Controller)}} is configured to automatically execute a program.   "
		
		Manual = "   {{block(Controller)}} is not executing an active program.   It is capable of receiving instructions from an external source – typically an operator. The {{block(Controller)}} executes operations based on the instructions received from the external source.   "
		
		ManuaLDatAInput = "   operator can enter a series of operations for the {{block(Controller)}} to perform.  The {{block(Controller)}} will execute this specific series of operations and then stop.   "
		
		SemIAutomatic = "   {{block(Controller)}} is operating in a mode that restricts the active program from processing its next process step without operator intervention.   "
		
		Edit = "   {{block(Controller)}} is currently functioning as a programming device and is not capable of executing an active program.   "
		
		FeeDHold = "   axes of the device are commanded to stop, but the spindle continues to function.   "
		