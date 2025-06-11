# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;**DEPRECATED** {{block(Representation)}} for an {{block(Observation)}} where each discrete occurrence of the data may have the same value as the previous occurrence of the data.
&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;
{{block(Discrete)}} for an {{block(Observation)}} is defined by the associated {{property(DataItem::representation)}} as `DISCRETE`.

{{property(DataItem::representation)}} as `DISCRETE` **MUST** have {{property(DataItem::category)}} as `EVENT`.

*MTConnect Version 1.5* replaced {{property(DataItem::representation)}} as `DISCRETE` with {{property(DataItem::discrete)}}.

Each occurrence of the {{block(Observation)}} **MAY** have the same value as the previous occurrence, and **MUST NOT** suppress duplicates.

Examples of {{block(Discrete)}}: A `PartCount` reporting the completion of each part using a 1 to indicate completion of a single part, a `Message` that occurs each time a door opens. &#10;

"""


class DiscreteClass(RepresentationClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""



