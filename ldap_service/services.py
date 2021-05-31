import os


def get_attribute_and_fta_by_account_number(account_number) -> tuple:
    attribute: str = None
    fta: str = None

    command_base = "ldapsearch -h vedir.srv.hcvlny.cv.net -p 389 -D uid=appuser,ou=appadm,o=entitlement -w PaBlAn0 -b ou=roles,o=entitlement '(&(Accountnumber={account_number})(objectClass=CVCSDPRole))' | egrep 'attribute2|acctfta'"
    command = command_base.format(account_number=account_number)

    ldapsearch_response = os.popen(command).read().split()

    if 'attribute2:' in ldapsearch_response:
        attribute = ldapsearch_response[ldapsearch_response.index('attribute2:') + 1].strip("0")

    if 'acctfta:' in ldapsearch_response:
        fta = ldapsearch_response[ldapsearch_response.index('acctfta:') + 1].strip("0")

    return attribute, fta


def get_lineup_id_by_attribute_and_fta(attribute, fta) -> str:
    lineup_id: str = None
    ocmr_corp_fta = f'{attribute}-{fta}'

    command_base = "ldapsearch -h vedir.srv.hcvlny.cv.net -p 389 -D uid=appuser,ou=appadm,o=entitlement -w PaBlAn0 -b ou=ocmrlineup,o=entitlement '(&(OCMRCorpFTA={ocmr_corp_fta})(objectClass=CVCSDPLineupMap))' | egrep OCMRLaBoxLineupID | sort -u"
    command = command_base.format(ocmr_corp_fta=ocmr_corp_fta)

    _, lineup_id = os.popen(command).read().strip().split()

    return lineup_id


def get_lineup_id_by_account_number(account_number) -> str:
    lineup_id: str = None
    attribute, fta = get_attribute_and_fta_by_account_number(account_number)

    if all([attribute, fta]):
        lineup_id = get_lineup_id_by_attribute_and_fta(attribute, fta)

    return lineup_id
