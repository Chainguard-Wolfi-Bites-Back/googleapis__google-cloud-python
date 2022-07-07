# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.beyondcorp.clientgateways.v1",
    manifest={
        "ClientGateway",
        "ListClientGatewaysRequest",
        "ListClientGatewaysResponse",
        "GetClientGatewayRequest",
        "CreateClientGatewayRequest",
        "DeleteClientGatewayRequest",
        "ClientGatewayOperationMetadata",
    },
)


class ClientGateway(proto.Message):
    r"""Message describing ClientGateway object.

    Attributes:
        name (str):
            Required. name of resource. The name is
            ignored during creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        state (google.cloud.beyondcorp_clientgateways_v1.types.ClientGateway.State):
            Output only. The operational state of the
            gateway.
        id (str):
            Output only. A unique identifier for the
            instance generated by the system.
        client_connector_service (str):
            Output only. The client connector service name that the
            client gateway is associated to. Client Connector Services,
            named as follows:
            ``projects/{project_id}/locations/{location_id}/client_connector_services/{client_connector_service_id}``.
    """

    class State(proto.Enum):
        r"""Represents the different states of a gateway."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        UPDATING = 2
        DELETING = 3
        RUNNING = 4
        DOWN = 5
        ERROR = 6

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    id = proto.Field(
        proto.STRING,
        number=5,
    )
    client_connector_service = proto.Field(
        proto.STRING,
        number=6,
    )


class ListClientGatewaysRequest(proto.Message):
    r"""Message for requesting list of ClientGateways.

    Attributes:
        parent (str):
            Required. Parent value for
            ListClientGatewaysRequest.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    filter = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by = proto.Field(
        proto.STRING,
        number=5,
    )


class ListClientGatewaysResponse(proto.Message):
    r"""Message for response to listing ClientGateways.

    Attributes:
        client_gateways (Sequence[google.cloud.beyondcorp_clientgateways_v1.types.ClientGateway]):
            The list of ClientGateway.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (Sequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    client_gateways = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ClientGateway",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClientGatewayRequest(proto.Message):
    r"""Message for getting a ClientGateway.

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClientGatewayRequest(proto.Message):
    r"""Message for creating a ClientGateway.

    Attributes:
        parent (str):
            Required. Value for parent.
        client_gateway_id (str):
            Optional. User-settable client gateway resource ID.

            -  Must start with a letter.
            -  Must contain between 4-63 characters from
               ``/[a-z][0-9]-/``.
            -  Must end with a number or a letter.
        client_gateway (google.cloud.beyondcorp_clientgateways_v1.types.ClientGateway):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    client_gateway_id = proto.Field(
        proto.STRING,
        number=2,
    )
    client_gateway = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ClientGateway",
    )
    request_id = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteClientGatewayRequest(proto.Message):
    r"""Message for deleting a ClientGateway

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )


class ClientGatewayOperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target = proto.Field(
        proto.STRING,
        number=3,
    )
    verb = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
