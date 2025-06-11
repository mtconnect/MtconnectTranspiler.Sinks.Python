# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{termplural(organize)}} data reported from a {{block(Device)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(DeviceStream)}} **MUST** be provided for each {{block(Device)}} reporting data in an {{term(MTConnectStreams Response Document)}}.

If the response to the request for data from an {{term(agent)}} does not contain any data for a specific {{block(Device)}}, an empty {{block(DeviceStream)}} entity **MAY** be created to indicate that the {{block(Device)}} exists, but there was no data available.&#10;

"""


class DeviceStreamClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the {{block(Device)}}.
        
        The value reported for {{property(DeviceStream::name)}} **MUST** be the same as the value defined for the {{property(Device::name)}} in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Name = ""

        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;uuid of the {{block(Device)}}.  The value reported for {{property(DeviceStream::uuid)}} **MUST** be the same as the value defined for the {{property(Device::uuid)}} of the same {{block(Device)}} in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Uuid = ""

        # TODO: Import ComponentStreamClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasComponentStream = ""



