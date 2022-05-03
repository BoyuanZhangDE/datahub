import datetime
from typing import Union, Optional
from datahub.configuration.common import ConfigModel


class GlueProfilingConfig(ConfigModel):
    enabled: Optional[bool] = False
    partitioned: Optional[bool] = False
    partition_column_name: Optional[str] = None

    rowCount: Optional[str] = None
    columnCount: Optional[str] = None
    uniqueCount: Optional[str] = None
    uniqueProportion: Optional[str] = None
    nullCount: Optional[str] = None
    nullProportion: Optional[str] = None
    min: Optional[str] = None
    max: Optional[str] = None
    mean: Optional[str] = None
    median: Optional[str] = None
    stdev: Optional[str] = None

    # qunatile
    quantiles: Optional[list[str]] = None
    quantile_prefix: Optional[str] = None

    # # histogram
    # MAX_HIST_BINS:

    # sample values
    # num_sample_rows: 2


    # Hidden option - used for debugging purposes.
    catch_exceptions: bool = True

    partition_profiling_enabled: bool = True
    bigquery_temp_table_schema: Optional[Optional[str] ] = None
    partition_datetime: Optional[datetime.datetime]

