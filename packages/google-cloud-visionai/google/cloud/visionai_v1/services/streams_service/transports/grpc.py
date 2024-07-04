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
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers, operations_v1
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
import grpc  # type: ignore

from google.cloud.visionai_v1.types import common, streams_resources, streams_service

from .base import DEFAULT_CLIENT_INFO, StreamsServiceTransport


class StreamsServiceGrpcTransport(StreamsServiceTransport):
    """gRPC backend transport for StreamsService.

    Service describing handlers for resources.
    Vision API and Vision AI API are two independent APIs developed
    by the same team. Vision API is for people to annotate their
    image while Vision AI is an e2e solution for customer to build
    their own computer vision application.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "visionai.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'visionai.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if a ``channel`` instance is provided.
            channel (Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, grpc.Channel):
            # Ignore credentials if a channel was passed.
            credentials = None
            self._ignore_credentials = True
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            # initialize with the provided callable or the default channel
            channel_init = channel or type(self).create_channel
            self._grpc_channel = channel_init(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "visionai.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [streams_service.ListClustersRequest], streams_service.ListClustersResponse
    ]:
        r"""Return a callable for the list clusters method over gRPC.

        Lists Clusters in a given project and location.

        Returns:
            Callable[[~.ListClustersRequest],
                    ~.ListClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_clusters" not in self._stubs:
            self._stubs["list_clusters"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/ListClusters",
                request_serializer=streams_service.ListClustersRequest.serialize,
                response_deserializer=streams_service.ListClustersResponse.deserialize,
            )
        return self._stubs["list_clusters"]

    @property
    def get_cluster(
        self,
    ) -> Callable[[streams_service.GetClusterRequest], common.Cluster]:
        r"""Return a callable for the get cluster method over gRPC.

        Gets details of a single Cluster.

        Returns:
            Callable[[~.GetClusterRequest],
                    ~.Cluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cluster" not in self._stubs:
            self._stubs["get_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/GetCluster",
                request_serializer=streams_service.GetClusterRequest.serialize,
                response_deserializer=common.Cluster.deserialize,
            )
        return self._stubs["get_cluster"]

    @property
    def create_cluster(
        self,
    ) -> Callable[[streams_service.CreateClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the create cluster method over gRPC.

        Creates a new Cluster in a given project and
        location.

        Returns:
            Callable[[~.CreateClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cluster" not in self._stubs:
            self._stubs["create_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/CreateCluster",
                request_serializer=streams_service.CreateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cluster"]

    @property
    def update_cluster(
        self,
    ) -> Callable[[streams_service.UpdateClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the update cluster method over gRPC.

        Updates the parameters of a single Cluster.

        Returns:
            Callable[[~.UpdateClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_cluster" not in self._stubs:
            self._stubs["update_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/UpdateCluster",
                request_serializer=streams_service.UpdateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_cluster"]

    @property
    def delete_cluster(
        self,
    ) -> Callable[[streams_service.DeleteClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete cluster method over gRPC.

        Deletes a single Cluster.

        Returns:
            Callable[[~.DeleteClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cluster" not in self._stubs:
            self._stubs["delete_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/DeleteCluster",
                request_serializer=streams_service.DeleteClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cluster"]

    @property
    def list_streams(
        self,
    ) -> Callable[
        [streams_service.ListStreamsRequest], streams_service.ListStreamsResponse
    ]:
        r"""Return a callable for the list streams method over gRPC.

        Lists Streams in a given project and location.

        Returns:
            Callable[[~.ListStreamsRequest],
                    ~.ListStreamsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_streams" not in self._stubs:
            self._stubs["list_streams"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/ListStreams",
                request_serializer=streams_service.ListStreamsRequest.serialize,
                response_deserializer=streams_service.ListStreamsResponse.deserialize,
            )
        return self._stubs["list_streams"]

    @property
    def get_stream(
        self,
    ) -> Callable[[streams_service.GetStreamRequest], streams_resources.Stream]:
        r"""Return a callable for the get stream method over gRPC.

        Gets details of a single Stream.

        Returns:
            Callable[[~.GetStreamRequest],
                    ~.Stream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_stream" not in self._stubs:
            self._stubs["get_stream"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/GetStream",
                request_serializer=streams_service.GetStreamRequest.serialize,
                response_deserializer=streams_resources.Stream.deserialize,
            )
        return self._stubs["get_stream"]

    @property
    def create_stream(
        self,
    ) -> Callable[[streams_service.CreateStreamRequest], operations_pb2.Operation]:
        r"""Return a callable for the create stream method over gRPC.

        Creates a new Stream in a given project and location.

        Returns:
            Callable[[~.CreateStreamRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_stream" not in self._stubs:
            self._stubs["create_stream"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/CreateStream",
                request_serializer=streams_service.CreateStreamRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_stream"]

    @property
    def update_stream(
        self,
    ) -> Callable[[streams_service.UpdateStreamRequest], operations_pb2.Operation]:
        r"""Return a callable for the update stream method over gRPC.

        Updates the parameters of a single Stream.

        Returns:
            Callable[[~.UpdateStreamRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_stream" not in self._stubs:
            self._stubs["update_stream"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/UpdateStream",
                request_serializer=streams_service.UpdateStreamRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_stream"]

    @property
    def delete_stream(
        self,
    ) -> Callable[[streams_service.DeleteStreamRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete stream method over gRPC.

        Deletes a single Stream.

        Returns:
            Callable[[~.DeleteStreamRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_stream" not in self._stubs:
            self._stubs["delete_stream"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/DeleteStream",
                request_serializer=streams_service.DeleteStreamRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_stream"]

    @property
    def get_stream_thumbnail(
        self,
    ) -> Callable[
        [streams_service.GetStreamThumbnailRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the get stream thumbnail method over gRPC.

        Gets the thumbnail (image snapshot) of a single
        Stream.

        Returns:
            Callable[[~.GetStreamThumbnailRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_stream_thumbnail" not in self._stubs:
            self._stubs["get_stream_thumbnail"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/GetStreamThumbnail",
                request_serializer=streams_service.GetStreamThumbnailRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_stream_thumbnail"]

    @property
    def generate_stream_hls_token(
        self,
    ) -> Callable[
        [streams_service.GenerateStreamHlsTokenRequest],
        streams_service.GenerateStreamHlsTokenResponse,
    ]:
        r"""Return a callable for the generate stream hls token method over gRPC.

        Generate the JWT auth token required to get the
        stream HLS contents.

        Returns:
            Callable[[~.GenerateStreamHlsTokenRequest],
                    ~.GenerateStreamHlsTokenResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_stream_hls_token" not in self._stubs:
            self._stubs["generate_stream_hls_token"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/GenerateStreamHlsToken",
                request_serializer=streams_service.GenerateStreamHlsTokenRequest.serialize,
                response_deserializer=streams_service.GenerateStreamHlsTokenResponse.deserialize,
            )
        return self._stubs["generate_stream_hls_token"]

    @property
    def list_events(
        self,
    ) -> Callable[
        [streams_service.ListEventsRequest], streams_service.ListEventsResponse
    ]:
        r"""Return a callable for the list events method over gRPC.

        Lists Events in a given project and location.

        Returns:
            Callable[[~.ListEventsRequest],
                    ~.ListEventsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_events" not in self._stubs:
            self._stubs["list_events"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/ListEvents",
                request_serializer=streams_service.ListEventsRequest.serialize,
                response_deserializer=streams_service.ListEventsResponse.deserialize,
            )
        return self._stubs["list_events"]

    @property
    def get_event(
        self,
    ) -> Callable[[streams_service.GetEventRequest], streams_resources.Event]:
        r"""Return a callable for the get event method over gRPC.

        Gets details of a single Event.

        Returns:
            Callable[[~.GetEventRequest],
                    ~.Event]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_event" not in self._stubs:
            self._stubs["get_event"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/GetEvent",
                request_serializer=streams_service.GetEventRequest.serialize,
                response_deserializer=streams_resources.Event.deserialize,
            )
        return self._stubs["get_event"]

    @property
    def create_event(
        self,
    ) -> Callable[[streams_service.CreateEventRequest], operations_pb2.Operation]:
        r"""Return a callable for the create event method over gRPC.

        Creates a new Event in a given project and location.

        Returns:
            Callable[[~.CreateEventRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_event" not in self._stubs:
            self._stubs["create_event"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/CreateEvent",
                request_serializer=streams_service.CreateEventRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_event"]

    @property
    def update_event(
        self,
    ) -> Callable[[streams_service.UpdateEventRequest], operations_pb2.Operation]:
        r"""Return a callable for the update event method over gRPC.

        Updates the parameters of a single Event.

        Returns:
            Callable[[~.UpdateEventRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_event" not in self._stubs:
            self._stubs["update_event"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/UpdateEvent",
                request_serializer=streams_service.UpdateEventRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_event"]

    @property
    def delete_event(
        self,
    ) -> Callable[[streams_service.DeleteEventRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete event method over gRPC.

        Deletes a single Event.

        Returns:
            Callable[[~.DeleteEventRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_event" not in self._stubs:
            self._stubs["delete_event"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/DeleteEvent",
                request_serializer=streams_service.DeleteEventRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_event"]

    @property
    def list_series(
        self,
    ) -> Callable[
        [streams_service.ListSeriesRequest], streams_service.ListSeriesResponse
    ]:
        r"""Return a callable for the list series method over gRPC.

        Lists Series in a given project and location.

        Returns:
            Callable[[~.ListSeriesRequest],
                    ~.ListSeriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_series" not in self._stubs:
            self._stubs["list_series"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/ListSeries",
                request_serializer=streams_service.ListSeriesRequest.serialize,
                response_deserializer=streams_service.ListSeriesResponse.deserialize,
            )
        return self._stubs["list_series"]

    @property
    def get_series(
        self,
    ) -> Callable[[streams_service.GetSeriesRequest], streams_resources.Series]:
        r"""Return a callable for the get series method over gRPC.

        Gets details of a single Series.

        Returns:
            Callable[[~.GetSeriesRequest],
                    ~.Series]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_series" not in self._stubs:
            self._stubs["get_series"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/GetSeries",
                request_serializer=streams_service.GetSeriesRequest.serialize,
                response_deserializer=streams_resources.Series.deserialize,
            )
        return self._stubs["get_series"]

    @property
    def create_series(
        self,
    ) -> Callable[[streams_service.CreateSeriesRequest], operations_pb2.Operation]:
        r"""Return a callable for the create series method over gRPC.

        Creates a new Series in a given project and location.

        Returns:
            Callable[[~.CreateSeriesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_series" not in self._stubs:
            self._stubs["create_series"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/CreateSeries",
                request_serializer=streams_service.CreateSeriesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_series"]

    @property
    def update_series(
        self,
    ) -> Callable[[streams_service.UpdateSeriesRequest], operations_pb2.Operation]:
        r"""Return a callable for the update series method over gRPC.

        Updates the parameters of a single Event.

        Returns:
            Callable[[~.UpdateSeriesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_series" not in self._stubs:
            self._stubs["update_series"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/UpdateSeries",
                request_serializer=streams_service.UpdateSeriesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_series"]

    @property
    def delete_series(
        self,
    ) -> Callable[[streams_service.DeleteSeriesRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete series method over gRPC.

        Deletes a single Series.

        Returns:
            Callable[[~.DeleteSeriesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_series" not in self._stubs:
            self._stubs["delete_series"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/DeleteSeries",
                request_serializer=streams_service.DeleteSeriesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_series"]

    @property
    def materialize_channel(
        self,
    ) -> Callable[
        [streams_service.MaterializeChannelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the materialize channel method over gRPC.

        Materialize a channel.

        Returns:
            Callable[[~.MaterializeChannelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "materialize_channel" not in self._stubs:
            self._stubs["materialize_channel"] = self.grpc_channel.unary_unary(
                "/google.cloud.visionai.v1.StreamsService/MaterializeChannel",
                request_serializer=streams_service.MaterializeChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["materialize_channel"]

    def close(self):
        self.grpc_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("StreamsServiceGrpcTransport",)
