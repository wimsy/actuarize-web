# -*- coding: utf-8 -*-

###############################################################################
#
# Civic
# Retrieves a host of information about the district and representatives of a specified location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Civic(Choreography):

    """
    Create a new instance of the Civic Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GoodCitizen/Civic')


    def new_input_set(self):
        return CivicInputSet()

    def _make_result_set(self, result, path):
        return CivicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CivicChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Civic
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CivicInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((optional, json) The JSON dictionary for the Sulight Labs credentials required to operate this choreo. LittleSis credentials are optional. See docs for the format of this input.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate of your location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Set the number of records to return for the bills, votes, and relationships of each legislator. Defaults to 5.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate of your locaion.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the Civic choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CivicResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from the Civic Choreo.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CivicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CivicResultSet(response, path)
