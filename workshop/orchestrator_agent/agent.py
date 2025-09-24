import logging
from google.adk.sessions import DatabaseSessionService
from google.adk.artifacts import GcsArtifactService
from google.adk.runners import Runner
from .sub_agent.agent import root_agent
from config import GCS_IMAGE_BUCKET, LOCAL_DB_URL

logger = logging.getLogger(__name__)

gcs_bucket_name_py = GCS_IMAGE_BUCKET

try:
    gcs_service_py = GcsArtifactService(bucket_name=gcs_bucket_name_py)
    logger.info(f"Python GcsArtifactService initialized for bucket: {gcs_bucket_name_py}")
except Exception as e:
    logger.error(f"Error initializing Python GcsArtifactService: {e}")

session_service = DatabaseSessionService(db_url=LOCAL_DB_URL)

runner = Runner(
    agent=root_agent,
    app_name="StoryTeller",
    session_service=session_service,
    artifact_service=gcs_service_py,
)
