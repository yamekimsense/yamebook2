#run like this
#python3 114-acitoolkit-show-tenant.py -u 'https://sandboxapicdc.cisco.com' -l 'admin' -p '!v3G@!4@Y'
#
#this file comes from https://github.com/datacenter/acitoolkit/blob/master/samples/aci-show-tenants.py

import sys
import acitoolkit.acitoolkit as ACI


def main():
    """
    Main execution routine
    :return: None
    """
    # Take login credentials from the command line if provided
    # Otherwise, take them from your environment variables file ~/.profile
    description = 'Simple application that logs on to the APIC and displays all of the Tenants.'
    creds = ACI.Credentials('apic', description)
    args = creds.get()

    # Login to APIC
    session = ACI.Session(args.url, args.login, args.password)

    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    # Download all of the tenants
    print("TENANT")
    print("------")
    tenants = ACI.Tenant.get(session)
    for tenant in tenants:
        print(tenant.name)

if __name__ == '__main__':
    main()


'''

(venv) wankim@WANKIM-M-P1E1 100-ACI-API % python3 140-acitoolkit-show-tenant.py -u 'https://sandboxapicdc.cisco.com' -l 'admin' -p '!v3G@!4@Y'
TENANT
------
infra
common
mgmt
aci_2023_tenant
oneaciapp
ABC
Tenant-VJ
TEST_tENANT
TEST_1
funsiona_bien
SLF
gs_560030y
karben
production_rajan
INITIALS_Toolkit_Tenant
VJ-Tenant
tenant4
0aci_api_test
RCC012023
0aci-api-test2
CUST101
ALASCOM
Teste_Fabricio
(venv) wankim@WANKIM-M-P1E1 100-ACI-API % 


'''