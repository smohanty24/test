import json
import sys
from urllib import request as req


class TeamsWebhookException(Exception):
    pass


#WEBHOOK_URL = "https://myco.webhook.office.com/webhookb2/abc-def-ghi/IncomingWebhook/blahblah42/jkl-mno"
WEBHOOK_URL="https://microfocusinternational.webhook.office.com/webhookb2/c8d46fc0-fae0-4b82-a3f5-9bd09ed0c1f4@856b813c-16e5-49a5-85ec-6f081e13b527/IncomingWebhook/380e1a9bd22d40fcbd077cd9aad14675/a9c961e2-e338-4206-8137-aaa82cb4a497"

def post_message(message: str) -> None:
    request = req.Request(url=WEBHOOK_URL, method="POST")
    request.add_header(key="Content-Type", val="application/json")
    data = json.dumps({"text": message}).encode()
    with req.urlopen(url=request, data=data) as response:
        if response.status != 200:
            raise TeamsWebhookException(response.reason)

if __name__ == "__main__":
    post_message("Time for dinner")