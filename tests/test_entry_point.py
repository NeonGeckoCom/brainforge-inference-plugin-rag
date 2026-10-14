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

from importlib.metadata import entry_points

from neon_inference_plugin_rag import RagStep
from neon_inference_plugin_rag import ResponseParser

def test_entry_point_loads_rag_step():
    matches = [
        ep for ep in entry_points(group="brainforge.inference.request_steps")
        if ep.name == "neon.rag"
    ]
    assert len(matches) == 1
    loaded = matches[0].load()
    assert loaded is RagStep
    assert loaded.id == "neon.rag"


def test_entry_point_loads_citation_step():
    matches = [
        ep for ep in entry_points(group="brainforge.inference.response_steps")
        if ep.name == "neon.citations"
    ]
    assert len(matches) == 1
    loaded = matches[0].load()
    assert loaded is ResponseParser
    assert loaded.id == "neon.citations"
