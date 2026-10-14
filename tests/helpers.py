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

from typing import Optional

from neon_data_models.models.api.llm import (
    LLMPersona,
    LLMRequest,
    LLMResponse,
)


def make_request(**overrides) -> LLMRequest:
    values = dict(
        query="hello",
        history=[("user", "hi"), ("llm", "hey")],
        persona=LLMPersona(name="vanilla"),
        model="demo@1",
    )
    values.update(overrides)
    return LLMRequest(**values)


def make_response(text: str = "ok", request: Optional[LLMRequest] = None,
                  **overrides) -> LLMResponse:
    request = request or make_request()
    values = dict(
        response=text,
        history=list(request.history) + [("user", request.query), ("llm", text)],
    )
    values.update(overrides)
    return LLMResponse(**values)
