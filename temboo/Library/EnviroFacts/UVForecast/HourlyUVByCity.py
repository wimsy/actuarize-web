# -*- coding: utf-8 -*-

###############################################################################
#
# HourlyUVByCity
# Retrieves EPA hourly Ultraviolet (UV) Index readings in a given city. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class HourlyUVByCity(Choreography):

    """
    Create a new instance of the HourlyUVByCity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/UVForecast/HourlyUVByCity')


    def new_input_set(self):
        return HourlyUVByCityInputSet()

    def _make_result_set(self, result, path):
        return HourlyUVByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HourlyUVByCityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the HourlyUVByCity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class HourlyUVByCityInputSet(InputSet):
        """
        Set the value of the City input for this choreography. ((required, string) A valid City Name in the United States.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Results can be retrieved in either JSON or XML. Defaults to XML.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the State input for this choreography. ((required, string) The abbreviation of the state that the city resides in.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the HourlyUVByCity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class HourlyUVByCityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class HourlyUVByCityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HourlyUVByCityResultSet(response, path)
