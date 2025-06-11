class DataItemRelationshipTypeEnum(MTCEnum):
	
		Attachment = "   reference to a {{block(DataItem)}} that associates the values with an external entity.    "
		
		CoordinatESystem = "   referenced {{block(DataItem)}} provides the `id` of the effective Coordinate System.    "
		
		Limit = "   referenced {{block(DataItem)}} provides process limits.    "
		
		Observation = "   referenced {{block(DataItem)}} provides the observed values.    "
		