"""
The MIT License (MIT)

Copyright (c) 2022-present tag-epic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import List, Literal, Optional, TypedDict

from typing_extensions import NotRequired

from .snowflake import Snowflake

AutoModerationEventType = Literal[1]
AutoModerationTriggerType = Literal[1, 2, 3, 4]
KeywordPresetType = Literal[1, 2, 3]
AutoModerationActionType = Literal[1, 2, 3, 4]


class AutoModerationTriggerMetadata(TypedDict, total=False):
    keyword_filter: List[str]
    presets: List[KeywordPresetType]
    allow_list: List[str]


class AutoModerationActionMetadata(TypedDict, total=False):
    channel_id: Snowflake
    duration_seconds: int


class AutoModerationAction(TypedDict):
    type: AutoModerationActionType
    metadata: NotRequired[AutoModerationActionMetadata]


class AutoModerationRule(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: AutoModerationEventType
    trigger_type: AutoModerationTriggerType
    trigger_metadata: AutoModerationTriggerMetadata
    actions: List[AutoModerationAction]
    enabled: bool
    exempt_roles: List[Snowflake]
    exempt_channels: List[Snowflake]


class AutoModerationRuleCreate(TypedDict):
    name: str
    event_type: AutoModerationEventType
    trigger_type: AutoModerationTriggerType
    actions: List[AutoModerationAction]
    trigger_metadata: NotRequired[AutoModerationTriggerMetadata]
    enabled: NotRequired[bool]
    exempt_roles: NotRequired[List[Snowflake]]
    exempt_channels: NotRequired[List[Snowflake]]


class AutoModerationRuleModify(TypedDict, total=False):
    name: str
    event_type: AutoModerationEventType
    trigger_metadata: AutoModerationTriggerMetadata
    actions: List[AutoModerationAction]
    enabled: bool
    exempt_roles: List[Snowflake]
    exempt_channels: List[Snowflake]


class AutoModerationActionExecution(TypedDict):
    guild_id: Snowflake
    action: AutoModerationAction
    rule_id: Snowflake
    rule_trigger_type: AutoModerationTriggerType
    user_id: Snowflake
    matched_keyword: Optional[str]
    channel_id: NotRequired[Snowflake]
    message_id: NotRequired[Snowflake]
    alert_system_message_id: NotRequired[Snowflake]
    content: NotRequired[str]
    matched_content: NotRequired[Optional[str]]
