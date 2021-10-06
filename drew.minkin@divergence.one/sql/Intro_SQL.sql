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
		s.[SalesReasonKey]
		, count(*) quantity
from 
		[dbo].[FactInternetSales] f
inner join 
		[dbo].[FactInternetSalesReason] s
on 
		s.[SalesOrderNumber] = f.SalesOrderNumber
and 
		s.[SalesOrderLineNumber] = f.SalesOrderLineNumber
group by 
		s.[SalesReasonKey]

