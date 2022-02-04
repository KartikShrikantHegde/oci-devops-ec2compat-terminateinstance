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

    def launch_instance(self,oci_instance_shape,oci_subnet_id,oci_image_id,oci_compartment_ocid,oci_ad_name):
        try:
            associate_public_ip_for_oci=True
            name_random = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(17))
            oci_instance_display_name = f'i-{name_random}'
            logging.getLogger().info("inside launch compute function")
            # Initialize service client with default config file
            core_client = oci.core.ComputeClient(config={'region': self.region}, signer = self.signer)
            launch_instance_response = core_client.launch_instance(
                launch_instance_details=oci.core.models.LaunchInstanceDetails(
                availability_domain=oci_ad_name, # This will be dynamically fetch from fetch ad function.
                compartment_id=oci_compartment_ocid, # This will be  from a map 
                shape=oci_instance_shape,
                display_name=oci_instance_display_name,
                create_vnic_details=oci.core.models.CreateVnicDetails(
                    assign_public_ip=associate_public_ip_for_oci,
                    subnet_id=oci_subnet_id

                ),
                image_id=oci_image_id

                ))
            return launch_instance_response
        except Exception as error:
            logging.getLogger().info("Error while launching the instance" + str(error))


    def fetch_ad(self,oci_compartment_ocid,aws_region):
        logging.getLogger().info("Inside fetch Ad info function")
        identity_client = oci.identity.IdentityClient(config={'region': self.region}, signer = self.signer)
        logging.getLogger().info("Doing pagination query")
        availability_domains = oci.pagination.list_call_get_all_results(
            identity_client.list_availability_domains,oci_compartment_ocid).data

        return availability_domains 

        

def handler(ctx, data: io.BytesIO=None):
    try:
        body = str(str(data.getvalue()))
        logging.getLogger().info("inputs" + str(body))
        logging.getLogger().info("Invoked function with default  image")
        instance_config = read_from_json_file("/function/instance_config.json")
        region_config =  read_from_json_file("/function/region_config.json")
        shape_config = read_from_json_file("/function/shape_config.json")
        image_config = read_from_json_file("/function/image_config.json")
        subnet_config = read_from_json_file("/function/subnet_config.json")

        aws_image_id = body.split('ImageId=')[1].split('&')[0]
        aws_subnet_id = body.split('SubnetId=')[1].split('&')[0]
        aws_shape_name = body.split('InstanceType=')[1].split('&')[0]
       
        logging.getLogger().info('subnet is ' + str(aws_subnet_id))

        oci_region = 'us-phoenix-1' #Eventually this will come from the compat endpoint handeler 
        aws_region = 'us-east-1' #Eventually get this from AWS Endpoint context value 

        oci_instance_shape = shape_config[aws_shape_name]
        oci_subnet_id = subnet_config[aws_subnet_id]
        oci_image_id = image_config[aws_image_id]
        oci_compartment_ocid = region_config[aws_region]['oci_compartment_ocid']
        oci_instance_ad_count = int(region_config[aws_region]['oci_ad'].split('-')[-1]) -1
        
        oci_sdk_handler = oci_sdk_actions(oci_region)
        ad_info=oci_sdk_handler.fetch_ad(oci_compartment_ocid,aws_region)
        logging.getLogger().info("Proceeding with AD info" + str(ad_info[oci_instance_ad_count]))
        oci_ad_name='Qhab:PHX-AD-1' #This will be from the map,token.
        instance_creation_response = oci_sdk_handler.launch_instance(oci_instance_shape,oci_subnet_id,oci_image_id,oci_compartment_ocid,oci_ad_name)
        return response.Response(
            ctx, 
            response_data=json.dumps({"output": str(instance_creation_response.data)}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().error("Exception" + str(error))
    