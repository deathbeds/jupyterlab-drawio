"""source of truth for ipydrawio version"""

# Copyright 2021 ipydrawio contributors
# Copyright 2020 jupyterlab-drawio contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from pathlib import Path

HERE = Path(__file__).parent
PKG_JSON = HERE / "ext/ipd/package.json"

__js__ = json.loads(PKG_JSON.read_text(encoding="utf-8"))

__version__ = __js__["version"]

__all__ = ["__version__", "__js__"]
