class PartProcessingStateEnum(MTCEnum):
	
		NeedSProcessing = "   part occurrence is not actively being processed, but the processing has not ended.   Processing requirements exist that have not yet been fulfilled. This is the default entry state when the part occurrence is originally received. In some cases, the part occurrence may return to this state while it waits for additional processing to be performed.   "
		
		INProcess = "   part occurrence is actively being processed.   "
		
		ProcessinGEnded = "   part occurrence is no longer being processed.   A general state when the reason for termination is unknown.   "
		
		ProcessinGEndeDComplete = "   part occurrence has completed processing successfully.   "
		
		ProcessinGEndeDStopped = "   process has been stopped during the processing.   The part occurrence will require special treatment.   "
		
		ProcessinGEndeDAborted = "   processing of the part occurrence has come to a premature end.   "
		
		ProcessinGEndeDLost = "   terminal state when the part occurrence has been removed from the equipment by an external entity and it no longer exists at the equipment.   "
		
		ProcessinGEndeDSkipped = "   part occurrence has been skipped for processing on the piece of equipment.   "
		
		ProcessinGEndeDRejected = "   part occurrence has been processed completely. However, the processing may have a problem.   "
		
		WaitinGFoRTransit = "   part occurrence is waiting for transit.   "
		
		INTransit = "   part occurrence is being transported to its destination.   "
		
		TransiTComplete = "   part occurrence has been placed at its designated destination.   "
		