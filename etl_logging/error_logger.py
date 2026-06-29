from sqlalchemy import text
from config.database import engine

def log_error(pipeline_name, error_message):

    with engine.begin() as conn:

        conn.execute(
            text("""
                INSERT INTO error_logs
                (
                    pipeline_name,
                    error_message
                )

                VALUES
                (
                    :pipeline_name,
                    :error_message
                )
            """),

            {
                "pipeline_name": pipeline_name,
                "error_message": error_message
            }
        )