class SensorStateDetectEnum(MTCEnum):
	
		Detected = "   sensor is active and the threshold has been met.   "
		
		NoTDetected = "   sensor is active and ready but the threshold has not been met.   "
		
		Unknown = "   sensor is active, but the state cannot be determined.  > Note: unknown covers situations where the sensor reading is unstable.   "
		