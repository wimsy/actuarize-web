# -*- coding: utf-8 -*-

###############################################################################
#
# DailyUVByZipCode
# Retrieves EPA daily Ultraviolet (UV) Index readings in a given zip code. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DailyUVByZipCode(Choreography):

    """
    Create a new instance of the DailyUVByZipCode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/UVForecast/DailyUVByZipCode')


    def new_input_set(self):
        return DailyUVByZipCodeInputSet()

    def _make_result_set(self, result, path):
        return DailyUVByZipCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DailyUVByZipCodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DailyUVByZipCode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DailyUVByZipCodeInputSet(InputSet):
        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Results can be retrieved in either JSON or XML. Defaults to XML.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Zip input for this choreography. ((required, integer) A valid United States Postal Service (USPS) ZIP Code or Postal Code.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the DailyUVByZipCode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DailyUVByZipCodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DailyUVByZipCodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DailyUVByZipCodeResultSet(response, path)
