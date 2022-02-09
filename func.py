# oci-load-file-into-adw-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
from operator import contains
import os
import json
import oci
import logging
import random
import string

from fdk import response

def read_from_json_file(path):
    try:
        json_file = open(path)
        return (json.load(json_file))
    except Exception as error:
        logging.getLogger().error("Exception while reading json file" + str(error))


class oci_sdk_actions:
    def __init__(self,region):
        self.region = region
        self.signer = oci.auth.signers.get_resource_principals_signer()

    def describe_instances(self,oci_compartment_ocid,input):
        try:
            core_client = oci.core.ComputeClient(config={'region': self.region}, signer = self.signer)
            number_of_instance_ids = input.lower().count('instanceid')
            if number_of_instance_id != 1:
                return "Sorry in demo we can take only 1 ID"

        except Exception as error:
            logging.getLogger().info("Error while launching the instance" + str(error))



def handler(ctx, data: io.BytesIO=None):
    try:
        body = str(str(data.getvalue()))
        logging.getLogger().info("inputs" + str(body))
        
        # logging.getLogger().info("Invoked function with default  image")
        # instance_config = read_from_json_file("/function/instance_config.json")
        region_config =  read_from_json_file("/function/region_config.json")
        # shape_config = read_from_json_file("/function/shape_config.json")
        # image_config = read_from_json_file("/function/image_config.json")
        # subnet_config = read_from_json_file("/function/subnet_config.json")

       
        # logging.getLogger().info('subnet is ' + str(aws_subnet_id))

        oci_region = 'us-phoenix-1' #Eventually this will come from the compat endpoint handeler 
        aws_region = 'us-east-1' #Eventually get this from AWS Endpoint context value 

    
        oci_compartment_ocid = region_config[aws_region]['oci_compartment_ocid']
        
        oci_sdk_handler = oci_sdk_actions(oci_region)
        describe_instance_response = oci_sdk_handler.describe_instances(oci_compartment_ocid,body)
    
        # instance_creation_response = oci_sdk_handler.launch_instance(oci_instance_shape,oci_subnet_id,oci_image_id,oci_compartment_ocid,oci_ad_name)
        return response.Response(
            ctx, 
            response_data=json.dumps({"output": describe_instance_response}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().error("Exception" + str(error))
    