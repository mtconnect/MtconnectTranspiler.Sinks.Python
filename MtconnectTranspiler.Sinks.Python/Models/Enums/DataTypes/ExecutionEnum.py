class ExecutionEnum(MTCEnum):
	
		Ready = "   {{block(Component)}} is ready to execute instructions.  It is currently idle.   "
		
		Active = "   {{block(Component)}} is actively executing an instruction.   "
		
		Interrupted = "   {{block(Component)}} suspends the execution of the program due to an external signal.  Action is required to resume execution.   "
		
		FeeDHold = "   motion of the active axes are commanded to stop at their current position.   "
		
		Stopped = "   {{block(Component)}} program is not `READY` to execute.   "
		
		OptionaLStop = "   command from the program has intentionally interrupted execution.  The {{block(Component)}} **MAY** have another state that indicates if the execution is interrupted or the execution ignores the interrupt instruction.   "
		
		PrograMStopped = "   command from the program has intentionally interrupted execution.  Action is required to resume execution.   "
		
		PrograMCompleted = "   program completed execution.   "
		
		Wait = "   {{block(Component)}} suspends execution while a secondary operation executes.  Execution resumes automatically once the secondary operation completes.   "
		
		PrograMOptionaLStop = "   program has been intentionally optionally stopped using an M01 or similar code.  **DEPRECATED** in *version 1.4* and replaced with `OPTIONAL_STOP`.   "
		