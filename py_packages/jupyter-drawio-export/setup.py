"""
Copyright 2020 jupyterlab-drawio contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
VERSION = [*HERE.glob("src/jupyter_drawio_export/_version.py")][0]

version = re.findall(
    r"""__version__\s*=\s*"([^"]+)""", VERSION.read_text(encoding="utf-8")
)[0]


if __name__ == "__main__":
    import setuptools
    setuptools.setup(
        version=version,
        data_files=[
            (
                "etc/jupyter/jupyter_notebook_config.d",
                ["src/jupyter_drawio_export/etc/jupyter-drawio-export.json"],
            )
        ],

    )
