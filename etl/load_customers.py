import time

from generator.generate_customers import generate_customers
from validation.validate_customers import validate_customers
from transformation.transform_customers import transform_customers

from etl_logging.etl_logger import log_pipeline
from etl_logging.error_logger import log_error

from config.database import engine


def load_customers():

    start = time.time()

    try:

        df = generate_customers()

        valid_df, invalid_df = validate_customers(df)

        transformed_df = transform_customers(valid_df)

        transformed_df.to_sql(
            name="customers",
            con=engine,
            if_exists="append",
            index=False
        )

        execution_time = round(time.time() - start, 2)

        log_pipeline(
            pipeline_name="Customer Churn ETL",
            records_generated=len(df),
            records_loaded=len(transformed_df),
            validation_errors=len(invalid_df),
            status="Success",
            execution_time=execution_time
        )

        print(f"Generated : {len(df)}")
        print(f"Valid : {len(valid_df)}")
        print(f"Invalid : {len(invalid_df)}")
        print(f"Loaded : {len(transformed_df)}")
        print(f"Execution Time : {execution_time} sec")

        return len(transformed_df)

    except Exception as e:

        log_error(
            pipeline_name="Customer Churn ETL",
            error_message=str(e)
        )

        print("Pipeline Failed")
        print(e)

        raise