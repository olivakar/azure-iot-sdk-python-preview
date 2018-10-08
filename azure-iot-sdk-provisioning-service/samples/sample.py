# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

from azure.iot.sdk.provisioning.service import ProvisioningServiceClient
from azure.iot.sdk.provisioning.service.models import (BulkEnrollmentOperation, IndividualEnrollment, AttestationMechanism, TpmAttestation, QuerySpecification)

service_string = "[Service Connection String]"
ek = "[Endorsement Key]"

client = ProvisioningServiceClient(connection_string=service_string)

#Create Individual Enrollment with TPM
am = AttestationMechanism.create_with_tpm(endorsement_key=ek)
ie = IndividualEnrollment(registration_id="reg-id", attestation=am)
ie = client.create_or_update_individual_enrollment(id=ie.registration_id, enrollment=ie) #returns like a get operation

#Update Individual Enrollment
ie.device_id = "dev-id"
ie = client.create_or_update_individual_enrollment(id=ie.registration_id, enrollment=ie)

#Delete Individual Enrollmet
client.delete_individual_enrollment(id=ie.registration_id)

#Bulk Create
new_enrollments = []
for i in range(0, 10):
    new_am = AttestationMechanism.create_with_tpm(endorsement_key=ek)
    new_ie = IndividualEnrollment(registration_id=("id-" + str(i)), attestation=new_am)
    new_enrollments.append(new_ie)
bulk_op = BulkEnrollmentOperation(enrollments=new_enrollments, mode="create")
client.run_bulk_enrollment_operation(bulk_operation=bulk_op)

#Query Results
results = []
qs = QuerySpecification(query="*")
cont = ""
while cont != None:
    qrr = client.query_individual_enrollments(query_specification=qs, x_ms_max_item_count=5, x_ms_continuation=cont, raw=True)
    results.extend(qrr.output)
    cont = qrr.headers.get("x-ms-continuation", None)

#Bulk Delete
bulk_op.mode = "delete"
client.run_bulk_enrollment_operation(bulk_operation=bulk_op)