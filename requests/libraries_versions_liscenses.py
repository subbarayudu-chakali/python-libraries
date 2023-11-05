import subprocess
import requests

# Get the list of installed packages and their versions
packages = subprocess.check_output(['pip', 'freeze'])

# Split the output into lines, and then split each line into package and version
package_lines = packages.split('\n')
packages_and_versions = []
for line in package_lines:
    parts = line.split('==')
    package = parts[0].strip()
    version = parts[1].strip()
    packages_and_versions.append((package, version))

# Loop through each package and get the license information from PyPI
licenses = {}
for package, version in packages_and_versions:
    url = f"https://pypi.org/project/{package}/{version}/LICENSE"
    response = requests.get(url)
    licenses[package] = response.text

# Print the list of packages and their licenses
print("Packages and Licenses:")
for package, license in licenses.items():
    print(f"{package}: {license}")
