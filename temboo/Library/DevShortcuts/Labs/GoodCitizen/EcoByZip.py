# -*- coding: utf-8 -*-

###############################################################################
#
# EcoByZip
# Returns a host of eco-conscious environmental information for a specified location based on zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EcoByZip(Choreography):

    """
    Create a new instance of the EcoByZip Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GoodCitizen/EcoByZip')


    def new_input_set(self):
        return EcoByZipInputSet()

    def _make_result_set(self, result, path):
        return EcoByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EcoByZipChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EcoByZip
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EcoByZipInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((optional, string) A JSON dictionary containing credentials for Genability. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of facility records to search for in the Envirofacts database.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Zip input for this choreography. ((required, integer) The zip code for the user's current location.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the EcoByZip choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EcoByZipResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from the Eco Choreo.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EcoByZipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EcoByZipResultSet(response, path)
