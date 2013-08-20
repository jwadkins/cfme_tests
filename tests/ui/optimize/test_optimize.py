import pytest
import time
import datetime
import collections
from unittestzero import Assert
from ... cap_and_util.delete_metrics import delete_raw_metric_data
from ... cap_and_util.delete_metrics import delete_metric_rollup_data
from ... cap_and_util.add_metrics import insert_previous_weeks_hourly_rollups
from ... cap_and_util.add_metrics import insert_previous_weeks_daily_rollups

@pytest.fixture
def provider_info(db_session):
    import db
    session = db_session
    provider_info = session.query(db.ExtManagementSystem).filter_by(type = 'EmsVmware').first()
    resource_id = provider_info.id
    name = provider_info.name
    provider_info = collections.namedtuple('provider_info', ['id', 'name'])
    provider_info = provider_info(resource_id, name)
    return provider_info

@pytest.mark.nondestructive
@pytest.mark.usefixtures("maximized")
#@pytest.mark.usefixtures("setup_infrastructure_providers")
def test_delete_provider_metric_data(db_session, provider_info):
    resource_id = provider_info.id
    delete_raw_metric_data(db_session, resource_id)
    delete_metric_rollup_data(db_session, resource_id)    

@pytest.mark.nondestructive
@pytest.mark.usefixtures("maximized")
def test_add_provider_metric_data(db_session, provider_info):
    resource_id = provider_info.id
    provider_name = provider_info.name
    hourly_rollup_data = {
        #'resource_name': provider_name,
        'resource_type': 'ExtManagementSystem',
        'cpu_usagemhz_rate_average': 2000,
        'cpu_usage_rate_average': 3000,
        'derived_memory_used': 1000,
        'derived_memory_available': 4000,
        'derived_memory_reserved': 7000,
        'derived_cpu_available': 5000,
        'derived_cpu_reserved': 7000,
        'cpu_ready_delta_summation': 262081,
        'cpu_system_delta_summation': 14572,
        'cpu_wait_delta_summation': 39261192,    
        'cpu_used_delta_summation': 7660021
    }
    daily_rollup_data = {
        #'resource_name': provider_name,
        'resource_type': 'ExtManagementSystem',
        'cpu_usagemhz_rate_average': 2000,
        'cpu_usage_rate_average': 3000,
        'derived_memory_used': 1000,
        'derived_memory_available': 4000,
        'derived_memory_reserved': 7000,        
        'derived_cpu_available': 5000,
        'derived_cpu_reserved': 7000,
        'cpu_ready_delta_summation': 262081,
        'cpu_system_delta_summation': 14572,
        'cpu_wait_delta_summation': 39261192,    
        'cpu_used_delta_summation': 7660021,        
        'min_max' : '''---
:min_cpu_usagemhz_rate_average: 100
:max_cpu_usagemhz_rate_average: 800
:min_derived_memory_used: 200
:max_derived_memory_used: 700'''
    }
    insert_previous_weeks_hourly_rollups(db_session, resource_id, hourly_rollup_data)
    insert_previous_weeks_daily_rollups(db_session, resource_id, daily_rollup_data)

@pytest.mark.nondestructive
@pytest.mark.usefixtures("maximized")
def test_add_provider_metric_data(optimize_utilization_pg, provider_info):
    Assert.true(optimize_utilization_pg.is_the_current_page)
    node_name = provider_info.name
    node_pg = optimize_utilization_pg.click_on_node(node_name)
    assert 0
    summary_pg = node_pg.click_on_summary()    
'''
@pytest.mark.nondestructive
#@pytest.mark.usefixtures("setup_infrastructure_providers")
@pytest.mark.usefixtures("maximized")
class TestUtilization:
    def test_datastores(self, optimize_utilization_pg):
        Assert.true(optimize_utilization_pg.is_the_current_page)
        node_name = "datastore1"
        assert 0
        node_pg = optimize_utilization_pg.click_on_node(node_name)
        summary_pg = node_pg.click_on_summary()
        #Assert.true(summary_pg.tab_buttons.current_tab == "Summary")
        sum_trends = "2 Weeks"
        sum_classification = ""
        sum_time_zone = ""
        sum_date = "7/5/2013"
        initial_sum_date = summary_pg.date_field.get_attribute("value")
        summary_pg.fill_data(sum_trends, sum_classification, sum_time_zone, sum_date)
        if(summary_pg.date_field.get_attribute("value") == initial_sum_date):
             Assert.true(summary_pg.date_field.get_attribute("value") == sum_date, "There is no utilization date for the specified date")
        else:
            Assert.true(summary_pg.date_field.get_attribute("value") == sum_date)
        time.sleep(5)
        details_pg = summary_pg.click_on_details()
        #Assert.true(summary_pg.tab_buttons.current_tab == "Details")
        det_trends = "3 Weeks"
        det_classification = ""
        det_time_zone = ""
        details_pg.fill_data(det_trends, det_classification, det_time_zone)
        time.sleep(5)
        report_pg = details_pg.click_on_report()
        #Assert.true(summary_pg.tab_buttons.current_tab == "Report")
        rep_trends = "4 Weeks"
        rep_classification = ""
        rep_time_zone = ""
        rep_date = "7/5/2013"
        initial_rep_date = report_pg.date_field.get_attribute("value")
        report_pg.fill_data(rep_trends, rep_classification, rep_time_zone, rep_date)
        if(summary_pg.date_field.get_attribute("value") == initial_sum_date):
             Assert.true(report_pg.date_field.get_attribute("value") == rep_date, "There is no utilization date for the specified date")
        else:
             Assert.true(report_pg.date_field.get_attribute("value") == rep_date)
        Assert.true(report_pg.details.get_section("Basic Information").get_item("Utilization Trend Summary for").value == "Datastore [%s]" %node_name)

    def test_providers(self, optimize_utilization_pg):
        Assert.true(optimize_utilization_pg.is_the_current_page)
        node_name = "RHEV 3.1"
        node_pg = optimize_utilization_pg.click_on_node(node_name)
        summary_pg = node_pg.click_on_summary()
        #Assert.true(summary_pg.tab_buttons.current_tab == "Summary")
        sum_trends = "2 Weeks"
        sum_classification = ""
        sum_time_zone = ""
        sum_date = "7/5/2013"
        initial_sum_date = summary_pg.date_field.get_attribute("value")
        summary_pg.fill_data(sum_trends, sum_classification, sum_time_zone, sum_date)
        if(summary_pg.date_field.get_attribute("value") == initial_sum_date):
             Assert.true(summary_pg.date_field.get_attribute("value") == sum_date, "There is no utilization date for the specified date")
        else:
            Assert.true(summary_pg.date_field.get_attribute("value") == sum_date)
        time.sleep(5)
        details_pg = summary_pg.click_on_details()
        det_trends = "3 Weeks"
        det_classification = ""
        det_time_zone = ""
        details_pg.fill_data(det_trends, det_classification, det_time_zone)
        time.sleep(5)
        report_pg = details_pg.click_on_report()
        rep_trends = "4 Weeks"
        rep_classification = ""
        rep_time_zone = ""
        rep_date = "7/5/2013"
        initial_rep_date = report_pg.date_field.get_attribute("value")
        report_pg.fill_data(rep_trends, rep_classification, rep_time_zone, rep_date)
        if(summary_pg.date_field.get_attribute("value") == initial_sum_date):
             Assert.true(report_pg.date_field.get_attribute("value") == rep_date, "There is no utilization date for the specified date")
        else:
            Assert.true(report_pg.date_field.get_attribute("value") == rep_date)
        Assert.true(report_pg.details.get_section("Basic Information").get_item("Utilization Trend Summary for").value == "Management System [%s]" %node_name)
'''


