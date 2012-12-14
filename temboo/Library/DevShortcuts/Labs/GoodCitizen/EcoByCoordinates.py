# -*- coding: utf-8 -*-

###############################################################################
#
# EcoByCoordinates
# Returns a host of eco-conscious environmental information for a specified location based on Lattitude and Longitude inputs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EcoByCoordinates(Choreography):

    """
    Create a new instance of the EcoByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GoodCitizen/EcoByCoordinates')


    def new_input_set(self):
        return EcoByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return EcoByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EcoByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EcoByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EcoByCoordinatesInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((optional, string) A JSON dictionary containing credentials for Genability. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate for the user's current location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of facility records to search for in the Envirofacts database.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate for the user's current location.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the EcoByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EcoByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from the Eco Choreo.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EcoByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EcoByCoordinatesResultSet(response, path)
