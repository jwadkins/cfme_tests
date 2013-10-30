import db


def check_off_hours(db_session, resource_id, columns, hours_to_check):
	resource_id = resource_id
	columns = columns
	hours_to_check = hours_to_check
	session = db_session


	#entry = session.query(db.MetricRollup).filter(db.MetricRollup.resource_id == resource_id, db.MetricRollup.timestamp == '2013-10-29 14:00:00').first()

	i=0
	j=0

	while(i < len(hours_to_check)):

		temp_entry = session.query(db.MetricRollup).filter(db.MetricRollup.resource_id == resource_id, db.MetricRollup.timestamp == hours_to_check[i]).first()

		#assert 0

		while(j < len(columns)):

			temp_value = getattr(temp_entry, columns[j])

			print('\nThe Resource Name is: %s and the timestamp is: %s  The value in column: %s is %f' %(temp_entry.resource_name, hours_to_check[i], columns[j], temp_value))

			j += 1

		i += 1

	#assert 0

	#return entry.cpu_usage_rate_average


