class CharacteristicStatusEnum(MTCEnum):
	
		Pass = "   measurement is within acceptable tolerances.   "
		
		Fail = "   measurement is not within acceptable tolerances.   "
		
		Rework = "   failed, but acceptable constraints achievable by utilizing additional manufacturing processes.   "
		
		SysteMError = "   measurement is indeterminate due to an equipment failure.   "
		
		Indeterminate = "   measurement cannot be determined.   "
		
		NoTAnalyzed = "   measurement cannot be evaluated.   "
		
		BasiCORTheoretiCExacTDimension = "   nominal provided without tolerance limits. {{cite(QIF 3:2018 5.10.2.6)}}   "
		
		Undefined = "   status of measurement cannot be determined.   "
		