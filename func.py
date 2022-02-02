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

    def launch_instance(self):
        logging.getLogger().info("inside launch compute function")
        # Initialize service client with default config file
        core_client = oci.core.ComputeClient(config={'region': self.region}, signer = self.signer)
        launch_instance_response = core_client.launch_instance(
            availability_domain="Qhab:PHX-AD-1",
            compartment_id="ocid1.compartment.oc1..aaaaaaaaievlqkktpe5yumlanr64gnzgi2vokbhrsuz2sddcjooewbqqj5ha",
            shape="VM.Standard2.8",
            create_vnic_details=oci.core.models.CreateVnicDetails(
                assign_public_ip=True,
                subnet_id="ocid1.subnet.oc1.phx.aaaaaaaa5t6wyuvglpzdw3rm6mvtgnjupv22edbxzacra7djem7asv2eufgq"

            ),
            image_id="ocid1.image.oc1.phx.aaaaaaaaqpk3kgliqneamdnkslngae5x22xf43xqglu6ijrxl32wx3noxtca"

            )
        logging.getLogger().info(str(launch_instance_response.data))




#     def fetch_ad(self,region_config,aws_region):
#         logging.getLogger().info("Inside fetch Ad info function")
#         identity_client = oci.identity.IdentityClient(config={'region': self.region}, signer = self.signer)
#         oci_compartment_id = region_config[aws_region]['oci_compartment_ocid']
#         oci_ad = region_config[aws_region]['oci_ad']
#         logging.getLogger().info("Doing pagination query")
#         availability_domains = oci.pagination.list_call_get_all_results(
#             identity_client.list_availability_domains,oci_compartment_id).data
#         return availability_domains 

        

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
        logging.getLogger().info('subnet is ' + str(aws_subnet_id))

        oci_region = 'us-phoenix-1' #Eventually this will come from the compat endpoint handeler 
        oci_sdk_handler = oci_sdk_actions(oci_region)
        oci_sdk_handler.launch_instance()
        # ad=oci_sdk_handler.fetch_ad(region_config,aws_region)
        # for i in ad:
        #     logging.getLogger().info(str(i['name']))

        # logging.getLogger().info("ivar"+str(region_config))
        return response.Response(
            ctx, 
            response_data=json.dumps({"status": "you are inside oci"}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().error("Exception" + str(error))
    