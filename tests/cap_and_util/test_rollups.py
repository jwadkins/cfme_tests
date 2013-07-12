import pytest
import time
import sys
from unittestzero import Assert
from delete_metrics import delete_raw_metric_data
from delete_metrics import delete_metric_rollup_data
from add_metrics import insert_previous_hour_raw_metric_data
from add_metrics import insert_previous_day_hourly_rollups

@pytest.mark.nondestructive
def test_delete_raw_vm_metric_data(db_session):
    resource_id = 6
    delete_raw_metric_data(db_session, resource_id)
    
    delete_metric_rollup_data(db_session, resource_id)

@pytest.mark.nondestructive
def test_add_previous_hour_raw_metrics(db_session):
    resource_id = 6
    columns = {
        'resource_name':'dajo-cfme-5104-4',
        'resource_type': 'VmOrTemplate',
        'cpu_usagemhz_rate_average': 300,
        'net_usage_rate_average' : 600,
        'disk_usage_rate_average': 80,
        'derived_memory_used': 400,
    }
    insert_previous_hour_raw_metric_data(db_session, resource_id, columns)


@pytest.mark.nondestructive
def test_add_previous_day_hourly_metrics(db_session):
    resource_id = 6
    columns = {
        'resource_name':'dajo-cfme-5104-4',
        'resource_type': 'VmOrTemplate',
        'cpu_usagemhz_rate_average': 200,
        'net_usage_rate_average' : 500,
        'disk_usage_rate_average': 70,
        'derived_memory_used': 100,
        #'derived_storage_vm_count_managed': 70,
        #'mem_usage_absolute_average': 80,
        'cpu_ready_delta_summation ': 372579.208333333,
        #'cpu_system_delta_summation': 159470.75,
        #'cpu_wait_delta_summation': 4737532.375,
        'cpu_used_delta_summation': 2143234.66666667
    }
    insert_previous_day_hourly_rollups(db_session, resource_id, columns)
