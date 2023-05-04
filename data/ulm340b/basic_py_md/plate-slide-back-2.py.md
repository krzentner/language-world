

and then provide a series of `if check(...): robot.action(...)` statements below.
'''

ANSWER_BEGIN_LINE = 87
ANSWER_END_LINE = 97

def main(answer):
    pass

if __name__ == '__main__':
    with open('task2.py') as f:
        text = f.read()
    answer_text = text[ANSWER_BEGIN_LINE:ANSWER_END_LINE]
    answer = ast.unparse(ast.parse(answer_text))
    print(f'>>> {answer}')

    main(answer)

    
[eod] [code]# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.card_without_cvc_payment_method_specific_input import CardWithoutCVCPaymentMethodSpecificInput


class IdealPaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):

    __bank_account_address = None
    __bic = None
    __bic_holder = None
    __iban = None
    __owner_name = None

    @property
    def bank_account_address(self):
        """
        | Address of the bank account
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__bank_account_address

    @bank_account_address.setter
    def bank_account_address(self, value):
        self.__bank_account_address = value

    @property
    def bic(self):
        """
        | BIC code of the bank account
        
        Type: str
        """
        return self.__bic

    @bic.setter
    def bic(self, value):
        self.__bic = value

    @property
    def bic_holder(self):
        """
        | Name of the bank as written on the customer's bank statement
        
        Type: str
        """
        return self.__bic_holder

    @bic_holder.setter
    def bic_holder(self, value):