# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;provides information from an {{term(agent)}} defining version information, storage capacity, and parameters associated with the data management within the {{term(agent)}}.&#10;

"""


class HeaderClass:


    def __init__(self):


        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;timestamp of the last update of the {{block(Device)}} information for any device.&#10;

        """

        self.DeviceModelChangeTime = ""

        # TODO: Import UInt32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;maximum number of {{block(Asset)}} types that can be stored in the {{term(agent)}} that published the {{term(response document)}}.  
        
        > Note: The implementer is responsible for allocating the appropriate amount of storage capacity required to accommodate the {{property(Header::assetBufferSize)}}.
        &#10;

        """

        self.AssetBufferSize = ""

        # TODO: Import UInt32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;current number of {{block(Asset)}} that are currently stored in the {{term(agent)}} as of the {{property(Header::creationTime)}} that the {{term(agent)}} published the {{term(response document)}}.
        
        {{property(Header::assetCount)}} **MUST NOT** be larger than the value reported for {{property(Header::assetBufferSize)}}.
        &#10;

        """

        self.AssetCount = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;timestamp that an {{term(agent)}} published the {{term(response document)}}. &#10;

        """

        self.CreationTime = ""

        # TODO: Import UInt64 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier for a specific instantiation of the {{term(buffer)}} associated with the {{term(agent)}} that published the {{term(response document)}}.  
             
        {{property(Header::instanceId)}} **MUST** be changed to a different unique number each time the {{term(buffer)}} is cleared and a new set of data begins to be collected.&#10;

        """

        self.InstanceId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identification defining where the {{term(agent)}} that published the {{term(response document)}} is installed or hosted.
        
        {{property(Header::sender)}} **MUST** be either an IP Address or Hostname describing where the {{term(agent)}} is installed or the URL of the {{term(agent)}}; e.g., `http://<address>[:port]/`. 
        
        > Note:  The port number need not be specified if it is the default HTTP port 80.&#10;

        """

        self.Sender = ""

        # TODO: Import Boolean and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;indicates whether the {{term(agent)}} that published the {{term(response document)}} is operating in a test mode.
        
        If {{property(Header::testIndicator)}} is not specified, the value for {{property(Header::testIndicator)}} **MUST** be interpreted to be `false`.&#10;

        """

        self.TestIndicator = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(major)}}, {{term(minor)}}, and {{term(revision)}} number of the MTConnect Standard that defines the {{term(semantic data model)}} that represents the content of the {{term(response document)}}. It also includes the revision number of the {{term(schema)}} associated with that specific {{term(semantic data model)}}.
        
        As an example, the value reported for {{property(Header::version)}} for a {{term(response document)}} that was structured based on {{term(schema)}} revision 10 associated with Version 1.4.0 of the MTConnect Standard would be:  1.4.0.10&#10;

        """

        self.Version = ""



