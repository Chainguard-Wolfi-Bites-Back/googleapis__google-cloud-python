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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.bigquery_biglake_v1alpha1.types import metastore


class ListCatalogsPager:
    """A pager for iterating through ``list_catalogs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``catalogs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCatalogs`` requests and continue to iterate
    through the ``catalogs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., metastore.ListCatalogsResponse],
        request: metastore.ListCatalogsRequest,
        response: metastore.ListCatalogsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListCatalogsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[metastore.ListCatalogsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[metastore.Catalog]:
        for page in self.pages:
            yield from page.catalogs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogsAsyncPager:
    """A pager for iterating through ``list_catalogs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``catalogs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCatalogs`` requests and continue to iterate
    through the ``catalogs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[metastore.ListCatalogsResponse]],
        request: metastore.ListCatalogsRequest,
        response: metastore.ListCatalogsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListCatalogsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[metastore.ListCatalogsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[metastore.Catalog]:
        async def async_generator():
            async for page in self.pages:
                for response in page.catalogs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatabasesPager:
    """A pager for iterating through ``list_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``databases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDatabases`` requests and continue to iterate
    through the ``databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., metastore.ListDatabasesResponse],
        request: metastore.ListDatabasesRequest,
        response: metastore.ListDatabasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListDatabasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[metastore.ListDatabasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[metastore.Database]:
        for page in self.pages:
            yield from page.databases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatabasesAsyncPager:
    """A pager for iterating through ``list_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``databases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDatabases`` requests and continue to iterate
    through the ``databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[metastore.ListDatabasesResponse]],
        request: metastore.ListDatabasesRequest,
        response: metastore.ListDatabasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListDatabasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[metastore.ListDatabasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[metastore.Database]:
        async def async_generator():
            async for page in self.pages:
                for response in page.databases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTablesPager:
    """A pager for iterating through ``list_tables`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListTablesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tables`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTables`` requests and continue to iterate
    through the ``tables`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListTablesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., metastore.ListTablesResponse],
        request: metastore.ListTablesRequest,
        response: metastore.ListTablesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListTablesRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListTablesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListTablesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[metastore.ListTablesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[metastore.Table]:
        for page in self.pages:
            yield from page.tables

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTablesAsyncPager:
    """A pager for iterating through ``list_tables`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListTablesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tables`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTables`` requests and continue to iterate
    through the ``tables`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListTablesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[metastore.ListTablesResponse]],
        request: metastore.ListTablesRequest,
        response: metastore.ListTablesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListTablesRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListTablesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListTablesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[metastore.ListTablesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[metastore.Table]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tables:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLocksPager:
    """A pager for iterating through ``list_locks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListLocksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``locks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLocks`` requests and continue to iterate
    through the ``locks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListLocksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., metastore.ListLocksResponse],
        request: metastore.ListLocksRequest,
        response: metastore.ListLocksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListLocksRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListLocksResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListLocksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[metastore.ListLocksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[metastore.Lock]:
        for page in self.pages:
            yield from page.locks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLocksAsyncPager:
    """A pager for iterating through ``list_locks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListLocksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``locks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLocks`` requests and continue to iterate
    through the ``locks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_biglake_v1alpha1.types.ListLocksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[metastore.ListLocksResponse]],
        request: metastore.ListLocksRequest,
        response: metastore.ListLocksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_biglake_v1alpha1.types.ListLocksRequest):
                The initial request object.
            response (google.cloud.bigquery_biglake_v1alpha1.types.ListLocksResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metastore.ListLocksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[metastore.ListLocksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[metastore.Lock]:
        async def async_generator():
            async for page in self.pages:
                for response in page.locks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
