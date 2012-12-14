# -*- coding: utf-8 -*-

###############################################################################
#
# DailyUVByCity
# Retrieves EPA daily Ultraviolet (UV) Index readings in a given city.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DailyUVByCity(Choreography):

    """
    Create a new instance of the DailyUVByCity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/UVForecast/DailyUVByCity')


    def new_input_set(self):
        return DailyUVByCityInputSet()

    def _make_result_set(self, result, path):
        return DailyUVByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DailyUVByCityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DailyUVByCity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DailyUVByCityInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the DailyUVByCity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DailyUVByCityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DailyUVByCityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DailyUVByCityResultSet(response, path)
