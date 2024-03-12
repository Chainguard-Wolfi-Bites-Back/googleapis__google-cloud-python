# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1alpha",
    manifest={
        "IndustryVertical",
        "SolutionType",
        "SearchTier",
        "SearchAddOn",
        "Interval",
        "CustomAttribute",
        "UserInfo",
        "EmbeddingConfig",
        "DoubleList",
        "GuidedSearchSpec",
        "CustomFineTuningSpec",
        "IdpConfig",
        "Principal",
    },
)


class IndustryVertical(proto.Enum):
    r"""The industry vertical associated with the
    [DataStore][google.cloud.discoveryengine.v1alpha.DataStore].

    Values:
        INDUSTRY_VERTICAL_UNSPECIFIED (0):
            Value used when unset.
        GENERIC (1):
            The generic vertical for documents that are
            not specific to any industry vertical.
        MEDIA (2):
            The media industry vertical.
    """
    INDUSTRY_VERTICAL_UNSPECIFIED = 0
    GENERIC = 1
    MEDIA = 2


class SolutionType(proto.Enum):
    r"""The type of solution.

    Values:
        SOLUTION_TYPE_UNSPECIFIED (0):
            Default value.
        SOLUTION_TYPE_RECOMMENDATION (1):
            Used for Recommendations AI.
        SOLUTION_TYPE_SEARCH (2):
            Used for Discovery Search.
        SOLUTION_TYPE_CHAT (3):
            Used for use cases related to the Generative
            AI agent.
    """
    SOLUTION_TYPE_UNSPECIFIED = 0
    SOLUTION_TYPE_RECOMMENDATION = 1
    SOLUTION_TYPE_SEARCH = 2
    SOLUTION_TYPE_CHAT = 3


class SearchTier(proto.Enum):
    r"""Tiers of search features. Different tiers might have
    different pricing. To learn more, please check the pricing
    documentation.

    Values:
        SEARCH_TIER_UNSPECIFIED (0):
            Default value when the enum is unspecified.
            This is invalid to use.
        SEARCH_TIER_STANDARD (1):
            Standard tier.
        SEARCH_TIER_ENTERPRISE (2):
            Enterprise tier.
    """
    SEARCH_TIER_UNSPECIFIED = 0
    SEARCH_TIER_STANDARD = 1
    SEARCH_TIER_ENTERPRISE = 2


class SearchAddOn(proto.Enum):
    r"""Add-on that provides additional functionality for search.

    Values:
        SEARCH_ADD_ON_UNSPECIFIED (0):
            Default value when the enum is unspecified.
            This is invalid to use.
        SEARCH_ADD_ON_LLM (1):
            Large language model add-on.
    """
    SEARCH_ADD_ON_UNSPECIFIED = 0
    SEARCH_ADD_ON_LLM = 1


class Interval(proto.Message):
    r"""A floating point interval.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        minimum (float):
            Inclusive lower bound.

            This field is a member of `oneof`_ ``min``.
        exclusive_minimum (float):
            Exclusive lower bound.

            This field is a member of `oneof`_ ``min``.
        maximum (float):
            Inclusive upper bound.

            This field is a member of `oneof`_ ``max``.
        exclusive_maximum (float):
            Exclusive upper bound.

            This field is a member of `oneof`_ ``max``.
    """

    minimum: float = proto.Field(
        proto.DOUBLE,
        number=1,
        oneof="min",
    )
    exclusive_minimum: float = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="min",
    )
    maximum: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="max",
    )
    exclusive_maximum: float = proto.Field(
        proto.DOUBLE,
        number=4,
        oneof="max",
    )


class CustomAttribute(proto.Message):
    r"""A custom attribute that is not explicitly modeled in a resource,
    e.g. [UserEvent][google.cloud.discoveryengine.v1alpha.UserEvent].

    Attributes:
        text (MutableSequence[str]):
            The textual values of this custom attribute. For example,
            ``["yellow", "green"]`` when the key is "color".

            Empty string is not allowed. Otherwise, an
            ``INVALID_ARGUMENT`` error is returned.

            Exactly one of
            [CustomAttribute.text][google.cloud.discoveryengine.v1alpha.CustomAttribute.text]
            or
            [CustomAttribute.numbers][google.cloud.discoveryengine.v1alpha.CustomAttribute.numbers]
            should be set. Otherwise, an ``INVALID_ARGUMENT`` error is
            returned.
        numbers (MutableSequence[float]):
            The numerical values of this custom attribute. For example,
            ``[2.3, 15.4]`` when the key is "lengths_cm".

            Exactly one of
            [CustomAttribute.text][google.cloud.discoveryengine.v1alpha.CustomAttribute.text]
            or
            [CustomAttribute.numbers][google.cloud.discoveryengine.v1alpha.CustomAttribute.numbers]
            should be set. Otherwise, an ``INVALID_ARGUMENT`` error is
            returned.
    """

    text: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    numbers: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=2,
    )


class UserInfo(proto.Message):
    r"""Information of an end user.

    Attributes:
        user_id (str):
            Highly recommended for logged-in users. Unique identifier
            for logged-in user, such as a user name. Don't set for
            anonymous users.

            Always use a hashed value for this ID.

            Don't set the field to the same fixed ID for different
            users. This mixes the event history of those users together,
            which results in degraded model quality.

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an ``INVALID_ARGUMENT`` error
            is returned.
        user_agent (str):
            User agent as included in the HTTP header.

            The field must be a UTF-8 encoded string with a length limit
            of 1,000 characters. Otherwise, an ``INVALID_ARGUMENT``
            error is returned.

            This should not be set when using the client side event
            reporting with GTM or JavaScript tag in
            [UserEventService.CollectUserEvent][google.cloud.discoveryengine.v1alpha.UserEventService.CollectUserEvent]
            or if
            [UserEvent.direct_user_request][google.cloud.discoveryengine.v1alpha.UserEvent.direct_user_request]
            is set.
    """

    user_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EmbeddingConfig(proto.Message):
    r"""Defines embedding config, used for bring your own embeddings
    feature.

    Attributes:
        field_path (str):
            Full field path in the schema mapped as
            embedding field.
    """

    field_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DoubleList(proto.Message):
    r"""Double list.

    Attributes:
        values (MutableSequence[float]):
            Double values.
    """

    values: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=1,
    )


class GuidedSearchSpec(proto.Message):
    r"""Defines guided search spec.

    Attributes:
        enable_refinement_attributes (bool):
            Whether or not to enable and include
            refinement attributes in gudied search result.
        enable_related_questions (bool):
            Whether or not to enable and include related
            questions in search response.
        max_related_questions (int):
            Max number of related questions to be returned. The valid
            range is [1, 5]. If enable_related_questions is true, the
            default value is 3.
    """

    enable_refinement_attributes: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    enable_related_questions: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    max_related_questions: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CustomFineTuningSpec(proto.Message):
    r"""Defines custom fine tuning spec.

    Attributes:
        enable_search_adaptor (bool):
            Whether or not to enable and include custom
            fine tuned search adaptor model.
    """

    enable_search_adaptor: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class IdpConfig(proto.Message):
    r"""Identity Provider Config.

    Attributes:
        idp_type (google.cloud.discoveryengine_v1alpha.types.IdpConfig.IdpType):
            Identity provider type configured.
        external_idp_config (google.cloud.discoveryengine_v1alpha.types.IdpConfig.ExternalIdpConfig):
            External Identity provider config.
    """

    class IdpType(proto.Enum):
        r"""Identity Provider Type.

        Values:
            IDP_TYPE_UNSPECIFIED (0):
                Default value. ACL search not enabled.
            GSUITE (1):
                Google 1P provider.
            THIRD_PARTY (2):
                Third party provider.
        """
        IDP_TYPE_UNSPECIFIED = 0
        GSUITE = 1
        THIRD_PARTY = 2

    class ExternalIdpConfig(proto.Message):
        r"""Third party IDP Config.

        Attributes:
            workforce_pool_name (str):
                Workforce pool name. Example:
                "locations/global/workforcePools/pool_id".
        """

        workforce_pool_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    idp_type: IdpType = proto.Field(
        proto.ENUM,
        number=1,
        enum=IdpType,
    )
    external_idp_config: ExternalIdpConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ExternalIdpConfig,
    )


class Principal(proto.Message):
    r"""Principal identifier of a user or a group.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_id (str):
            User identifier. For Google Workspace user account, user_id
            should be the google workspace user email. For non-google
            identity provider user account, user_id is the mapped user
            identifier configured during the workforcepool config.

            This field is a member of `oneof`_ ``principal``.
        group_id (str):
            Group identifier. For Google Workspace user account,
            group_id should be the google workspace group email. For
            non-google identity provider user account, group_id is the
            mapped group identifier configured during the workforcepool
            config.

            This field is a member of `oneof`_ ``principal``.
    """

    user_id: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="principal",
    )
    group_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="principal",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
