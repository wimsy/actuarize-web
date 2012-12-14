# -*- coding: utf-8 -*-

###############################################################################
#
# GetTestRating
# Returns the Education.com TestRating for a single school or schools within a city or zip code. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTestRating(Choreography):

    """
    Create a new instance of the GetTestRating Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/GetTestRating')


    def new_input_set(self):
        return GetTestRatingInputSet()

    def _make_result_set(self, result, path):
        return GetTestRatingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTestRatingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTestRating
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTestRatingInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your School Finder API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((conditional, string) The name of a city. Must also be accompanied by the corresponding state parameter.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the NCES input for this choreography. ((conditional, string) The National Center for Education Statistics (NCES) id of the school.)
        """
        def set_NCES(self, value):
            InputSet._set_input(self, 'NCES', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SchoolID input for this choreography. ((conditional, string) The Education.com id of the school you want to find.)
        """
        def set_SchoolID(self, value):
            InputSet._set_input(self, 'SchoolID', value)

        """
        Set the value of the State input for this choreography. ((conditional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((conditional, integer) A five digit US postal code.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the GetTestRating choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTestRatingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Education.com.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTestRatingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTestRatingResultSet(response, path)
