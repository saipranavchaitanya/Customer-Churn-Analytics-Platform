from sqlalchemy import text
from config.database import engine


def log_pipeline(
    pipeline_name,
    records_generated,
    records_loaded,
    validation_errors,
    status,
    execution_time
):

    with engine.begin() as conn:

        conn.execute(
            text("""
                INSERT INTO etl_logs
                (
                    pipeline_name,
                    records_generated,
                    records_loaded,
                    validation_errors,
                    status,
                    execution_time_seconds
                )

                VALUES
                (
                    :pipeline_name,
                    :records_generated,
                    :records_loaded,
                    :validation_errors,
                    :status,
                    :execution_time
                )
            """),

            {
                "pipeline_name": pipeline_name,
                "records_generated": records_generated,
                "records_loaded": records_loaded,
                "validation_errors": validation_errors,
                "status": status,
                "execution_time": execution_time
            }
        )