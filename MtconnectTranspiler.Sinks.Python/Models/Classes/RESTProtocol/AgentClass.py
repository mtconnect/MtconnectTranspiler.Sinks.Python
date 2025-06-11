# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{term(agent)}}.

An {{term(agent)}} **MUST** perform the following tasks:

* Collect data from manufacturing equipment.
* Generate {{termplural(response document)}}.
* Provide a REST interface using {{term(HTTP)}}.

In addition to {{term(XML)}} and {{term(HTTP)}}, An {{term(agent)}} **MAY** provide additional protocols and representations. Some representations **MAY** have companion specifications.&#10;

"""


class AgentClass:


    def __init__(self):


        # TODO: Import UInt32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier for an {{term(instance)}} of the {{term(agent)}}.
             
        {{property(Header::instanceId)}} **MUST** be changed to a different unique number each time the {{term(buffer)}} is cleared and a new set of data begins to be collected.&#10;

        """

        self.InstanceId = ""

        # TODO: Import UInt64 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(sequence number)}}.&#10;

        """

        self.SequenceNumber = ""

        # TODO: Import UInt32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;maximum number of {{termplural(Observation)}} that **MAY** be retained in the {{term(agent)}} that published the {{term(response document)}} at any point in time.&#10;

        """

        self.BufferSize = ""

        # TODO: Import UInt32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;maximum number of {{termplural(Asset)}} that **MAY** be retained in the {{term(agent)}} that published the {{term(response document)}} at any point in time.&#10;

        """

        self.MaxAssets = ""

        # TODO: Import UInt32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;current number of {{termplural(Asset)}} that are currently stored in the {{term(agent)}} as of the {{property(Header::creationTime)}} that the {{term(agent)}} published the {{term(response document)}}.&#10;

        """

        self.AssetCount = ""

        # TODO: Import ObservationGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasObservation = ""

        # TODO: Import AssetClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasAsset = ""



