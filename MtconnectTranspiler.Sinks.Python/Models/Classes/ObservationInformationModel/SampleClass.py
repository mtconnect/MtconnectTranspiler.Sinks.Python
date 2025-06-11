# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Observation)}} that is continuously changing or analog data value.
&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;
It provides the information and data reported from a piece of equipment for those {{block(DataItem)}} entities defined with {{property(DataItem::category)}} as `SAMPLE` in the {{term(MTConnectDevices Response Document)}}.

{{block(Sample)}} **MUST** always be reported in `float`.

{{figure(Sample Example)}} shows {{block(Sample)}} type examples. It also shows an example for when the {{property(Observation::result)}} is not available (`dataItemId`=`cspeed`).

![Sample Example](figures/Sample%20Example.png "Sample Example"){: width="0.8"}

> Note: See {{lst(sample-example)}} for the {{term(XML)}} representation of the same example.

The following {{sect(Value Properties of Sample)}} lists the additional and/or updated attributes for {{block(Sample)}}.&#10;

"""


class SampleClass(ObservationGeneralization):


    def __init__(self):


        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;time-period over which the data was collected.
        
        {{property(Sample::duration)}} **MUST** be provided when the {{property(DataItem::statistic)}} is defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Duration = ""

        # TODO: Import ResetTriggeredEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifies when a reported value has been reset and what has caused that reset to occur for those {{block(DataItem)}} entities that may be periodically reset to an initial value.
        
        `resetTriggered` **MUST** only be provided for the specific occurrence of a {{block(DataItem)}} reported in the {{term(MTConnectStreams Response Document)}} when the reset occurred.&#10;

        """

        self.ResetTriggered = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;rate at which successive samples of the value are recorded.
        &#10;
        &#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{property(Sample::sampleRate)}} is expressed in terms of samples per second.
        
        If {{property(Sample::sampleRate)}} is smaller than one, the number can be represented as a decimal type floating-point number. For example, a rate of 1 per 10 seconds would be 0.1 {{property(Sample::sampleRate)}} **MUST** be provided when {{property(DataItem::representation)}} defined in the {{term(MTConnectDevices Response Document)}} is `TIME_SERIES`.
        
        When {{property(DataItem::representation)}} is not `TIME_SERIES`, it **MUST** be assumed that the data reported is represented by a single value and {{property(Sample::sampleRate)}} **MUST NOT** be reported in the {{term(MTConnectStreams Response Document)}}.&#10;

        """

        self.SampleRate = ""

        # TODO: Import StatisticEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of statistical calculation defined by the {{property(DataItem::statistic)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Statistic = ""

        # TODO: Import ComponentStreamClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.OrganizedByComponentStream = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Units = ""

        # TODO: Import SampleEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = ""



