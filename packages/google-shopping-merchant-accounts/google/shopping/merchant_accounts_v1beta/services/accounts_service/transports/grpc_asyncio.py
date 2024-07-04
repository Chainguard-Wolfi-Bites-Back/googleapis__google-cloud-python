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
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.shopping.merchant_accounts_v1beta.types import accounts

from .base import DEFAULT_CLIENT_INFO, AccountsServiceTransport
from .grpc import AccountsServiceGrpcTransport


class AccountsServiceGrpcAsyncIOTransport(AccountsServiceTransport):
    """gRPC AsyncIO backend transport for AccountsService.

    Service to support Accounts API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "merchantapi.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "merchantapi.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = None,
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
                 The hostname to connect to (default: 'merchantapi.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
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
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, aio.Channel):
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

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def get_account(
        self,
    ) -> Callable[[accounts.GetAccountRequest], Awaitable[accounts.Account]]:
        r"""Return a callable for the get account method over gRPC.

        Retrieves an account from your Merchant Center
        account. After inserting, updating, or deleting an
        account, it may take several minutes before changes take
        effect.

        Returns:
            Callable[[~.GetAccountRequest],
                    Awaitable[~.Account]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_account" not in self._stubs:
            self._stubs["get_account"] = self.grpc_channel.unary_unary(
                "/google.shopping.merchant.accounts.v1beta.AccountsService/GetAccount",
                request_serializer=accounts.GetAccountRequest.serialize,
                response_deserializer=accounts.Account.deserialize,
            )
        return self._stubs["get_account"]

    @property
    def create_and_configure_account(
        self,
    ) -> Callable[
        [accounts.CreateAndConfigureAccountRequest], Awaitable[accounts.Account]
    ]:
        r"""Return a callable for the create and configure account method over gRPC.

        Creates a standalone Merchant Center account with
        additional configuration. Adds the user that makes the
        request as an admin for the new account.

        Returns:
            Callable[[~.CreateAndConfigureAccountRequest],
                    Awaitable[~.Account]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_and_configure_account" not in self._stubs:
            self._stubs["create_and_configure_account"] = self.grpc_channel.unary_unary(
                "/google.shopping.merchant.accounts.v1beta.AccountsService/CreateAndConfigureAccount",
                request_serializer=accounts.CreateAndConfigureAccountRequest.serialize,
                response_deserializer=accounts.Account.deserialize,
            )
        return self._stubs["create_and_configure_account"]

    @property
    def delete_account(
        self,
    ) -> Callable[[accounts.DeleteAccountRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete account method over gRPC.

        Deletes the specified account regardless of its type:
        standalone, MCA or sub-account. Deleting an MCA leads to
        the deletion of all of its sub-accounts. Executing this
        method requires admin access.

        Returns:
            Callable[[~.DeleteAccountRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_account" not in self._stubs:
            self._stubs["delete_account"] = self.grpc_channel.unary_unary(
                "/google.shopping.merchant.accounts.v1beta.AccountsService/DeleteAccount",
                request_serializer=accounts.DeleteAccountRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_account"]

    @property
    def update_account(
        self,
    ) -> Callable[[accounts.UpdateAccountRequest], Awaitable[accounts.Account]]:
        r"""Return a callable for the update account method over gRPC.

        Updates an account regardless of its type:
        standalone, MCA or sub-account. Executing this method
        requires admin access.

        Returns:
            Callable[[~.UpdateAccountRequest],
                    Awaitable[~.Account]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_account" not in self._stubs:
            self._stubs["update_account"] = self.grpc_channel.unary_unary(
                "/google.shopping.merchant.accounts.v1beta.AccountsService/UpdateAccount",
                request_serializer=accounts.UpdateAccountRequest.serialize,
                response_deserializer=accounts.Account.deserialize,
            )
        return self._stubs["update_account"]

    @property
    def list_accounts(
        self,
    ) -> Callable[
        [accounts.ListAccountsRequest], Awaitable[accounts.ListAccountsResponse]
    ]:
        r"""Return a callable for the list accounts method over gRPC.

        Lists accounts accessible to the calling user and
        matching the constraints of the request such as page
        size or filters. This is not just listing the
        sub-accounts of an MCA, but all accounts the calling
        user has access to including other MCAs, linked
        accounts, standalone accounts and so on.

        Returns:
            Callable[[~.ListAccountsRequest],
                    Awaitable[~.ListAccountsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_accounts" not in self._stubs:
            self._stubs["list_accounts"] = self.grpc_channel.unary_unary(
                "/google.shopping.merchant.accounts.v1beta.AccountsService/ListAccounts",
                request_serializer=accounts.ListAccountsRequest.serialize,
                response_deserializer=accounts.ListAccountsResponse.deserialize,
            )
        return self._stubs["list_accounts"]

    @property
    def list_sub_accounts(
        self,
    ) -> Callable[
        [accounts.ListSubAccountsRequest], Awaitable[accounts.ListSubAccountsResponse]
    ]:
        r"""Return a callable for the list sub accounts method over gRPC.

        List all sub-accounts for a given multi client account. This is
        a convenience wrapper for the more powerful ``ListAccounts``
        method. This method will produce the same results as calling
        ``ListsAccounts`` with the following filter:
        ``relationship(providerId={parent} AND service(type="ACCOUNT_AGGREGATION"))``

        Returns:
            Callable[[~.ListSubAccountsRequest],
                    Awaitable[~.ListSubAccountsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sub_accounts" not in self._stubs:
            self._stubs["list_sub_accounts"] = self.grpc_channel.unary_unary(
                "/google.shopping.merchant.accounts.v1beta.AccountsService/ListSubAccounts",
                request_serializer=accounts.ListSubAccountsRequest.serialize,
                response_deserializer=accounts.ListSubAccountsResponse.deserialize,
            )
        return self._stubs["list_sub_accounts"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_account: gapic_v1.method_async.wrap_method(
                self.get_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_and_configure_account: gapic_v1.method_async.wrap_method(
                self.create_and_configure_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_account: gapic_v1.method_async.wrap_method(
                self.delete_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_account: gapic_v1.method_async.wrap_method(
                self.update_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_accounts: gapic_v1.method_async.wrap_method(
                self.list_accounts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sub_accounts: gapic_v1.method_async.wrap_method(
                self.list_sub_accounts,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        return self.grpc_channel.close()


__all__ = ("AccountsServiceGrpcAsyncIOTransport",)
