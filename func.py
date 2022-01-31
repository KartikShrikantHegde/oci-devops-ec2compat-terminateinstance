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

def read_from_json_file(path):
    try:
        json_file = open(path)
        return (json.load(json_file))
    except Exception as error:
        logging.getLogger().error("Exception while reading json file" + str(error))


def handler(ctx, data: io.BytesIO=None):
    try:
        body = json.loads(data.getvalue())
        logging.getLogger().info("inputs" + str(body))
        logging.getLogger().info("Invoked function with default  image")
        instance_config = read_from_json_file("/function/instanceconfig.json")
        region_config =  read_from_json_file("/function/regionconfig.json")
        aws_region = body['Region']
        
        logging.getLogger().info("ivar"+str(region_config))
        return response.Response(
            ctx, 
            response_data=json.dumps({"status": "Hello World! with DefaultImage"}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().error("Exception" + str(error))
    