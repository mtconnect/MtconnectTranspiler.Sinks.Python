# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""

"""


class FeatureMeasurementResultClass(TableClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier of this measurement.&#10;

        """

        self.MeasurementId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(UUID)}} of the feature.&#10;

        """

        self.FeaturePersistentId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(UUID)}} of the characteristic.&#10;

        """

        self.CharacteristicPersistentId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;class of measurement being performed. {{cite(QIF 3:2018 Section 6.3)}}
        
        Examples: `POINT`, `RADIUS`, `ANGLE`, `LENGTH`, etc.&#10;

        """

        self.MeasurementType = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;measurement based on the measurement type.&#10;

        """

        self.MeasurementValue = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;engineering units of the measurement.&#10;

        """

        self.MeasurementUnits = ""

        # TODO: Import CharacteristicStatusEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;pass/fail result of the measurement.&#10;

        """

        self.CharacteristicStatus = ""

        # TODO: Import UncertaintyTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;method used to compute {{term(standard uncertainty)}}.&#10;

        """

        self.UncertaintyType = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(uncertainty)}} specified by `UNCERTAINTY_TYPE`.&#10;

        """

        self.Uncertainty = ""



