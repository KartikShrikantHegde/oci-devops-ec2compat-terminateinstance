# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
core_client = oci.core.ComputeClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
launch_instance_response = core_client.launch_instance(
    launch_instance_details=oci.core.models.LaunchInstanceDetails(
        availability_domain="EXAMPLE-availabilityDomain-Value",
        compartment_id="ocid1.test.oc1..<unique_ID>EXAMPLE-compartmentId-Value",
        shape="EXAMPLE-shape-Value",
        capacity_reservation_id="ocid1.test.oc1..<unique_ID>EXAMPLE-capacityReservationId-Value",
        create_vnic_details=oci.core.models.CreateVnicDetails(
            assign_public_ip=True,
            assign_private_dns_record=False,
            defined_tags={
                'EXAMPLE_KEY_v1GMl': {
                    'EXAMPLE_KEY_uJCpT': 'EXAMPLE--Value'}},
            display_name="EXAMPLE-displayName-Value",
            freeform_tags={
                'EXAMPLE_KEY_Bkw6h': 'EXAMPLE_VALUE_T601E3Jv9YvmtiHrar4j'},
            hostname_label="EXAMPLE-hostnameLabel-Value",
            nsg_ids=["EXAMPLE--Value"],
            private_ip="EXAMPLE-privateIp-Value",
            skip_source_dest_check=True,
            subnet_id="ocid1.test.oc1..<unique_ID>EXAMPLE-subnetId-Value",
            vlan_id="ocid1.test.oc1..<unique_ID>EXAMPLE-vlanId-Value"),
        dedicated_vm_host_id="ocid1.test.oc1..<unique_ID>EXAMPLE-dedicatedVmHostId-Value",
        defined_tags={
            'EXAMPLE_KEY_ZkQQX': {
                'EXAMPLE_KEY_lASAV': 'EXAMPLE--Value'}},
        display_name="EXAMPLE-displayName-Value",
        extended_metadata={
            'EXAMPLE_KEY_YiFyo': 'EXAMPLE--Value'},
        fault_domain="EXAMPLE-faultDomain-Value",
        freeform_tags={
            'EXAMPLE_KEY_lxWLC': 'EXAMPLE_VALUE_Amar21LjVTYlaieCasQ6'},
        hostname_label="EXAMPLE-hostnameLabel-Value",
        image_id="ocid1.test.oc1..<unique_ID>EXAMPLE-imageId-Value",
        ipxe_script="EXAMPLE-ipxeScript-Value",
        launch_options=oci.core.models.LaunchOptions(
            boot_volume_type="IDE",
            firmware="BIOS",
            network_type="E1000",
            remote_data_volume_type="IDE",
            is_pv_encryption_in_transit_enabled=False,
            is_consistent_volume_naming_enabled=False),
        instance_options=oci.core.models.InstanceOptions(
            are_legacy_imds_endpoints_disabled=True),
        availability_config=oci.core.models.LaunchInstanceAvailabilityConfigDetails(
            is_live_migration_preferred=False,
            recovery_action="RESTORE_INSTANCE"),
        preemptible_instance_config=oci.core.models.PreemptibleInstanceConfigDetails(
            preemption_action=oci.core.models.TerminatePreemptionAction(
                type="TERMINATE",
                preserve_boot_volume=True)),
        metadata={
            'EXAMPLE_KEY_M9sLR': 'EXAMPLE_VALUE_YVJnohGQ2zs9fw0RM4nq'},
        agent_config=oci.core.models.LaunchInstanceAgentConfigDetails(
            is_monitoring_disabled=True,
            is_management_disabled=True,
            are_all_plugins_disabled=False,
            plugins_config=[
                oci.core.models.InstanceAgentPluginConfigDetails(
                    name="EXAMPLE-name-Value",
                    desired_state="ENABLED")]),
        shape_config=oci.core.models.LaunchInstanceShapeConfigDetails(
            ocpus=1894.4413,
            memory_in_gbs=6435.6567,
            baseline_ocpu_utilization="BASELINE_1_8"),
        source_details=oci.core.models.InstanceSourceViaBootVolumeDetails(
            source_type="bootVolume",
            boot_volume_id="ocid1.test.oc1..<unique_ID>EXAMPLE-bootVolumeId-Value"),
        subnet_id="ocid1.test.oc1..<unique_ID>EXAMPLE-subnetId-Value",
        is_pv_encryption_in_transit_enabled=True,
        platform_config=oci.core.models.AmdVmLaunchInstancePlatformConfig(
            type="AMD_VM",
            is_secure_boot_enabled=True,
            is_trusted_platform_module_enabled=True,
            is_measured_boot_enabled=True)),
    opc_retry_token="EXAMPLE-opcRetryToken-Value")

# Get the data from response
print(launch_instance_response.data)