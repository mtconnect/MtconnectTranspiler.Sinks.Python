using CaseExtensions;
using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.Xmi.UML;

namespace MtconnectTranspiler.Sinks.Python.Models
{
    /// <summary>
    /// Represents a generic constraint which could be used to create methods
    /// </summary>
    public class Constraint : MtconnectVersionedObject
    {
        /// <summary>
        /// Internal string, used by <see cref="Name"/>.
        /// </summary>
        protected string _name { get; set; } = string.Empty;
        /// <summary>
        /// The intended name for the Python method.
        /// </summary>
        public string Name
        {
            get
            {
                if (string.IsNullOrEmpty(_name))
                {
                    _name = base.SysML_Name.ToPascalCase();
                }
                return _name;
            }
            set { _name = value; }
        }

        /// <summary>
        /// Refers to the language of the <see cref="RawScript"/>. <b>NOTE</b>: As of v2.0 of the MTConnect Standard, OCL2.0 is typical language used.
        /// </summary>
        public string SourceLanguage { get; set; } = "Unspecified";

        /// <summary>
        /// Source code that defines the logic for the constraint.
        /// </summary>
        public string RawScript { get; set; }

        /// <summary>
        /// Constructs a new <see cref="Constraint"/>
        /// </summary>
        /// <param name="model"><inheritdoc cref="XmiDocument"/></param>
        /// <param name="source"><inheritdoc cref="UmlConstraint"/></param>
        public Constraint(XmiDocument model, UmlConstraint source) : base(model, source)
        {
            SourceLanguage = source.Specification?.Language ?? "Unspecified";
            RawScript = source.Specification?.Body ?? string.Empty;
        }
    }
}
