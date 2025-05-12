using MtconnectTranspiler.Sinks.Python.Example;
using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.Xmi.UML;

namespace MtconnectTranspiler.Sinks.Python.Models
{
    /// <summary>
    /// Represents a Python <see cref="PythonEnum"/> value.
    /// </summary>
    public class EnumItem : MtconnectVersionedObject
    {
        /// <summary>
        /// Reference to any Comments written in the SysML model to be converted into a Python format <c>&lt;summary /&gt;</c>
        /// </summary>
        public Summary Summary { get; protected set; }

        /// <summary>
        /// Internal string, used by <see cref="Name"/>.
        /// </summary>
        protected string _name { get; set; }
        /// <summary>
        /// <inheritdoc cref="PythonType.Name"/>
        /// </summary>
        public string Name
        {
            get
            {
                if (string.IsNullOrEmpty(_name))
                    _name = PythonHelperMethods.ToSnakeCase(base.SysML_Name);
                return _name;
            }
            set { _name = value; }
        }

        public string OriginalName => base.SysML_Name;

        private string _namespace;
        public string Namespace
        {
            get { return _namespace; }
            set
            {
                _namespace = value;
                TypeCache.RegisterType(this.SysML_ID, SysML_Name, _namespace);
            }
        }

        /// <summary>
        /// Constructs an <see cref="EnumItem"/> more generically. <b>NOTE</b>: You'll need to add items manually from here.
        /// </summary>
        /// <param name="model"><inheritdoc cref="XmiDocument" path="/summary"/></param>
        /// <param name="source"><inheritdoc cref="XmiElement" path="/summary"/></param>
        public EnumItem(XmiDocument model, XmiElement source) : base(model, source) { }


        /// <summary>
        /// <inheritdoc cref="EnumItem(XmiDocument, XmiElement)"/>
        /// </summary>
        /// <param name="model"><inheritdoc cref="EnumItem(XmiDocument, XmiElement)" path="/param[@name='model']"/></param>
        /// <param name="source">The source <see cref="UmlEnumerationLiteral"/> to convert into an <see cref="PythonEnum"/></param>
        public EnumItem(XmiDocument model, UmlEnumerationLiteral source) : this(model, source as XmiElement)
        {
            if (source?.Comments?.Length > 0)
                Summary = new Summary(source.Comments);
        }

        /// <summary>
        /// <inheritdoc cref="EnumItem(XmiDocument, XmiElement)"/>
        /// </summary>
        /// <param name="model"><inheritdoc cref="EnumItem(XmiDocument, XmiElement)" path="/param[@name='model']"/></param>
        /// <param name="source">The source <see cref="UmlClass"/> to convert into an <see cref="EnumItem"/></param>
        public EnumItem(XmiDocument model, UmlClass source) : this(model, source as XmiElement)
        {
            if (source?.Comments?.Length > 0)
                Summary = new Summary(source.Comments);
        }

    }
}
