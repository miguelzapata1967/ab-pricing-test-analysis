# ===========================================================================================
#  checking dataframes structure and data types
# ===========================================================================================

import pandas as pd

# ===========================================================================================
#  Importing dataframes 
# ===========================================================================================

db1 = pd.read_csv(r'C:\Users\mexar\OneDrive\DE_Academy\A_B_Testing\CSVs\test_results.csv')
db2 = pd.read_csv(r'C:\Users\mexar\OneDrive\DE_Academy\A_B_Testing\CSVs\user_table.csv')

# ===========================================================================================
#  checking dataframes structure and data types
# ===========================================================================================
db1.info()
db2.info()

print(db1.head())
print(db2.head())   


# ===========================================================================================
#  checking duplicated user_id in both dataframes
# ===========================================================================================

print('test_results duplicated user_ids:', db1.duplicated(subset=['user_id'], keep=False).sum())
print('user_table   duplicated user_ids:', db2.duplicated(subset=['user_id'], keep=False).sum())


# ===========================================================================================
#  checking test_results user_ids missing from user_table and viceversa
# ===========================================================================================

print('Users missing from user_table:', (~db1['user_id'].isin(db2['user_id'])).sum())
print('Users missing from test_results:', (~db2['user_id'].isin(db1['user_id'])).sum())

# ===========================================================================================
#  checking test groups against assigned prices
# ===========================================================================================

print(db1.groupby(['test', 'price']).size())


# ===========================================================================================
#  creating dataframe for mismatched test and price records
# ===========================================================================================

mismatched_df = db1[
    ((db1['test'] == 0) & (db1['price'] == 59)) |
    ((db1['test'] == 1) & (db1['price'] == 39))
].copy()

print('Total mismatched records:', len(mismatched_df))
print(mismatched_df.head())

# ===========================================================================================
#  exporting mismatched records
# ===========================================================================================

mismatched_df.to_csv( r'C:\Users\mexar\OneDrive\DE_Academy\A_B_Testing\CSVs\mismatched_records.csv', index=False)

# ===========================================================================================
#  creating clean dataframe for A/B testing
# ===========================================================================================

db_clean = db1[
    ((db1['test'] == 0) & (db1['price'] == 39)) |
    ((db1['test'] == 1) & (db1['price'] == 59))
].copy()

print('Original records:', len(db1))
print('Mismatched records:', len(mismatched_df))
print('Clean records:', len(db_clean))


# ===========================================================================================
#  validating values in clean dataframe
# ===========================================================================================

print('\nConverted values:')
print(db_clean['converted'].value_counts())

print('\nSource values:')
print(db_clean['source'].value_counts())

print('\nDevice values:')
print(db_clean['device'].value_counts())

print('\nOperating system values:')
print(db_clean['operative_system'].value_counts())

# ===========================================================================================
#  converting timestamp to datetime and calculating test duration
# ===========================================================================================

# db_clean['timestamp'] = pd.to_datetime(db_clean['timestamp'])

# test_start = db_clean['timestamp'].min()
# test_end = db_clean['timestamp'].max()
# test_duration = test_end - test_start

# print('\nTimestamp data type:', db_clean['timestamp'].dtype)
# print('Test start:', test_start)
# print('Test end:', test_end)
# print('Test duration:', test_duration)

# ===========================================================================================
#  checking for invalid timestamps
# ===========================================================================================

timestamp_check = pd.to_datetime(
    db_clean['timestamp'],
    format='%Y-%m-%d %H:%M:%S',
    errors='coerce'
)

invalid_timestamp_mask = timestamp_check.isna()

invalid_timestamps_df = db_clean[invalid_timestamp_mask].copy()

print('\nInvalid timestamp records:', len(invalid_timestamps_df))

print('\nInvalid timestamp values:')
print(invalid_timestamps_df[
    ['user_id', 'timestamp', 'test', 'price', 'converted']
].to_string(index=False))

print('\nTOTAL INVALID TIMESTAMPS:', len(invalid_timestamps_df))

# ===========================================================================================
#  exporting invalid timestamp records
# ===========================================================================================

invalid_timestamps_df.to_csv(
    r'C:\Users\mexar\OneDrive\DE_Academy\A_B_Testing\CSVs\invalid_timestamps.csv',
    index=False
)

print('Invalid timestamp records exported:', len(invalid_timestamps_df))




# ===========================================================================================
#  creating dataframe with valid timestamps
# ===========================================================================================

valid_timestamp_df = db_clean[~invalid_timestamp_mask].copy()

valid_timestamp_df['timestamp'] = pd.to_datetime(
    valid_timestamp_df['timestamp'],
    format='%Y-%m-%d %H:%M:%S'
)

print('\nValid timestamp records:', len(valid_timestamp_df))
print('Invalid timestamp records:', len(invalid_timestamps_df))

# ===========================================================================================
# calculating A/B test duration
# ===========================================================================================

test_start = valid_timestamp_df['timestamp'].min()
test_end = valid_timestamp_df['timestamp'].max()
test_duration = test_end - test_start

print('\nA/B TEST DURATION')
print('Test start:', test_start)
print('Test end:', test_end)
print('Test duration:', test_duration)

# ===========================================================================================
# merging experiment data with geographic data
# ===========================================================================================

db_merged = db_clean.merge(
    db2,
    on='user_id',
    how='left'
)

print('\nGEOGRAPHIC MERGE')
print('Records before merge:', len(db_clean))
print('Records after merge:', len(db_merged))

# ===========================================================================================
#  validating geographic merge
# ===========================================================================================

print('\nMissing geographic information:')
print(db_merged[['city', 'country', 'lat', 'long']].isna().sum())

print('\nMerged dataset shape:')
print(db_merged.shape)

# ===========================================================================================
# calculating conversion rate by price
# ===========================================================================================

conversion_by_price = db_merged.groupby('price')['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

conversion_by_price['conversion_rate_percent'] = (
    conversion_by_price['conversion_rate'] * 100
)

print('\nCONVERSION RATE BY PRICE')
print(conversion_by_price)

# ===========================================================================================
# calculating revenue by price
# ===========================================================================================

db_merged['revenue'] = db_merged['price'] * db_merged['converted']

revenue_by_price = db_merged.groupby('price').agg(
    users=('user_id', 'count'),
    conversions=('converted', 'sum'),
    total_revenue=('revenue', 'sum')
)

revenue_by_price['revenue_per_user'] = (
    revenue_by_price['total_revenue'] / revenue_by_price['users']
)

print('\nREVENUE BY PRICE')
print(revenue_by_price)

# ===========================================================================================
#  testing statistical significance of conversion rates
# ===========================================================================================

from statsmodels.stats.proportion import proportions_ztest

conversions = [4030, 1772]
users = [202517, 113918]

z_stat, p_value = proportions_ztest(
    conversions,
    users
)

print('\nSTATISTICAL SIGNIFICANCE TEST')
print('Z-statistic:', z_stat)
print('P-value:', p_value)

# ===========================================================================================
# checking conversion rates over the test period
# ===========================================================================================

time_analysis = valid_timestamp_df.copy()

time_analysis['month'] = time_analysis['timestamp'].dt.to_period('M')

conversion_by_month = time_analysis.groupby(
    ['month', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

conversion_by_month['conversion_rate_percent'] = (
    conversion_by_month['conversion_rate'] * 100
)

print('\nCONVERSION RATE BY MONTH AND PRICE')
print(conversion_by_month)

# ===========================================================================================
# Checking weekly conversion stability
# ===========================================================================================

weekly_analysis = valid_timestamp_df.copy()

weekly_analysis['week'] = (
    weekly_analysis['timestamp'].dt.to_period('W')
)

conversion_by_week = weekly_analysis.groupby(
    ['week', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

conversion_by_week['conversion_rate_percent'] = (
    conversion_by_week['conversion_rate'] * 100
)

print('\nQUESTION 9 - WEEKLY CONVERSION RATE BY PRICE')
print(conversion_by_week)


# ===========================================================================================
# business impact of the price change
# ===========================================================================================

revenue_39 = revenue_by_price.loc[39, 'revenue_per_user']
revenue_59 = revenue_by_price.loc[59, 'revenue_per_user']

revenue_difference = revenue_59 - revenue_39

revenue_percent_change = (
    (revenue_59 - revenue_39) / revenue_39
) * 100

print('\nQUESTION 10 - BUSINESS IMPACT')
print('Revenue per user at $39:', revenue_39)
print('Revenue per user at $59:', revenue_59)
print('Revenue difference per user:', revenue_difference)
print('Revenue percent change:', revenue_percent_change)


# ===========================================================================================
# conversion rate by marketing source and price
# ===========================================================================================

source_analysis = db_merged.groupby(
    ['source', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

source_analysis['conversion_rate_percent'] = (
    source_analysis['conversion_rate'] * 100
)

print('\nQUESTION 11 - CONVERSION BY MARKETING SOURCE')
print(source_analysis)


# ===========================================================================================
# conversion rate by device and price
# ===========================================================================================

device_analysis = db_merged.groupby(
    ['device', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

device_analysis['conversion_rate_percent'] = (
    device_analysis['conversion_rate'] * 100
)

print('\nQUESTION 12A - CONVERSION BY DEVICE')
print(device_analysis)


# ===========================================================================================
# conversion rate by operating system and price
# ===========================================================================================

os_analysis = db_merged.groupby(
    ['operative_system', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

os_analysis['conversion_rate_percent'] = (
    os_analysis['conversion_rate'] * 100
)

print('\nQUESTION 12B - CONVERSION BY OPERATING SYSTEM')
print(os_analysis)


# ===========================================================================================
# geographic analysis by city and price
# ===========================================================================================

geo_analysis_df = db_merged.dropna(
    subset=['city', 'country']
).copy()

city_analysis = geo_analysis_df.groupby(
    ['city', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

city_analysis['conversion_rate_percent'] = (
    city_analysis['conversion_rate'] * 100
)

print('\nQUESTION 13 - GEOGRAPHIC ANALYSIS')
print('Records available for geographic analysis:', len(geo_analysis_df))
print('Records excluded because geography is missing:',
      len(db_merged) - len(geo_analysis_df))

print('\nCONVERSION BY CITY AND PRICE')
print(city_analysis)

# ===========================================================================================
# identifying cities with small sample sizes
# ===========================================================================================

city_sample_sizes = geo_analysis_df.groupby(
    ['city', 'price']
).size().unstack(fill_value=0)

city_sample_sizes.columns = [
    f'users_price_{price}'
    for price in city_sample_sizes.columns
]

print('\nCITY SAMPLE SIZE SUMMARY')
print(city_sample_sizes.describe())


# Identifying cities with fewer than 100 users
# in at least one price group

small_city_samples = city_sample_sizes[
    (city_sample_sizes['users_price_39'] < 100) |
    (city_sample_sizes['users_price_59'] < 100)
]

print('\nCITIES WITH SMALL SAMPLE SIZES')
print(small_city_samples)

print(
    '\nTotal cities with small sample sizes:',
    len(small_city_samples)
)

# ===========================================================================================
# conversion stability over time / novelty-effect investigation
# ===========================================================================================

monthly_analysis = valid_timestamp_df.copy()

monthly_analysis['month'] = (
    monthly_analysis['timestamp'].dt.to_period('M')
)

novelty_analysis = monthly_analysis.groupby(
    ['month', 'price']
)['converted'].agg(
    users='count',
    conversions='sum',
    conversion_rate='mean'
)

novelty_analysis['conversion_rate_percent'] = (
    novelty_analysis['conversion_rate'] * 100
)

print('\nQUESTION 14 - CONVERSION STABILITY OVER TIME')
print(novelty_analysis)


# ===========================================================================================
# final evidence summary
# ===========================================================================================

conversion_39 = conversion_by_price.loc[
    39, 'conversion_rate_percent'
]

conversion_59 = conversion_by_price.loc[
    59, 'conversion_rate_percent'
]

conversion_difference = conversion_39 - conversion_59

print('\nQUESTION 15 - FINAL EVIDENCE SUMMARY')

print('\nConversion Rate')
print('$39:', conversion_39, '%')
print('$59:', conversion_59, '%')
print('Difference:', conversion_difference, 'percentage points')

print('\nRevenue Per User')
print('$39:', revenue_39)
print('$59:', revenue_59)
print('Percent change at $59:', revenue_percent_change, '%')

print('\nStatistical Significance')
print('Z-statistic:', z_stat)
print('P-value:', p_value)

print('\nTest Duration')
print('Start:', test_start)
print('End:', test_end)
print('Duration:', test_duration)

print('\nData Quality')
print('Original records:', len(db1))
print('Clean records:', len(db_clean))
print('Mismatched test/price records:', len(mismatched_df))
print('Invalid timestamp records:', len(invalid_timestamps_df))
print(
    'Records without geographic information:',
    db_merged['city'].isna().sum()
)