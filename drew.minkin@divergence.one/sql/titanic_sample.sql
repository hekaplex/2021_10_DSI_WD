WITH
	t
		AS
		(
		SELECT 
			survived, Fare/Age as DollarPerYr
		from titanic
		)
,
	all_l
		AS
			(SELECT 
				--survived, 
				AVG(DollarPerYr) all_level
			from t
			)--group by survived
SELECT 
				survived, 
				AVG(DollarPerYr)/all_level relativeDPY
			from t,all_l
			group by survived,all_level
