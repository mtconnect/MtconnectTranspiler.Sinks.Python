# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Representation)}} for an {{block(Observation)}} composed of a series of sampled data.
&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;
{{block(TimeSeries)}} for an {{block(Observation)}} is defined by the associated {{property(DataItem::representation)}} as `TIME_SERIES`.

{{property(DataItem::representation)}} as `TIME_SERIES` **MUST** have {{property(DataItem::category)}} of `SAMPLE`.

{{figure(TemperatureTimeSeries)}} shows the model for {{block(Temperature)}} ({{block(Sample)}} type) with a {{block(Representation)}} type of {{block(TimeSeries)}}. 

![TemperatureTimeSeries](figures/TemperatureTimeSeries.png "TemperatureTimeSeries"){: width="0.8"}

> Note: See {{sect(Representation Schema Diagrams)}} for XML schema.

{{block(TimeSeries)}} **MUST** report multiple values at fixed intervals in a single {{block(Observation)}}. At minimum, one of {{property(DataItem::sampleRate)}} or {{property(Sample::sampleRate)}} **MUST** be specified. When both are specified, the {{property(Sample::sampleRate)}} supersedes the {{property(DataItem::sampleRate)}}.

{{property(Observation::timestamp)}} **MUST** be set to the time the last value was observed. The {{property(Sample::duration)}} **MAY** indicate the time interval from the first to the last value in the series.

{{sect(Value Properties of TimeSeries)}} defines additional attributes for an {{block(Observation)}} with {{block(TimeSeries)}} {{block(Representation)}} type.&#10;

"""


class TimeSeriesClass(RepresentationClass):


    def __init__(self):


        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number of values given for the {{block(Observation)}}.&#10;

        """

        self.SampleCount = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""



