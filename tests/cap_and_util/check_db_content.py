import datetime
import db

def check_off_hours(db_session, resource_id, columns, hours_to_check):
	resource_id = resource_id
	columns = columns
	past_date = past_date
	hours_off = hours_off

	session = db_session

	entry = session.query(db.MetricRollup).filter(db.MetricRollup.resource_id == resource_id, db.MetricRollup.timestamp == '2013-10-17 12:00:00').first()

	entry.disk_usage_rate_average


