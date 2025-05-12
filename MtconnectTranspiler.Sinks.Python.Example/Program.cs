using ConsoulLibrary;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MtconnectTranspiler;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates.Formatters;
using MtconnectTranspiler.Extensions;
using MtconnectTranspiler.Interpreters;
using MtconnectTranspiler.Sinks.Python.Example;
using MtconnectTranspiler.XmiOptions;

internal class Program
{
    private static void Main(string[] args)
    {
        if (args.Length == 0) throw new ArgumentNullException(nameof(args), "Missing projectPath argument");

        string projectPath = args[0];
        if (!Directory.Exists(projectPath))
        {
            Consoul.Write("Creating project path: " + projectPath);
            Directory.CreateDirectory(projectPath);
        }
        IConfiguration configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
#if DEBUG
            .AddJsonFile("appsettings.Development.json", optional: true, reloadOnChange: true)
#else
            .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
#endif
            .AddEnvironmentVariables()
            .AddCommandLine(args)
            .Build();

        //setup our DI
        var services = new ServiceCollection()
            .AddLogging((builder) =>
            {
                builder.AddConsoulLogger();
            });
        var serviceProvider = services
            .AddSingleton(configuration)
            .AddScribanServices(builder =>
            {
                string templatePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Templates");
                builder
                    .ConfigureTemplateLoader((loader) =>
                        // Use the local "/Templates" directory to store ".scriban" files
                        loader.UseTemplatesPath(templatePath)
                        // If using embedded resources to store ".scriban" files, then provide the assembly
                        //.UseResourceAssembly(typeof(Transpiler).Assembly, "MtconnectTranspiler.Sinks.Python.Example")
                        // Configure a Scriban ScriptObject capable of interpreting SysML comment contents into other formats.
                        // Configure a Scriban ScriptObject capable of formatting strings into code safe formats.
                        .AddMarkdownInterpreter("vscode_docs", new VisualStudioSummaryInterpreter())
                        .AddCodeFormatter("python_formatter", new PythonCodeFormatter())
                    )
                    .ConfigureGenerator((options) => {
                        options.OutputPath = configuration["OutputPath"];
                    });
            })
            .AddScoped<Transpiler>()
            .BuildServiceProvider();

        //configure console logging
        var logger = serviceProvider.GetService<ILoggerFactory>()
            .CreateLogger<Program>();
        logger.LogDebug("Starting application");

        // NOTE: The GitHubRelease can be a reference to a specific tag referring to the version in which to download.
        TranspilerDispatcherOptions? dispatchOptions = null;
        string modelPath = configuration["ModelPath"];
        if (!string.IsNullOrEmpty(modelPath))
        {
            if (!File.Exists(modelPath)) throw new FileNotFoundException(modelPath);

            dispatchOptions = new FromFileOptions() { Filepath = modelPath };
            Consoul.Write("Dispatching from file: " + modelPath);
        }
        else
        {
            dispatchOptions = new FromGitHubOptions() { GitHubRelease = "latest" };
            Consoul.Write("Dispatching from GitHub's latest release");
        }

        using (var tokenSource = new CancellationTokenSource())
        using (var dispatcher = new TranspilerDispatcher(dispatchOptions, serviceProvider.GetService<ILoggerFactory>()
            .CreateLogger<TranspilerDispatcher>()))
        {
            var defaultTranspiler = serviceProvider.GetService<Transpiler>();
            dispatcher.AddSink(defaultTranspiler);

            Consoul.Write("Beginning deserialization and dispatching");
            var task = Task.Run(() => dispatcher.TranspileAsync(tokenSource.Token));

#if DEBUG
            task = task.ContinueWith((t) => tokenSource.Cancel());
            Consoul.Wait(cancellationToken: tokenSource.Token);
#else
            task.Wait();
#endif

            if (task.IsCompletedSuccessfully)
            {
                Consoul.Write("Done!", ConsoleColor.Green);

                Environment.Exit(0);
            }
            else
            {
                Consoul.Write("Cancelled", ConsoleColor.Red);
                Environment.Exit(1);
            }

        }
    }
}