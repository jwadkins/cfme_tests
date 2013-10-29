import pytest
import datetime
import collections
from unittestzero import Assert
from check_db_content import check_off_hours
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def vm_info(db_session):
    import db
    session = db_session
    vm_info = session.query(db.Vm).filter_by(name = 'wadkins-cfme-35-1').first()
    resource_id = vm_info.id
    name = vm_info.name
    vm_info = collections.namedtuple('vm_info', ['id', 'name'])
    vm_info = vm_info(resource_id, name)
    return vm_info

@pytest.mark.nondestructive
@pytest.mark.usefixtures("maximized")
def test_gaps_in_collectoin(vm_info):

	hours_to_check = {
		'2013-10-17 10:00:00',
	}

	columns = {
	'disk_usage_rate_average'
	}    

    while(past_date <= date):

    	result = check_off_hours(db_session, resource_id, columns, hours_to_check)

    	assert 0

    	past_date = past_date + datetime.timedelta(hours = 2)




