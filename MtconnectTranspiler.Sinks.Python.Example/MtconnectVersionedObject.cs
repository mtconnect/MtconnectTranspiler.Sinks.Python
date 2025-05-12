using MtconnectTranspiler.Sinks.Models;
using MtconnectTranspiler.Xmi;

namespace MtconnectTranspiler.Sinks.Python
{
    /// <inheritdoc />
    public abstract class MtconnectVersionedObject : VersionedObject
    {
        /// <inheritdoc />
        public MtconnectVersionedObject(XmiDocument model, XmiElement source) : base(model, source) { }

        protected override string lookupMtconnectVersion(string? version)
        {
            return version ?? "1.0.1";
        }
    }
}