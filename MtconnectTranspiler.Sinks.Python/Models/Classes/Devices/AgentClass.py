# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Device)}} composed of an {{term(MTConnect Agent)}} and all its connected data sources.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;An {{block(Agent)}} **MUST** be provided by all {{term(MTConnect Agent)}} implementations.

An {{block(Agent)}} **MUST** provide notifications when devices are added or changed.

An {{block(Agent)}} **MUST** provide connection information for each data source currently supplying data to the {{term(MTConnect Agent)}}.

An {{block(Agent)}} **MAY** provide information about telemetry relating to data sources.

An {{block(Agent)}} **MAY** provide information about the {{term(MTConnect Agent)}} resource utilization.
&#10;

"""


class AgentClass(DeviceClass):

    pass

