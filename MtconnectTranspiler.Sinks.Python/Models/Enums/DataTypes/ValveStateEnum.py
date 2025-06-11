class ValveStateEnum(MTCEnum):
	
		Open = "   {{block(ValveState)}} where flow is allowed and the aperture is static.  > Note: For a binary value, `OPEN` indicates the valve has the maximum possible aperture.   "
		
		Opening = "   valve is transitioning from a `CLOSED` state to an `OPEN` state.   "
		
		Closed = "   {{block(ValveState)}} where flow is not possible, the aperture is static, and the valve is completely shut.   "
		
		Closing = "   valve is transitioning from an `OPEN` state to a `CLOSED` state.   "
		