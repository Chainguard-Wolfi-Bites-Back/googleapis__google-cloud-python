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

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bare_metal_solution_v2.types import common

__protobuf__ = proto.module(
    package="google.cloud.baremetalsolution.v2",
    manifest={
        "Volume",
        "GetVolumeRequest",
        "ListVolumesRequest",
        "ListVolumesResponse",
        "UpdateVolumeRequest",
        "RenameVolumeRequest",
        "EvictVolumeRequest",
        "ResizeVolumeRequest",
    },
)


class Volume(proto.Message):
    r"""A storage volume.

    Attributes:
        name (str):
            Output only. The resource name of this ``Volume``. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. Format:
            ``projects/{project}/locations/{location}/volumes/{volume}``
        id (str):
            An identifier for the ``Volume``, generated by the backend.
        storage_type (google.cloud.bare_metal_solution_v2.types.Volume.StorageType):
            The storage type for this volume.
        state (google.cloud.bare_metal_solution_v2.types.Volume.State):
            The state of this storage volume.
        requested_size_gib (int):
            The requested size of this storage volume, in
            GiB.
        originally_requested_size_gib (int):
            Originally requested size, in GiB.
        current_size_gib (int):
            The current size of this storage volume, in
            GiB, including space reserved for snapshots.
            This size might be different than the requested
            size if the storage volume has been configured
            with auto grow or auto shrink.
        emergency_size_gib (int):
            Additional emergency size that was requested for this
            Volume, in GiB. current_size_gib includes this value.
        max_size_gib (int):
            Maximum size volume can be expanded to in
            case of evergency, in GiB.
        auto_grown_size_gib (int):
            The size, in GiB, that this storage volume
            has expanded as a result of an auto grow policy.
            In the absence of auto-grow, the value is 0.
        remaining_space_gib (int):
            The space remaining in the storage volume for
            new LUNs, in GiB, excluding space reserved for
            snapshots.
        snapshot_reservation_detail (google.cloud.bare_metal_solution_v2.types.Volume.SnapshotReservationDetail):
            Details about snapshot space reservation and
            usage on the storage volume.
        snapshot_auto_delete_behavior (google.cloud.bare_metal_solution_v2.types.Volume.SnapshotAutoDeleteBehavior):
            The behavior to use when snapshot reserved
            space is full.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        snapshot_enabled (bool):
            Whether snapshots are enabled.
        pod (str):
            Immutable. Pod name.
        protocol (google.cloud.bare_metal_solution_v2.types.Volume.Protocol):
            Output only. Storage protocol for the Volume.
        boot_volume (bool):
            Output only. Whether this volume is a boot
            volume. A boot volume is one which contains a
            boot LUN.
        performance_tier (google.cloud.bare_metal_solution_v2.types.VolumePerformanceTier):
            Immutable. Performance tier of the Volume.
            Default is SHARED.
        notes (str):
            Input only. User-specified notes for new
            Volume. Used to provision Volumes that require
            manual intervention.
        workload_profile (google.cloud.bare_metal_solution_v2.types.Volume.WorkloadProfile):
            The workload profile for the volume.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time after which volume will be
            fully deleted. It is filled only for volumes in
            COOLOFF state.
        instances (MutableSequence[str]):
            Output only. Instances this Volume is
            attached to. This field is set only in Get
            requests.
        attached (bool):
            Output only. Is the Volume attached at at least one
            instance. This field is a lightweight counterpart of
            ``instances`` field. It is filled in List responses as well.
    """

    class StorageType(proto.Enum):
        r"""The storage type for a volume.

        Values:
            STORAGE_TYPE_UNSPECIFIED (0):
                The storage type for this volume is unknown.
            SSD (1):
                The storage type for this volume is SSD.
            HDD (2):
                This storage type for this volume is HDD.
        """
        STORAGE_TYPE_UNSPECIFIED = 0
        SSD = 1
        HDD = 2

    class State(proto.Enum):
        r"""The possible states for a storage volume.

        Values:
            STATE_UNSPECIFIED (0):
                The storage volume is in an unknown state.
            CREATING (1):
                The storage volume is being created.
            READY (2):
                The storage volume is ready for use.
            DELETING (3):
                The storage volume has been requested to be
                deleted.
            UPDATING (4):
                The storage volume is being updated.
            COOL_OFF (5):
                The storage volume is in cool off state. It will be deleted
                after ``expire_time``.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4
        COOL_OFF = 5

    class SnapshotAutoDeleteBehavior(proto.Enum):
        r"""The kinds of auto delete behavior to use when snapshot
        reserved space is full.

        Values:
            SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED (0):
                The unspecified behavior.
            DISABLED (1):
                Don't delete any snapshots. This disables new
                snapshot creation, as long as the snapshot
                reserved space is full.
            OLDEST_FIRST (2):
                Delete the oldest snapshots first.
            NEWEST_FIRST (3):
                Delete the newest snapshots first.
        """
        SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED = 0
        DISABLED = 1
        OLDEST_FIRST = 2
        NEWEST_FIRST = 3

    class Protocol(proto.Enum):
        r"""Storage protocol.

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Value is not specified.
            FIBRE_CHANNEL (1):
                Fibre Channel protocol.
            NFS (2):
                NFS protocol means Volume is a NFS Share
                volume. Such volumes cannot be manipulated via
                Volumes API.
        """
        PROTOCOL_UNSPECIFIED = 0
        FIBRE_CHANNEL = 1
        NFS = 2

    class WorkloadProfile(proto.Enum):
        r"""The possible values for a workload profile.

        Values:
            WORKLOAD_PROFILE_UNSPECIFIED (0):
                The workload profile is in an unknown state.
            GENERIC (1):
                The workload profile is generic.
            HANA (2):
                The workload profile is hana.
        """
        WORKLOAD_PROFILE_UNSPECIFIED = 0
        GENERIC = 1
        HANA = 2

    class SnapshotReservationDetail(proto.Message):
        r"""Details about snapshot space reservation and usage on the
        storage volume.

        Attributes:
            reserved_space_gib (int):
                The space on this storage volume reserved for
                snapshots, shown in GiB.
            reserved_space_used_percent (int):
                The percent of snapshot space on this storage
                volume actually being used by the snapshot
                copies. This value might be higher than 100% if
                the snapshot copies have overflowed into the
                data portion of the storage volume.
            reserved_space_remaining_gib (int):
                The amount, in GiB, of available space in
                this storage volume's reserved snapshot space.
            reserved_space_percent (int):
                Percent of the total Volume size reserved for snapshot
                copies. Enabling snapshots requires reserving 20% or more of
                the storage volume space for snapshots. Maximum reserved
                space for snapshots is 40%. Setting this field will
                effectively set snapshot_enabled to true.
        """

        reserved_space_gib: int = proto.Field(
            proto.INT64,
            number=1,
        )
        reserved_space_used_percent: int = proto.Field(
            proto.INT32,
            number=2,
        )
        reserved_space_remaining_gib: int = proto.Field(
            proto.INT64,
            number=3,
        )
        reserved_space_percent: int = proto.Field(
            proto.INT32,
            number=4,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    storage_type: StorageType = proto.Field(
        proto.ENUM,
        number=2,
        enum=StorageType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    requested_size_gib: int = proto.Field(
        proto.INT64,
        number=4,
    )
    originally_requested_size_gib: int = proto.Field(
        proto.INT64,
        number=16,
    )
    current_size_gib: int = proto.Field(
        proto.INT64,
        number=5,
    )
    emergency_size_gib: int = proto.Field(
        proto.INT64,
        number=14,
    )
    max_size_gib: int = proto.Field(
        proto.INT64,
        number=17,
    )
    auto_grown_size_gib: int = proto.Field(
        proto.INT64,
        number=6,
    )
    remaining_space_gib: int = proto.Field(
        proto.INT64,
        number=7,
    )
    snapshot_reservation_detail: SnapshotReservationDetail = proto.Field(
        proto.MESSAGE,
        number=8,
        message=SnapshotReservationDetail,
    )
    snapshot_auto_delete_behavior: SnapshotAutoDeleteBehavior = proto.Field(
        proto.ENUM,
        number=9,
        enum=SnapshotAutoDeleteBehavior,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    snapshot_enabled: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    pod: str = proto.Field(
        proto.STRING,
        number=15,
    )
    protocol: Protocol = proto.Field(
        proto.ENUM,
        number=18,
        enum=Protocol,
    )
    boot_volume: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    performance_tier: common.VolumePerformanceTier = proto.Field(
        proto.ENUM,
        number=20,
        enum=common.VolumePerformanceTier,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=21,
    )
    workload_profile: WorkloadProfile = proto.Field(
        proto.ENUM,
        number=22,
        enum=WorkloadProfile,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    instances: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=25,
    )
    attached: bool = proto.Field(
        proto.BOOL,
        number=26,
    )


class GetVolumeRequest(proto.Message):
    r"""Message for requesting storage volume information.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVolumesRequest(proto.Message):
    r"""Message for requesting a list of storage volumes.

    Attributes:
        parent (str):
            Required. Parent value for
            ListVolumesRequest.
        page_size (int):
            Requested page size. The server might return
            fewer items than requested. If unspecified,
            server will pick an appropriate default.
        page_token (str):
            A token identifying a page of results from
            the server.
        filter (str):
            List filter.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListVolumesResponse(proto.Message):
    r"""Response message containing the list of storage volumes.

    Attributes:
        volumes (MutableSequence[google.cloud.bare_metal_solution_v2.types.Volume]):
            The list of storage volumes.
        next_page_token (str):
            A token identifying a page of results from
            the server.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    volumes: MutableSequence["Volume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Volume",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateVolumeRequest(proto.Message):
    r"""Message for updating a volume.

    Attributes:
        volume (google.cloud.bare_metal_solution_v2.types.Volume):
            Required. The volume to update.

            The ``name`` field is used to identify the volume to update.
            Format:
            projects/{project}/locations/{location}/volumes/{volume}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update.
            The only currently supported fields are:

              'labels'
    """

    volume: "Volume" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Volume",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class RenameVolumeRequest(proto.Message):
    r"""Message requesting rename of a server.

    Attributes:
        name (str):
            Required. The ``name`` field is used to identify the volume.
            Format:
            projects/{project}/locations/{location}/volumes/{volume}
        new_volume_id (str):
            Required. The new ``id`` of the volume.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_volume_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EvictVolumeRequest(proto.Message):
    r"""Request for skip volume cooloff and delete it.

    Attributes:
        name (str):
            Required. The name of the Volume.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResizeVolumeRequest(proto.Message):
    r"""Request for emergency resize Volume.

    Attributes:
        volume (str):
            Required. Volume to resize.
        size_gib (int):
            New Volume size, in GiB.
    """

    volume: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gib: int = proto.Field(
        proto.INT64,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
