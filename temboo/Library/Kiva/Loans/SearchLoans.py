# -*- coding: utf-8 -*-

###############################################################################
#
# SearchLoans
# Returns a keyword search for loan listings by multiple criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchLoans(Choreography):

    """
    Create a new instance of the SearchLoans Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Loans/SearchLoans')


    def new_input_set(self):
        return SearchLoansInputSet()

    def _make_result_set(self, result, path):
        return SearchLoansResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchLoansChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchLoans
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchLoansInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the CountryCode input for this choreography. ((optional, string) A list of two-character ISO codes of countries by which to filter results.)
        """
        def set_CountryCode(self, value):
            InputSet._set_input(self, 'CountryCode', value)

        """
        Set the value of the Gender input for this choreography. ((optional, string) If supplied, results are filtered to loans with entrepreneurs of the specified gender. In the case of group loans, this matches against the predominate gender in the group: male or female.)
        """
        def set_Gender(self, value):
            InputSet._set_input(self, 'Gender', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Partner input for this choreography. ((optional, string) A list of partner IDs for which to filter results.)
        """
        def set_Partner(self, value):
            InputSet._set_input(self, 'Partner', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A query string against which results should be returned.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Region input for this choreography. ((optional, string) List of two-letter codes corresponding to regions in which Kiva operates. If supplied, results are filtered to loans only from the specified regions: na, ca, sa, af, as, me, ee.)
        """
        def set_Region(self, value):
            InputSet._set_input(self, 'Region', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Sector input for this choreography. ((optional, string) A list of business sectors for which to filter results.)
        """
        def set_Sector(self, value):
            InputSet._set_input(self, 'Sector', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) The order by which to sort results. Acceptable values: popularity, loan_amount, oldest, expiration, newest, amount_remaining, repayment_term. Defaults to newest.)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)

        """
        Set the value of the Status input for this choreography. ((optional, string) The status of loans to return: fundraising, funded, in_repayment, paid, ended_with_loss.)
        """
        def set_Status(self, value):
            InputSet._set_input(self, 'Status', value)


"""
A ResultSet with methods tailored to the values returned by the SearchLoans choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchLoansResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchLoansChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchLoansResultSet(response, path)
