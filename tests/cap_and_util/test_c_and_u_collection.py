import pytest
import collections
from unittestzero import Assert
from check_db_content import check_off_hours
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def vm_info(db_session, vm_name):
    import db
    session = db_session
    vm_info = session.query(db.Vm).filter_by(name= vm_name ).first()
    resource_id = vm_info.id
    name = vm_info.name
    vm_info = collections.namedtuple('vm_info', ['id', 'name'])
    vm_info = vm_info(resource_id, name)
    return vm_info


@pytest.mark.nondestructive
@pytest.mark.usefixtures("maximized")
def test_gaps_in_collectoin(db_session):

    i = 0
    vms_to_check = [
        'wadkins-cfme-35-1',
        'wadkins-cfme-520-37-1021-2'
    ]

    while (i < len(vms_to_check)):
        temp_vm = vm_info(db_session, vms_to_check[i])
        resource_id = temp_vm.id

        hours_to_check = [
            '2013-10-29 14:00:00',
            '2013-10-29 18:00:00',
            '2013-10-30 12:00:00 '
        ]

        columns = [
            'cpu_usage_rate_average',
            'disk_usage_rate_average'
        ]   

        result = check_off_hours(db_session, resource_id, columns, hours_to_check)

        i += 1

    #assert 0




