# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Observation)}} that provides the {{term(condition)}} of a piece of equipment or a {{term(Component)}}.

&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;It provides the information and data reported from a piece of equipment with {{property(DataItem::category)}} as `CONDITION` in the {{term(MTConnectDevices Response Document)}}.

{{figure(Condition Example)}} shows {{block(Condition)}} type examples for various {{property(Condition::state)}}: `Normal` (`dataItemId` = `path_system`) and `Warning` (`dataItemId` = `logic_cond`). It also shows an example for when the {{property(Condition::state)}} is not available (`dataItemId` = `cont_system`).

![Condition Example](figures/Condition%20Example.png "Condition Example"){: width="0.8"}

> Note: See {{lst(condition-example)}} for the {{term(XML)}} representation of the same example.

The following {{sect(Value Properties of Condition)}} lists the additional and/or updated attributes for {{block(Condition)}}.&#10;

"""


class ConditionClass(ObservationGeneralization):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;native code is the proprietary identifier designating a specific alarm, fault or warning code provided by the piece of equipment.&#10;

        """

        self.NativeCode = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;severity information to a client software application if the piece of equipment designates a severity level to a fault.&#10;

        """

        self.NativeSeverity = ""

        # TODO: Import QualifierEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;additional information regarding a {{term(condition state)}} associated with the measured value of a process variable.
        
        {{property(Condition::qualifier)}} defines whether the {{term(condition state)}} represented indicates a measured value that is above or below an expected value of a process variable.&#10;

        """

        self.Qualifier = ""

        # TODO: Import StatisticEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{property(Condition::statistic)}} provides additional information describing the meaning of the {{block(Condition)}} entity.
        
        {{property(Condition::statistic)}} **MUST** match the {{property(DataItem::statistic)}} defined in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.Statistic = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;specifies the language of the {{property(Observation::result)}} returned for the {{block(Condition)}}. 
        
        See {{cite(IETF RFC 4646)}} (http://www.ietf.org/rfc/rfc4646.txt).&#10;

        """

        self.XsLang = ""

        # TODO: Import ComponentStreamClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.OrganizedByComponentStream = ""

        # TODO: Import ConditionStateEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(condition state)}} of the piece of equipment or {{block(Component)}}.&#10;

        """

        self.State = ""

        # TODO: Import ConditionEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier of an individual {{term(condition activation)}} provided by a piece of equipment.
        
        {{property(Condition::conditionId)}} **MUST** be unique for all concurrent {{termpl(condition activation)}}.
        
        {{property(Condition::conditionId)}} **MUST** be maintained for all state transitions related to the same {{term(condition activation)}}.
        
        Multiple {{property(Condition::conditionId)}}s **MAY** exist for the same {{property(nativeCode)}}.
        
        If {{property(Condition::conditionId)}} is not given, the value is the {{property(Condition::nativeCode)}}. If {{property(Condition::nativeCode)}} and {{property(Condition::conditionId)}} are not given, {{property(Condition::conditionId)}} **MUST** be generated.&#10;

        """

        self.ConditionId = ""



