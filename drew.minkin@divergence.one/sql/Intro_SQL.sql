ALTER TABLE [dbo].[FactInternetSales] 
ADD  CONSTRAINT [PK_FactInternetSales_SalesOrderNumber_SalesOrderLineNumber] PRIMARY KEY CLUSTERED 
(
	[SalesOrderNumber] ASC,
	[SalesOrderLineNumber] ASC
)


USE [AdventureWorksDW2019]
GO

ALTER TABLE [dbo].[FactInternetSales]  
WITH CHECK 
ADD  CONSTRAINT [FK_FactInternetSales_DimDate1] 
FOREIGN KEY([DueDateKey])
REFERENCES [dbo].[DimDate] ([DateKey])
GO
/****** Script for SelectTopNRows command from SSMS  ******/
CREATE VIEW sample_demo as
SELECT Demographics,LastName, len(LastName) length_name
  FROM [AdventureWorks2019].[Person].[Person]
  
  select * from  sample_demo
  
  
  SELECT 
  CASE when substring(LastName,1,1)>'M' then 1 else 0 end
  length_name, count(*) from [dbo].[sample_demo]
  group by 
  CASE when substring(LastName,1,1)>'M' then 1 else 0 end, length_name
  order by 2 desc


  SELECT   CASE when substring(LastName,1,1)>'M' then 1 else 0 end
  , count(*) from [dbo].[sample_demo]
  group by CASE when substring(LastName,1,1)>'M' then 1 else 0 end
    order by 2 desc


ALTER TABLE [dbo].[FactInternetSales] CHECK CONSTRAINT [FK_FactInternetSales_DimDate1]
GO

select 
		--grouping/tuple/slicer/dimension (string or enumeration)
		s.[SalesReasonKey]
		--metric/aggregate/measure + numeric
		, count(*) quantity
from 
		[dbo].[FactInternetSales] f
inner join
--left outer join
--right outer join
--outer join
		[dbo].[FactInternetSalesReason] s
on 
--composite key = multiple columns

		--primary key
		s.[SalesOrderNumber] 
		= 
		--foreign key
		f.SalesOrderNumber
and 
		s.[SalesOrderLineNumber] = f.SalesOrderLineNumber
where f.SalesAmount < 10
group by 
		s.[SalesReasonKey]
having count(*) < 5000
order by
		--count(*)
		quantity desc
/*
1	47733
2	7390
10	3653
5	1818
6	1640
9	1551
4	730
*/