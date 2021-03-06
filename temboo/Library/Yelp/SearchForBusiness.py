# -*- coding: utf-8 -*-

###############################################################################
#
# SearchForBusiness
# Retrieves information for a given business id or name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchForBusiness(Choreography):

    """
    Create a new instance of the SearchForBusiness Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchForBusiness')


    def new_input_set(self):
        return SearchForBusinessInputSet()

    def _make_result_set(self, result, path):
        return SearchForBusinessResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForBusinessChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchForBusiness
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchForBusinessInputSet(InputSet):
        """
        Set the value of the BusinessId input for this choreography. ((conditional, string) The business id to return results for. This can be found in the URL when you're on the business page on yelp.com (i.e. "yelp-san-francisco"). This is required unless using the BusinessName input.)
        """
        def set_BusinessId(self, value):
            InputSet._set_input(self, 'BusinessId', value)

        """
        Set the value of the BusinessName input for this choreography. ((conditional, string) A term to narrow the search, such as business name. This is required unless using the BusinessId input.)
        """
        def set_BusinessName(self, value):
            InputSet._set_input(self, 'BusinessName', value)

        """
        Set the value of the City input for this choreography. ((conditional, string) The name of the city in which to search for businesses. This is required unless providing the BusinessId.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the ConsumerKey input for this choreography. ((required, string) The Consumer Key provided by Yelp.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((required, string) The Consumer Secret provided by Yelp.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, multiline) The format of the response from Yelp, either XML or JSON (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TokenSecret input for this choreography. ((required, string) The Token Secret provided by Yelp.)
        """
        def set_TokenSecret(self, value):
            InputSet._set_input(self, 'TokenSecret', value)

        """
        Set the value of the Token input for this choreography. ((required, string) The Token provided by Yelp.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the SearchForBusiness choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchForBusinessResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchForBusinessChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForBusinessResultSet(response, path)
