# LiteLLM Proxy
https://docs.litellm.ai/docs/proxy/docker_quick_start

https://docs.litellm.ai/docs/providers/gemini

```
$ uv run prisma generate
$ uv run litellm --config ./config.yaml --detailed_debug
```

## 動作確認

```
$ curl -X POST 'http://localhost:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-super-secret-master-key' \
-d '{
    "model": "gemini-2.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "日本で一番高い山は？"
      }
    ]
}'
```

## 参考情報
- schema.prisma: [litellmのドキュメント](https://docs.litellm.ai/docs/proxy/deploy#build-from-litellm-pip-package)によると必要らしいので取ってきた
