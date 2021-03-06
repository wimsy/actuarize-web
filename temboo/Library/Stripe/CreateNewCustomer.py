# -*- coding: utf-8 -*-

###############################################################################
#
# CreateNewCustomer
# Creates a new customer record.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateNewCustomer(Choreography):

    """
    Create a new instance of the CreateNewCustomer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/CreateNewCustomer')


    def new_input_set(self):
        return CreateNewCustomerInputSet()

    def _make_result_set(self, result, path):
        return CreateNewCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewCustomerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateNewCustomer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateNewCustomerInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the AddressLine1 input for this choreography. ((optional, string) The first line of the address that is associated with the credit card billing address)
        """
        def set_AddressLine1(self, value):
            InputSet._set_input(self, 'AddressLine1', value)

        """
        Set the value of the AddressLine2 input for this choreography. ((optional, string) The second line of the address that is associated with the credit card billing address)
        """
        def set_AddressLine2(self, value):
            InputSet._set_input(self, 'AddressLine2', value)

        """
        Set the value of the CVC input for this choreography. ((optional, integer) The 3-digit card security code)
        """
        def set_CVC(self, value):
            InputSet._set_input(self, 'CVC', value)

        """
        Set the value of the CardNumber input for this choreography. ((optional, integer) The credit card number without any separators. Required when attaching a credit card to the customer record unless using a Token.)
        """
        def set_CardNumber(self, value):
            InputSet._set_input(self, 'CardNumber', value)

        """
        Set the value of the CardholderName input for this choreography. ((optional, string) The cardholder's full name as it appears on the credit card)
        """
        def set_CardholderName(self, value):
            InputSet._set_input(self, 'CardholderName', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) The country associated with the credit card billing address)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Coupon input for this choreography. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        def set_Coupon(self, value):
            InputSet._set_input(self, 'Coupon', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) An arbitrary string of text that will be associated with the customer object)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) The customer's email address)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the ExpirationMonth input for this choreography. ((optional, integer) The card's expiration month as a two digit number. Required when supplying a card number to attach to the customer.)
        """
        def set_ExpirationMonth(self, value):
            InputSet._set_input(self, 'ExpirationMonth', value)

        """
        Set the value of the ExpirationYear input for this choreography. ((optional, integer) The card's expiration year as a 4 digit number. Required when supplying a card number to attach to the customer.)
        """
        def set_ExpirationYear(self, value):
            InputSet._set_input(self, 'ExpirationYear', value)

        """
        Set the value of the Plan input for this choreography. ((optional, string) The unique identifier of the plan to subscribe the customer to)
        """
        def set_Plan(self, value):
            InputSet._set_input(self, 'Plan', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The state of the address that is associated with the credit card billing address)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Token input for this choreography. ((optional, string) The token associated with a set of credit card details. When a token is provided, no other credit card details are necessary.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)

        """
        Set the value of the TrialEnd input for this choreography. ((optional, date) Epoch timestamp in seconds for the end of the trial period. The customer won't be charged during the trial period. Timestamp should be in UTC.)
        """
        def set_TrialEnd(self, value):
            InputSet._set_input(self, 'TrialEnd', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The zip code of the address that is associated with the credit card billing address)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the CreateNewCustomer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateNewCustomerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateNewCustomerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateNewCustomerResultSet(response, path)
