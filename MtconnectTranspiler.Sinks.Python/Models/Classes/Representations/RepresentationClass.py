# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;specifies the format and structure of {{property(Observation::result)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;The {{block(Representation)}} type for an {{block(Observation)}} is defined by the associated {{property(DataItem::representation)}} in the {{term(MTConnectDevices Response Document)}}.

{{block(Value)}} is the default {{block(Representation)}} type for all {{block(Observation)}} types.

The name of the {{block(Observation)}} type is modified for all {{block(Representation)}} types other than {{block(Value)}} by appending the pascal case of the {{block(Representation)}} type. 

Example: The name for {{block(Sample)}} {{block(Observation)}} type `Temperature`with `Representation` type of `TimeSeries` becomes `TemperatureTimeSeries`.&#10;

"""


class RepresentationClass:

    pass

