class AlarmCodeEnum(MTCEnum):
	
		Crash = "   spindle crashed.   "
		
		Jam = "   component jammed.   "
		
		Failure = "   component failed.   "
		
		Fault = "   fault occurred on the component.   "
		
		Stalled = "   component has stalled and cannot move.   "
		
		Overload = "   component is overloaded.   "
		
		Estop = "   ESTOP button was pressed.   "
		
		Material = "   problem with the material.   "
		
		Message = "   system message.   "
		
		Other = "   alarm is not in any of the above categories.   "
		