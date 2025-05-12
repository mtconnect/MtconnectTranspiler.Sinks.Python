using MtconnectTranspiler.Sinks.Python.Example;
using MtconnectTranspiler.Sinks.Python.Example.Models;
using MtconnectTranspiler.Xmi;

namespace MtconnectTranspiler.Sinks.Python.Models
{
    /// <summary>
    /// Represents the abstract for many Python types
    /// </summary>
    public abstract class PythonType : MtconnectVersionedObject
    {
        private string _namespace = "Mtconnect";
        /// <summary>
        /// The intended namespace for the Python type.
        /// </summary>
        public virtual string Namespace
        {
            get { return _namespace; }
            set
            {
                _namespace = value;
                switch (this)
                {
                    case PythonClass pythonClass:
                        TypeCache.RegisterType(pythonClass.ReferenceId, pythonClass.Name, pythonClass.Namespace);
                        break;
                    case Property pythonProperty:
                        TypeCache.RegisterType(pythonProperty.SysML_ID, pythonProperty.Name, pythonProperty.Namespace);
                        break;
                    case PythonPackage pythonPackage:
                        TypeCache.RegisterType(pythonPackage.ReferenceId, pythonPackage.Name, pythonPackage.Namespace);
                        break;
                    case PythonEnum pythonEnum:
                        TypeCache.RegisterType(pythonEnum.ReferenceId, $"{pythonEnum.Name}MetaClass", pythonEnum.Namespace);
                        break;
                    default:
                        break;
                }
            }
        }

        /// <summary>
        /// Internal string, used by <see cref="Name"/>.
        /// </summary>
        protected string _name { get; set; }
        /// <summary>
        /// The intended name for the Python type.
        /// </summary>
        public virtual string Name
        {
            get
            {
                if (string.IsNullOrEmpty(_name))
                    _name = PythonHelperMethods.ToPascalCase(base.SysML_Name);
                return _name;
            }
            set {
                TypeCache.ChangeTypeName(base.SysML_ID, value);
                _name = value;
            }
        }

        /// <summary>
        /// The accessibilty of the Python type.
        /// <list type="bullet">
        /// <item>public</item>
        /// <item>private</item>
        /// <item>protected</item>
        /// <item>internal</item>
        /// <item>protected internal</item>
        /// <item>private protected</item>
        /// </list>
        /// </summary>
        public string AccessModifier { get; set; } = "public";

        /// <summary>
        /// A modifier for the Python type.
        /// <list type="bullet">
        /// <item>abstract</item>
        /// <item>static</item>
        /// <item>sealed</item>
        /// <item>const</item>
        /// <item>event</item>
        /// <item>override</item>
        /// <item>virtual</item>
        /// <item>volatile</item>
        /// <item>extern</item>
        /// </list>
        /// </summary>
        public string Modifier { get; set; }

        /// <summary>
        /// Constructs an <see cref="PythonType"/> more generically. <b>NOTE</b>: You'll need to add items manually from here.
        /// </summary>
        /// <param name="model"><inheritdoc cref="XmiDocument" path="/summary"/></param>
        /// <param name="source"><inheritdoc cref="XmiElement" path="/summary"/></param>
        protected PythonType(XmiDocument model, XmiElement source) : base(model, source) { }
    }
}
