class RepresentationEnum(MTCEnum):
	
		TimESeries = "   series of sampled data.  The data is reported for a specified number of samples and each sample is reported with a fixed period.   "
		
		Value = "   measured value of the sample data.  If no {{property(DataItem::representation)}} is specified for a data item, the {{property(DataItem::representation)}} **MUST** be determined to be `VALUE`.   "
		
		DatASet = "   reported value(s) are represented as a set of {{termplural(key-value pair)}}.  Each reported value in the {{term(data set)}} **MUST** have a unique key.   "
		
		Discrete = "   **DEPRECATED** as {{property(DataItem::representation)}} type in *MTConnect Version 1.5*. Replaced by the {{property(DataItem::discrete)}}.   "
		
		Table = "   two dimensional set of {{termplural(key-value pair)}} where the {{block(Entry)}} represents a row, and the value is a set of {{term(key-value pair)}} {{block(Cell)}} elements.   A {{term(table)}} follows the same behavior as the {{term(data set)}} for change tracking, clearing, and history. When an {{block(Entry)}} changes, all {{block(Cell)}} elements update as a single unit following the behavior of a {{term(data set)}}.  > Note: It is best to use {{block(Variable)}} if the {{block(Cell)}} entities represent multiple semantic types.  Each {{block(Entry)}} in the {{term(table)}} **MUST** have a unique key. Each {{block(Cell)}} of each {{block(Entry)}} in the {{term(table)}} **MUST** have a unique key.  See {{block(Representation)}} in {{package(Observation Information Model)}}, for a description of {{block(Entry)}} and {{block(Cell)}} elements.   "
		