# oci-load-file-into-adw-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import os
import json
import oci
import logging

from fdk import response

def handler(ctx, data: io.BytesIO=None):
    try:
        body = json.loads(data.getvalue())
        logging.getLogger().info("inputs" + str(body))
        logging.getLogger().info("Invoked function with default  image")
        json_file = open("/function/instanceconfig.json")
        ivar = json.load(json_file)
        logging.getLogger().info("ivar"+ivar)
        return response.Response(
            ctx, 
            response_data=json.dumps({"status": "Hello World! with DefaultImage"}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().error("Exception" + str(error))
    