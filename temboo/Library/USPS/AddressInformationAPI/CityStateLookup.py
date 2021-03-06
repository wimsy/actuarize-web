# -*- coding: utf-8 -*-

###############################################################################
#
# CityStateLookup
# Lookup city and state using incomplete address information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CityStateLookup(Choreography):

    """
    Create a new instance of the CityStateLookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/USPS/AddressInformationAPI/CityStateLookup')


    def new_input_set(self):
        return CityStateLookupInputSet()

    def _make_result_set(self, result, path):
        return CityStateLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CityStateLookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CityStateLookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CityStateLookupInputSet(InputSet):
        """
        Set the value of the Endpoint input for this choreography. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((required, password) The password assigned by USPS)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserId input for this choreography. ((required, string) Alphanumeric ID assigned by USPS)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)

        """
        Set the value of the Zip input for this choreography. ((required, integer) Maximum characters allowed: 5)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the CityStateLookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CityStateLookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from USPS Web Service)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CityStateLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CityStateLookupResultSet(response, path)
