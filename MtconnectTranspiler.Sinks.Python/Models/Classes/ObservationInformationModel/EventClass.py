# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Observation)}} that is a discrete piece of information from a piece of equipment.
&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;
It provides the information and data reported from a piece of equipment for those {{block(DataItem)}} entities defined with {{property(DataItem::category)}} as `EVENT` in the {{term(MTConnectDevices Response Document)}}.

{{figure(Event Example)}} shows {{block(Event)}} type examples. It also shows an example for when the {{property(Observation::result)}} is not available (`dataItemId`=`d1_asset_rem`).

![Event Example](figures/Event%20Example.png "Event Example"){: width="0.8"}

> Note: See {{lst(event-example)}} for the {{term(XML)}} representation of the same example.

The following {{sect(Value Properties of Event)}} lists the additional and/or updated attributes for {{block(Event)}}.&#10;

"""


class EventClass(ObservationGeneralization):


    def __init__(self):


        # TODO: Import ResetTriggeredEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifies when a reported value has been reset and what has caused that reset to occur for those {{block(DataItem)}} entities that may be periodically reset to an initial value.
        
        `resetTriggered` **MUST** only be provided for the specific occurrence of a {{block(DataItem)}} reported in the {{term(MTConnectStreams Response Document)}} when the reset occurred.&#10;

        """

        self.ResetTriggered = ""

        # TODO: Import ComponentStreamClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.OrganizedByComponentStream = ""

        # TODO: Import EventEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = ""



