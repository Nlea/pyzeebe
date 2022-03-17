import json
import logging

import grpc
from zeebe_grpc.gateway_pb2 import (
    TopologyRequest,
    TopologyResponse   
)

from pyzeebe.grpc_internals.grpc_utils import is_error_status
from pyzeebe.grpc_internals.zeebe_adapter_base import ZeebeAdapterBase
from pyzeebe.job.job import Job

logger = logging.getLogger(__name__)

class ZeebeClusterAdapter(ZeebeAdapterBase):
    async def topology(
        self
    ) -> TopologyResponse:
        try:
            return await self._gateway_stub.Topology(
                TopologyRequest()
            )


        except grpc.aio.AioRpcError as grpc_error:
            await self._handle_grpc_error(grpc_error)