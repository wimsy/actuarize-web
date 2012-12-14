# -*- coding: utf-8 -*-

###############################################################################
#
# CreateServerXMLInput
# Creates a RightScale server instance using a given XML template.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateServerXMLInput(Choreography):

    """
    Create a new instance of the CreateServerXMLInput Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RightScale/CreateServerXMLInput')


    def new_input_set(self):
        return CreateServerXMLInputInputSet()

    def _make_result_set(self, result, path):
        return CreateServerXMLInputResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateServerXMLInputChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateServerXMLInput
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateServerXMLInputInputSet(InputSet):
        """
        Set the value of the ServerParameters input for this choreography. ((required, xml) The XML file containing the required parameters for the server creation. See documentation for XML schema.)
        """
        def set_ServerParameters(self, value):
            InputSet._set_input(self, 'ServerParameters', value)

        """
        Set the value of the ARIImage input for this choreography. ((required, string) The URL to the ARI Image.)
        """
        def set_ARIImage(self, value):
            InputSet._set_input(self, 'ARIImage', value)

        """
        Set the value of the AccountID input for this choreography. ((required, integer) The Account ID obtained from RightScale.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the CloudID input for this choreography. ((required, integer) The cloud region identifier. If undefined, the default is: 1 (us-east).)
        """
        def set_CloudID(self, value):
            InputSet._set_input(self, 'CloudID', value)

        """
        Set the value of the EC2AvailabilityZone input for this choreography. ((optional, any) The  EC2 availablity zone, for example: us-east-1a, or any.  Do not set, if also passing the vpc_subnet_href parameter.)
        """
        def set_EC2AvailabilityZone(self, value):
            InputSet._set_input(self, 'EC2AvailabilityZone', value)

        """
        Set the value of the EC2Image input for this choreography. ((required, string) The URL to AMI image.)
        """
        def set_EC2Image(self, value):
            InputSet._set_input(self, 'EC2Image', value)

        """
        Set the value of the EC2SSHKeyHref input for this choreography. ((optional, any) The URL to the SSH Key.)
        """
        def set_EC2SSHKeyHref(self, value):
            InputSet._set_input(self, 'EC2SSHKeyHref', value)

        """
        Set the value of the EC2SecurityGroupsHref input for this choreography. ((optional, any) The URL(s) to security group(s). Do not set, if also passing the vpc_subnet_href parameter.)
        """
        def set_EC2SecurityGroupsHref(self, value):
            InputSet._set_input(self, 'EC2SecurityGroupsHref', value)

        """
        Set the value of the InstanceType input for this choreography. ((optional, any) The AWS instance type: small, medium, etc.)
        """
        def set_InstanceType(self, value):
            InputSet._set_input(self, 'InstanceType', value)

        """
        Set the value of the MaxSpotPrice input for this choreography. ((required, integer) The maximum price (a dollar value) dollars) per hour for the spot server.)
        """
        def set_MaxSpotPrice(self, value):
            InputSet._set_input(self, 'MaxSpotPrice', value)

        """
        Set the value of the Password input for this choreography. ((required, password) The RightScale account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Pricing input for this choreography. ((required, string) AWS pricing.  Specify on_demand, or spot.)
        """
        def set_Pricing(self, value):
            InputSet._set_input(self, 'Pricing', value)

        """
        Set the value of the ServerDeployment input for this choreography. ((optional, any) The URL of the deployment that this server wil be added to.)
        """
        def set_ServerDeployment(self, value):
            InputSet._set_input(self, 'ServerDeployment', value)

        """
        Set the value of the ServerNickname input for this choreography. ((optional, any) The nickname for the server being created.)
        """
        def set_ServerNickname(self, value):
            InputSet._set_input(self, 'ServerNickname', value)

        """
        Set the value of the ServerTemplate input for this choreography. ((optional, any) The URL to a server template.)
        """
        def set_ServerTemplate(self, value):
            InputSet._set_input(self, 'ServerTemplate', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The RightScale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the VPCSubnet input for this choreography. ((required, string) The href to the VPC subnet)
        """
        def set_VPCSubnet(self, value):
            InputSet._set_input(self, 'VPCSubnet', value)


"""
A ResultSet with methods tailored to the values returned by the CreateServerXMLInput choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateServerXMLInputResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateServerXMLInputChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateServerXMLInputResultSet(response, path)
