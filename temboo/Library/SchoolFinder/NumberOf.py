# -*- coding: utf-8 -*-

###############################################################################
#
# NumberOf
# Returns the total number of schools, the number of schools at each level (elementary, middle, high) and the number of each type of school (public, private, charter) in a given city. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class NumberOf(Choreography):

    """
    Create a new instance of the NumberOf Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/NumberOf')


    def new_input_set(self):
        return NumberOfInputSet()

    def _make_result_set(self, result, path):
        return NumberOfResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NumberOfChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the NumberOf
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class NumberOfInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your School Finder API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((required, string) The name of a city. City requests must also be accompanied by the corresponding state parameter.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((required, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the NumberOf choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class NumberOfResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Education.com.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class NumberOfChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NumberOfResultSet(response, path)
