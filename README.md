# Spicy AI Video Generator API Examples with Muapi

Compare the spicy AI video generator endpoints on Muapi — relaxed-moderation tiers of Seedance 2.5, Seedance 2, Wan 3.0, Wan 2.7/2.6/2.2 and MiniMax H3 — across text-to-video, image-to-video and reference-to-video, all behind one API key and one request format. This guide covers Muapi endpoints only; it does not document the upstream providers' direct APIs. Spicy tiers apply relaxed content moderation, but you remain responsible for complying with Muapi's [terms](https://muapi.ai/terms) and applicable law.

## Related Projects

- [MuAPI](https://muapi.ai) — Unified API for image, video, and audio generation across hundreds of AI models.
- [Seedance 2.5 Spicy API](https://github.com/Anil-matcha/Seedance-2.5-Spicy-API) — deeper guide to the Seedance 2.5 Spicy family.
- [Seedance 2 Spicy API](https://github.com/Anil-matcha/Seedance-2-Spicy-API) — Seedance 2 Spicy endpoints.
- [Wan 3.0 Spicy API](https://github.com/Anil-matcha/Wan-3.0-Spicy-API) — Wan 3.0 Spicy endpoints.
- [MiniMax H3 Spicy API](https://github.com/Anil-matcha/MiniMax-H3-Spicy-API) — full schemas for all eight MiniMax H3 Spicy endpoints.
- [Awesome Uncensored AI Video Models](https://github.com/Anil-matcha/awesome-uncensored-ai-video-models) — catalog of uncensored video models.
- [Spicy AI Image Generator API](https://github.com/Anil-matcha/Spicy-AI-Image-Generator-API) — the image-side companion to this guide.
- [AI Video API](https://github.com/Anil-matcha/AI-Video-API) — examples for video-generation APIs in general.
- [Image-to-Video API](https://github.com/Anil-matcha/Image-to-Video-API) — image-to-video endpoints compared.

## Overview

- [Spicy AI Video Generator landing page](https://muapi.ai/ai-spicy-video-generator)
- [Muapi API documentation](https://muapi.ai/docs/api-reference)
- [Video generation docs](https://muapi.ai/docs/video-generation)
- [Create or manage an API key](https://muapi.ai/access-keys)

Requests go to `https://api.muapi.ai/api/v1/{endpoint}` with an `x-api-key` header. A submission returns a `request_id`; poll `GET /api/v1/predictions/{request_id}/result` until the task is completed. Generated video URLs are returned in the result.

## Endpoint comparison

| Model family | Workflow | Muapi endpoint | Resolutions | Listed price |
|---|---|---|---|---|
| Seedance 2.5 Spicy | Text-to-video | `seedance-2.5-spicy-text-to-video` | 480p, 720p, 1080p, 4k | $0.187–$1.87 / sec |
| Seedance 2.5 Spicy | Image-to-video | `seedance-2.5-spicy-image-to-video` | 480p, 720p, 1080p, 4k | $0.187–$1.87 / sec |
| Seedance 2 Spicy | Text-to-video | `seedance-2-spicy-text-to-video` | 720p, 1080p, 4k | see playground page |
| Seedance 2 Spicy | Image-to-video | `seedance-2-spicy-image-to-video` | 720p, 1080p, 4k | see playground page |
| Wan 3.0 Spicy | Text-to-video | `wan3.0-spicy-text-to-video` | 480p, 720p, 1080p | see playground page |
| Wan 3.0 Spicy | Image-to-video | `wan3.0-spicy-image-to-video` | 480p, 720p, 1080p | see playground page |
| Wan 2.7 Spicy | Image-to-video | `wan2.7-image-to-video-spicy` | 720p, 1080p | see playground page |
| Wan 2.6 Spicy | Image-to-video | `wan2.6-image-to-video-spicy` | 720p, 1080p | see playground page |
| Wan 2.2 Spicy | Image-to-video | `wan2.2-spicy-image-to-video` | 480p, 720p | from $0.20 |
| MiniMax H3 Spicy | Text-to-video | `minimax-h3-text-to-video-spicy` | 480p, 768p, 2K | $0.058–$0.161 / sec |
| MiniMax H3 Spicy | Image-to-video | `minimax-h3-image-to-video-spicy` | 480p, 768p, 2K | $0.058–$0.161 / sec |
| MiniMax H3 Max Spicy | Text-to-video | `minimax-h3-max-spicy-text-to-video` | 480p, 768p | $0.0575–$0.092 / sec |
| MiniMax H3 Max Spicy | Image-to-video | `minimax-h3-max-spicy-image-to-video` | 480p, 768p | $0.0575–$0.092 / sec |
| MiniMax H3 Max Turbo Spicy | Text-to-video | `minimax-h3-max-turbo-spicy-text-to-video` | 480p, 768p | $0.0288–$0.046 / sec |
| MiniMax H3 Max Turbo Spicy | Image-to-video | `minimax-h3-max-turbo-spicy-image-to-video` | 480p, 768p | $0.0288–$0.046 / sec |
| MiniMax H3 Spicy | Reference-to-video | `minimax-h3-reference-to-video-spicy` | 480p, 768p, 2K | from $0.058 / sec |
| MiniMax H3 Max Spicy | Reference-to-video | `minimax-h3-max-spicy-reference-to-video` | 480p, 768p | from $0.0575 / sec |

Prices are Muapi catalog values as listed on the landing page at the time of writing, not upstream provider rates, and can change. Confirm the current price on the endpoint's playground page before estimating production cost. This table lists the primary text-to-video, image-to-video and MiniMax reference-to-video endpoints; the other families also have extra endpoints (reference-to-video, first/last frame, video edit and extend, 480p/1080p/4k resolution-specific variants) covered in the family repos above.

## Request schemas

Required fields are marked with `*`. All values below come from Muapi's endpoint schemas.

| Endpoint | Fields |
|---|---|
| `seedance-2.5-spicy-text-to-video` | `prompt`*, `aspect_ratio` (`adaptive`, `16:9`, `9:16`, `1:1`, `3:4`, `4:3`, `21:9`; default `16:9`), `resolution` (default `720p`), `duration` (default 5), `generate_audio` (default true), `camera_fixed`, `high_bitrate`, `draft`, `draft_request_id` |
| `seedance-2.5-spicy-image-to-video` | `prompt`*, `image_url`*, `last_image`, `resolution` (default `720p`), `duration` (default 5), `generate_audio`, `camera_fixed`, `high_bitrate`, `draft`, `draft_request_id` |
| `seedance-2-spicy-text-to-video` | `prompt`*, `resolution` (default `720p`), `aspect_ratio` (`21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`), `duration` (default 5), `high_bitrate` |
| `seedance-2-spicy-image-to-video` | `prompt`*, `images_list`* (up to 2 URLs), `resolution`, `aspect_ratio`, `duration`, `high_bitrate` |
| `wan3.0-spicy-text-to-video` | `prompt`*, `resolution` (default `720p`), `aspect_ratio` (`adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`), `duration` (default 5), `thinking_mode`, `enable_audio` (default true), `seed` |
| `wan3.0-spicy-image-to-video` | `prompt`*, `image_url`*, `last_image`, plus the same options as Wan 3.0 text-to-video |
| `wan2.7-image-to-video-spicy` / `wan2.6-image-to-video-spicy` | `image_url`*, `prompt`, `negative_prompt`, `audio_url`, `resolution` (`720p`/`1080p`), `duration` (5, 10 or 15), `shot_type` (`single`/`multi`), `enable_prompt_expansion`, `seed` |
| `wan2.2-spicy-image-to-video` | `prompt`*, `image_url`*, `resolution` (`480p`/`720p`), `duration` (5 or 8) |
| MiniMax H3 Spicy endpoints (all 8) | Text, image and reference-to-video across the H3, H3 Max and H3 Max Turbo tiers. Reference-to-video takes `prompt`* plus `reference_images` (up to 9), `reference_videos` (up to 3) and `reference_audios` (up to 3, not usable alone); see the [MiniMax H3 Spicy API repo](https://github.com/Anil-matcha/MiniMax-H3-Spicy-API) for the complete per-tier schemas |

Notes:

- Image-to-video field names differ between families: Seedance 2.5 and Wan 3.0 take a single `image_url` (with optional `last_image` as the end frame), Seedance 2 takes an `images_list` array, and the Wan 2.6/2.7 endpoints require `image_url` with an optional prompt. Do not copy payloads between endpoints unchanged.
- Seedance 2.5 Spicy supports a `draft` mode that you can reference later with `draft_request_id`.
- Seedance 2 Spicy does not list 480p; Seedance 2.5 Spicy does.

## Choosing an endpoint

1. **Input you have:** a prompt only (text-to-video), a still to animate (image-to-video), or reusable subject/style/motion assets (MiniMax reference-to-video). Wan 2.6, 2.7 and 2.2 are image-to-video only here.
2. **Resolution needs:** only Seedance 2.5 Spicy reaches 4k alongside Seedance 2 Spicy; MiniMax H3 Spicy offers 2K; Wan 3.0 reaches 1080p; Wan 2.2 stops at 720p.
3. **Audio:** Seedance 2.5 Spicy (`generate_audio`) and Wan 3.0 Spicy (`enable_audio`) expose audio toggles; Wan 2.6/2.7 accept an `audio_url`.
4. **Cost and speed:** MiniMax H3 Max Turbo Spicy and Wan 2.2 Spicy are the low-cost, fast options; Seedance 2.5 Spicy scales cost with resolution.
5. **Evaluate on your own prompts.** This repo makes no quality or benchmark claims; compare motion, prompt adherence and audio on representative samples before committing to a model.
6. **Failure handling:** submissions are asynchronous. Poll and handle both completed and failed statuses explicitly.

## Quick start with cURL

```bash
export MUAPI_API_KEY="your-api-key"
```

Text-to-video on Seedance 2.5 Spicy:

```bash
curl -X POST "https://api.muapi.ai/api/v1/seedance-2.5-spicy-text-to-video" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"A high-contrast fashion film in a rain-soaked neon city","aspect_ratio":"16:9","resolution":"720p","duration":5,"generate_audio":true}'
```

Image-to-video on Wan 3.0 Spicy:

```bash
curl -X POST "https://api.muapi.ai/api/v1/wan3.0-spicy-image-to-video" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"image_url":"https://example.com/first-frame.jpg","prompt":"The camera slowly pushes in as wind moves her hair","resolution":"720p","duration":5}'
```

Each call returns `{"request_id":"REQUEST_ID"}`. Poll it:

```bash
curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: ${MUAPI_API_KEY}"
```

## Python example

Requires Python 3.9+ and `requests`:

```bash
python -m pip install -r requirements.txt
export MUAPI_API_KEY="your-api-key"
python examples/submit.py seedance25-t2v
```

`examples/submit.py` submits one of several preconfigured jobs, polls until a terminal status, and prints the result. Replace the placeholder image URL before running an image-to-video job.

## Links

- Landing page: <https://muapi.ai/ai-spicy-video-generator>
- API reference: <https://muapi.ai/docs/api-reference>
- API keys: <https://muapi.ai/access-keys>

## License

MIT
