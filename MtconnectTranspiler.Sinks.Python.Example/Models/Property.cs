using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.Xmi.UML;

namespace MtconnectTranspiler.Sinks.Python.Models
{
    /// <summary>
    /// Represents a Python property
    /// </summary>
    public class Property : PythonType
    {
        /// <summary>
        /// Reference to the <c>name</c> attribute.
        /// </summary>
        public string NormativeName { get; set; }

        /// <summary>
        /// Reference to any Comments written in the SysML model to be converted into a Python format <c>&lt;summary /&gt;</c>
        /// </summary>
        public Summary Summary { get; protected set; }

        /// <summary>
        /// Reference to the expected property type
        /// </summary>
        public string Type { get; set; }

        public string OriginalPropertyType { get; set; }

        public string Aggregation { get; set; }

        public string Extension { get; set; }

        public string Association { get; set; }

        public string DefaultValue { get; set; }

        private XmiElement? _remoteType { get; set; }

        /// <summary>
        /// Constructs an <see cref="Property"/> more generically. <b>NOTE</b>: You'll need to add items manually from here.
        /// </summary>
        /// <param name="model"><inheritdoc cref="XmiDocument" path="/summary"/></param>
        /// <param name="source"><inheritdoc cref="XmiElement" path="/summary"/></param>
        public Property(XmiDocument model, UmlProperty source) : base(model, source)
        {
            NormativeName = source.Name;

            if (source.Comments?.Length > 0)
                Summary = new Summary(source.Comments);

            AccessModifier = source.Visibility;

            Modifier = source.IsStatic ? "static" : source.IsReadOnly ? "readonly" : "";

            XmiElement? remoteType = null;
            Type = PythonHelperMethods.ToPrimitiveType(model, source)?.Name
                ?? PythonHelperMethods.TypeDeepSearch(model, source.PropertyType, out remoteType)
                ?? "object";

            OriginalPropertyType = source.PropertyType;

            Aggregation = source.Aggregation;
            Extension = source.Extension?.Extender;
            Association = PythonHelperMethods.TypeDeepSearch(model, source.Association, out remoteType);
            if (source.DefaultValue is UmlInstanceValue instanceValue)
            {
                DefaultValue = PythonHelperMethods.TypeDeepSearch(model, instanceValue.Instance, out XmiElement instanceType);
            } else
            {
                DefaultValue = source.DefaultValue?.Name;
            }

            // TODO: Determine multiplicity from lowerValue and upperValue
        }

    }
}
