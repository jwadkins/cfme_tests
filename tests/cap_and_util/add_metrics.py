
import pytest
import time
from unittestzero import Assert
import datetime


#def test_insert_vm(db_session):
#    vm_name = 'test_new_user'
#    host_id = 1
#    vendor = 'vmware'
#    storage_id = 2
#    ems_id = 17
#    ems_ref = 'vm-5042'
#    vm_type = 'VmVmware'
#    power_state = 'on'
#    
#    import db
#    session = db_session
#
#    new_vm = db.Vm(name = vm_name)
#    session.add(new_vm)
#    new_vm.host_id = host_id
#    new_vm.storage_id = storage_id
#    new_vm.ems_id = ems_id
#    new_vm.vendor = vendor
#    new_vm.type = vm_type
#    new_vm.power_state = power_state
#    new_vm.ems_ref = ems_ref
#
#    session.commit()

@pytest.mark.nondestructive
def insert_previous_hour_raw_metric_data(db_session, resource_id, columns):
    resource_id = resource_id
    #resource_name = resource_name
    columns = columns
    date = datetime.datetime.utcnow()
    date = date.replace(microsecond=0)
    date = date.replace(second = 0)
    date = date.replace(minute = 0)
    date = date - datetime.timedelta(hours = 1)
    previous_hour = date.hour
    capture_interval_name = 'realtime'
    import db
    session = db_session
    while date.hour <= previous_hour + 2:
        new_user = db.Metric(resource_id = resource_id)
        session.add(new_user)
        #new_user.resource_name = resource_name
        new_user.timestamp = date
        new_user.capture_interval_name = capture_interval_name
        date = date + datetime.timedelta(seconds = 20)
        for key, value in columns.items():
            setattr(new_user, key, value)
    session.commit()

@pytest.mark.nondestructive
def insert_previous_day_hourly_rollups(db_session, resource_id, columns):
    #resource_name = resource_name
    resource_id = resource_id                                                                      
    #timestamp = '2013-07-02 09:00:00'                                                                   
    date=datetime.datetime.utcnow()
    capture_interval_name = 'hourly'
    date = date.replace(microsecond = 0)
    date = date.replace(second = 0)
    date = date.replace(minute = 0)
    date = date.replace(hour = 0)
    date = date - datetime.timedelta(days = 1)
    columns = columns                                                                         
    import db
    session = db_session                                                                                 
    for x in range(0, 24):                                                                         
        new_user = db.MetricRollup(resource_id = resource_id)
        session.add(new_user)
        #new_user.resource_name = resource_name
        new_user.timestamp = date
        new_user.capture_interval_name = capture_interval_name
        date = date + datetime.timedelta(hours = 1)
        for key, value in columns.items():
            setattr(new_user, key, value) 
    session.commit()    



