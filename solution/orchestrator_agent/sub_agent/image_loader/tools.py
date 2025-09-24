from google.cloud import storage
import logging

from google.adk.tools.tool_context import ToolContext
from google.genai.types import Part


def get_image_bytes_from_gcs(gcs_uri: str) -> bytes | None:
    """Downloads an image from a Google Cloud Storage URI and returns its bytes.

    Args:
        gcs_uri: The Google Cloud Storage URI of the image
                 (e.g., 'gs://bucket-name/path/to/image.jpg').

    Returns:
        The image content as bytes, or None if the file cannot be downloaded.
    """
    if not gcs_uri.startswith("gs://"):
        logging.error("Invalid GCS URI. Must start with 'gs://'.")
        return None

    try:
        storage_client = storage.Client()
        bucket_name = gcs_uri.split("/")[2]
        blob_name = "/".join(gcs_uri.split("/")[3:])
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        image_bytes = blob.download_as_bytes()
        return image_bytes
    except Exception as e:
        logging.error(f"Failed to download image from {gcs_uri}: {e}")
        return None


async def load_image_data(tool_context: ToolContext, image_uri: str) -> dict:
    logger = logging.getLogger(__name__)
    logger.debug(f"Tool running: Getting image for '{image_uri}'...")

    try:
        image_bytes = get_image_bytes_from_gcs(image_uri)
        image_name = image_uri.replace("gs://", "").replace("/", "_")
        blob_part = Part.from_bytes(data=image_bytes, mime_type="image/png")

        try:
            res = await tool_context.save_artifact(
                filename=image_name, artifact=blob_part
            )
            return {"status": "success", "result": res}
        except Exception as e:
            error_message = f"Failed to save artifact: {e}"
            logger.error(error_message)
            return {"status": "error", "error_message": error_message}

    except ValueError as ve:
        logger.error(f"Configuration error: {ve}")
        return {"status": "error", "error_message": str(ve)}
