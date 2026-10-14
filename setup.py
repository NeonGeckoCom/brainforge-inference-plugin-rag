# Copyright (C) 2008-2026 Neongecko.com Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import getenv, path

from setuptools import find_packages, setup

BASE_PATH = path.abspath(path.dirname(__file__))


def get_requirements(requirements_filename: str):
    requirements_file = path.join(
        BASE_PATH, "requirements", requirements_filename
    )
    with open(requirements_file, "r", encoding="utf-8") as r:
        requirements = r.readlines()
    requirements = [
        r.strip()
        for r in requirements
        if r.strip() and not r.strip().startswith("#")
    ]

    for i in range(0, len(requirements)):
        r = requirements[i]
        if "@" in r:
            parts = [
                p.lower() if p.strip().startswith("git+http") else p
                for p in r.split("@")
            ]
            r = "@".join(parts)
        if getenv("GITHUB_TOKEN"):
            if "github.com" in r:
                requirements[i] = r.replace(
                    "github.com", f"{getenv('GITHUB_TOKEN')}@github.com"
                )
    return requirements


with open(path.join(BASE_PATH, "README.md"), "r") as f:
    long_description = f.read()

with open(
    path.join(BASE_PATH, "neon_inference_plugin_rag", "version.py"),
    "r",
    encoding="utf-8",
) as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]


setup(
    name="neon-inference-plugin-rag",
    version=version,
    description="RAG retrieval and citation steps for BrainForge inference pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeonGeckoCom/neon-inference-plugin-rag",
    author="NeonGecko",
    author_email="developers@neon.ai",
    license="AGPL-3.0-only",
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements("requirements.txt"),
    extras_require={
        "test": get_requirements("test.txt"),
    },
    zip_safe=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "brainforge.inference.request_steps": [
            "neon.rag = neon_inference_plugin_rag:RagStep",
        ],
        "brainforge.inference.response_steps": [
            "neon.citations = neon_inference_plugin_rag:ResponseParser",
        ],
    },
)
