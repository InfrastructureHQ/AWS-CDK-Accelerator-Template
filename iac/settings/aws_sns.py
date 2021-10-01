from typing import Dict, Optional

import pydantic

from settings.globalsettings import GlobalSettings

globalsettings = GlobalSettings()

AWS_ACCOUNT_ID = globalsettings.AWS_ACCOUNT_ID
AWS_REGION = globalsettings.AWS_REGION


class SNSSettings(
    pydantic.BaseSettings
):  # pylint: disable=too-few-public-methods

    stack_name: str = "APIStack"
    description: Optional[str] = "API Stack"
    aws_default_region = "us-east-1"
    stage: str = "production"
    email: Optional[str] = "<INSERT_VALUE>"
    cost_center: Optional[str]
    api_name: Optional[str] = "<INSERT_VALUE>"
    api_version: Optional[str] = "<INSERT_VALUE>"
