# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;abstract entity that provides telemetry data for a {{block(DataItem)}} at a point in time.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;![Observations](figures/Observations.png "Observations"){: width="0.8"}

> Note: See {{sect(Observations Schema Diagrams)}} for XML schema. The XML schema also shows differences in XML representation of certain MTConnect entities.

{{figure(DeviceStream Example)}} shows a complete example of {{block(DeviceStream)}} for the {{block(Device)}} shown in {{package(Device Information Model)}}.

![DeviceStream Example](figures/DeviceStream%20Example.png "DeviceStream Example"){: width="0.8"}

> Note: See {{lst(devicestream-example)}} for the {{term(XML)}} representation of the same example.


This section provides semantic information for the {{block(Observation)}} model.

> Note: See {{sect(Observations Schema Diagrams)}} for XML schema of {{block(Observation)}} types.

#### Observations made for DataItem

{{block(Component)}} {{termplural(observe)}} {{block(DataItem)}} entities and creates {{block(Observation)}} entities for the {{block(DataItem)}} entities. See {{figure(Observations)}}.

{{block(Observation)}} entities made by a {{block(Component)}} are organized by a {{block(ComponentStream)}} which is specifically created for that {{block(Component)}}.

![Observations made for DataItem Example](figures/Observations%20made%20for%20DataItem%20Example.png "Observations made for DataItem Example"){: width="0.8"}

> Note: See {{sect(Observations made for DataItem Example)}} for how XML representation of the same example is separated into {{term(MTConnectDevices Response Document)}} and {{term(MTConnectStreams Response Document)}}.

{{figure(Observations made for DataItem Example)}} is a subset of {{figure(DeviceStream Example)}}. It shows an example of the association between a {{block(DataItem)}} {{block(Event)}} type (`EMERGENCY_STOP`) and an {{block(Observation)}} {{block(Event)}} type (`EmergencyStop`). See {{sect(Naming Convention for Observation types)}}.

{{figure(Observations made for DataItem Example)}} also shows example of the association between a {{block(Component)}} type (`Controller`) and related {{block(ComponentStream)}}.

#### Naming Convention for Observation types

The name of an {{block(Observation)}} type **MUST** derive from the associated {{property(DataItem::type)}} converted to Pascal-Case by removing underscores (_ ) and capitalizing each word. The conversion **MUST NOT** apply to the following abbreviated words: `PH`, `AC`, `DC` and `URI`. `MTCONNECT` **MUST** be converted to `MTConnect`. See {{figure(Observations made for DataItem Example)}} for an example.

The name of an {{block(Observation)}} type reported in the {{term(MTConnectStreams Response Document)}} is extended when the {{property(DataItem::representation)}} is used to further describe that {{block(DataItem)}} in the {{term(MTConnectDevices Response Document)}}. See {{package(Representations)}} for more details.&#10;

"""


class ObservationGeneralization(ObservationClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier of the {{block(Composition)}} entity defined in the {{term(MTConnectDevices Response Document)}} associated with the data reported for the {{block(Observation)}}.&#10;

        """

        self.CompositionId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier of the {{block(DataItem)}} associated with this {{block(Observation)}}.
        
        {{property(Observation::dataItemId)}} **MUST** match the associated {{property(DataItem::id)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.DataItemId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the {{block(DataItem)}} associated with this {{block(Observation)}}.
        
        {{property(Observation::name)}} **MUST** match the associated {{property(DataItem::name)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Name = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number representing the sequential position of an occurrence of an {{term(observation)}} in the data buffer of an {{term(agent)}}.
        
        {{property(Observation::sequence)}} **MUST** have a value represented as an unsigned 64-bit value from 1 to $$ 2^{64}-1 $$.&#10;

        """

        self.Sequence = ""

        # TODO: Import DataItemSubTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;subtype of the {{block(DataItem)}} associated with this {{block(Observation)}}.
        
        {{property(Observation::subType)}} **MUST** match the associated {{property(DataItem::subType)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.SubType = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;most accurate time available to a piece of equipment that represents the point in time that the data reported was measured.&#10;

        """

        self.Timestamp = ""

        # TODO: Import ComponentGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.MadeByComponent = ""

        # TODO: Import DataItemTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of the {{block(DataItem)}} associated with this {{block(Observation)}}.
        
        {{property(Observation::type)}} **MUST** match the associated {{property(DataItem::type)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Type = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;units of the {{block(DataItem)}} associated with this {{block(Observation)}}.
        
        {{property(Observation::units)}} **MUST** match the associated {{property(DataItem::units)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Units = ""

        # TODO: Import Boolean and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;when `true`, {{property(Observation::result)}} is indeterminate.
        
        > Note 1 to entry: In {{term(XML)}}, when `isUnavailable` is `true`, the {{term(XML)}} `CDATA` of the `Observation` **MUST** be `UNAVAILABLE`.
         ```xml
        <Execution dataItemId="..." ...>UNAVAILABLE</Execution>
        ```
        
        > Note 2 to entry: In {{term(JSON)}}, when `isUnavailable` is `true`, the {{term(JSON)}} `value` of the `Observation` **MUST** be `UNAVAILABLE`.
        ```json
          "Execution" : [ { "dataItemId": "..." ..., "value": "UNAVAILABLE" } ]
        ```&#10;

        """

        self.IsUnavailable = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(observation)}} of the {{block(Observation)}} entity.
        
        The default value type for {{property(Observation::result)}} is `string`.
        
        > Note 1 to entry: in {{term(XML)}} the {{property(Observation::result)}} is the `CDATA` of the Observation {{term(element)}}.
        
        ~~~~xml
        <Execution dataItemId="..." ...>READY</Execution>
        ~~~~
        
        > Note 2 to entry: in {{term(JSON)}} the {{property(Observation::result)}} is the member `value` of the Observation object.
        
        ~~~~json
        "Execution" : [ { "dataItemId": "..." ..., "value": "READY" } ]
        ~~~~&#10;

        """

        self.Result = ""

        # TODO: Import DataItemClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.MadeForDataItem = ""



