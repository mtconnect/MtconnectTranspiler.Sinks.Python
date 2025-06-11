class ResetTriggerEnum(MTCEnum):
	
		ActioNComplete = "   {{term(observation)}} of the {{block(DataItem)}} that is measuring an action or operation is to be reset upon completion of that action or operation.   "
		
		Annual = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset at the end of a 12-month period.   "
		
		Day = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset at the end of a 24-hour period.   "
		
		Life = "   {{term(observation)}} of the {{block(DataItem)}} is not reset and accumulates for the entire life of the piece of equipment.   "
		
		Maintenance = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset upon completion of a maintenance event.   "
		
		Month = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset at the end of a monthly period.   "
		
		PoweROn = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset when power was applied to the piece of equipment after a planned or unplanned interruption of power has occurred.   "
		
		Shift = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset at the end of a work shift.   "
		
		Week = "   {{term(observation)}} of the {{block(DataItem)}} is to be reset at the end of a 7-day period.   "
		