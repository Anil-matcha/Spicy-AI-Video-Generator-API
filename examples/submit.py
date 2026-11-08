"""Submit and poll a spicy video endpoint through Muapi.

Usage:
    export MUAPI_API_KEY="your-api-key"
    python examples/submit.py seedance25-t2v
    python examples/submit.py wan30-i2v
"""

import os
import sys
import time

import requests

BASE = "https://api.muapi.ai/api/v1"
TERMINAL = {"completed", "succeeded", "success", "failed", "error", "cancelled"}

T2V_PROMPT = "A high-contrast fashion film in a rain-soaked neon city"
I2V_PROMPT = "The camera slowly pushes in as wind moves her hair"
IMAGE = "https://example.com/first-frame.jpg"  # replace with a public image URL

JOBS = {
    "seedance25-t2v": ("seedance-2.5-spicy-text-to-video",
                       {"prompt": T2V_PROMPT, "aspect_ratio": "16:9", "resolution": "720p", "duration": 5, "generate_audio": True}),
    "seedance25-i2v": ("seedance-2.5-spicy-image-to-video",
                       {"prompt": I2V_PROMPT, "image_url": IMAGE, "resolution": "720p", "duration": 5, "generate_audio": True}),
    "seedance2-t2v": ("seedance-2-spicy-text-to-video",
                      {"prompt": T2V_PROMPT, "aspect_ratio": "16:9", "resolution": "720p", "duration": 5}),
    "seedance2-i2v": ("seedance-2-spicy-image-to-video",
                      {"prompt": I2V_PROMPT, "images_list": [IMAGE], "resolution": "720p", "duration": 5}),
    "wan30-t2v": ("wan3.0-spicy-text-to-video",
                  {"prompt": T2V_PROMPT, "aspect_ratio": "16:9", "resolution": "720p", "duration": 5}),
    "wan30-i2v": ("wan3.0-spicy-image-to-video",
                  {"prompt": I2V_PROMPT, "image_url": IMAGE, "resolution": "720p", "duration": 5}),
    "wan27-i2v": ("wan2.7-image-to-video-spicy",
                  {"prompt": I2V_PROMPT, "image_url": IMAGE, "resolution": "720p", "duration": 5}),
    "wan22-i2v": ("wan2.2-spicy-image-to-video",
                  {"prompt": I2V_PROMPT, "image_url": IMAGE, "resolution": "480p", "duration": 5}),
    "minimax-t2v": ("minimax-h3-text-to-video-spicy",
                    {"prompt": T2V_PROMPT, "aspect_ratio": "16:9", "resolution": "480p", "duration": 5}),
    "minimax-i2v": ("minimax-h3-image-to-video-spicy",
                    {"image_url": IMAGE, "prompt": I2V_PROMPT, "resolution": "480p", "duration": 5}),
    "minimax-ref": ("minimax-h3-reference-to-video-spicy",
                    {"prompt": "The character from the reference image walks through a rainy street at night",
                     "reference_images": [IMAGE], "resolution": "480p", "duration": 5}),
    "minimax-max-t2v": ("minimax-h3-max-spicy-text-to-video",
                        {"prompt": T2V_PROMPT, "aspect_ratio": "16:9", "resolution": "768p", "duration": 5}),
    "minimax-max-i2v": ("minimax-h3-max-spicy-image-to-video",
                        {"image_url": IMAGE, "prompt": I2V_PROMPT, "resolution": "768p", "duration": 5}),
    "minimax-max-ref": ("minimax-h3-max-spicy-reference-to-video",
                        {"prompt": "The character from the reference image walks through a rainy street at night",
                         "reference_images": [IMAGE], "resolution": "768p", "duration": 5}),
    "minimax-turbo-t2v": ("minimax-h3-max-turbo-spicy-text-to-video",
                          {"prompt": T2V_PROMPT, "aspect_ratio": "16:9", "resolution": "480p", "duration": 5}),
    "minimax-turbo-i2v": ("minimax-h3-max-turbo-spicy-image-to-video",
                          {"image_url": IMAGE, "prompt": I2V_PROMPT, "resolution": "480p", "duration": 5}),
}


def main():
    api_key = os.environ.get("MUAPI_API_KEY")
    if not api_key:
        sys.exit("Set MUAPI_API_KEY first.")
    if len(sys.argv) != 2 or sys.argv[1] not in JOBS:
        sys.exit("Usage: python examples/submit.py {" + "|".join(JOBS) + "}")

    endpoint, payload = JOBS[sys.argv[1]]
    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    resp = requests.post(f"{BASE}/{endpoint}", headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    request_id = resp.json()["request_id"]
    print(f"Submitted {endpoint}: request_id={request_id}")

    for _ in range(120):
        result = requests.get(f"{BASE}/predictions/{request_id}/result", headers=headers, timeout=60)
        result.raise_for_status()
        body = result.json()
        status = str(body.get("status", "")).lower()
        print(f"status={status}")
        if status in TERMINAL:
            print(body)
            return
        time.sleep(5)
    sys.exit("Timed out waiting for the result; poll the request_id again later.")


if __name__ == "__main__":
    main()
