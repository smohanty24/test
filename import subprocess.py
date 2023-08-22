import subprocess

# Path to JasperStarter executable
jasperstarter_path = "C:\\Program Files (x86)\\JasperStarter\\bin\\jasperstarter"

# Path to the .jrxml report design file
jrxml_file = "C:\\python-test\\test.jrxml"

# Path to the output report (PDF, HTML, etc.)
output_file = "C:\\python-test\\report.pdf"

# Define JasperStarter command
command = [
    jasperstarter_path,
    "process",
    jrxml_file,
    "--output",
    output_file,
    "--format",
    "pdf"
]

# Run the JasperStarter command
subprocess.run(command)
