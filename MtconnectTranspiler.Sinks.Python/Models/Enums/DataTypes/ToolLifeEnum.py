class ToolLifeEnum(MTCEnum):
	
		Minutes = "   tool life measured in minutes.   All units for minimum, maximum, and nominal **MUST** be provided in minutes.   "
		
		ParTCount = "   tool life measured in parts.   All units for minimum, maximum, and nominal **MUST** be provided as the number of parts.   "
		
		Wear = "   tool life measured in tool wear.   Wear **MUST** be provided in millimeters as an offset to nominal. All units for minimum, maximum, and nominal **MUST** be given as millimeter offsets as well. The standard will only consider dimensional wear at this time.   "
		