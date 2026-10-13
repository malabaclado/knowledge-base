[pewdiepie-archdaemon/odysseus: Self-hosted AI workspace.](https://github.com/pewdiepie-archdaemon/odysseus)
[open-webui/open-webui: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)](https://github.com/open-webui/open-webui)


[How to Run LLMs Locally with Ollama in 11 Steps [2026]](https://tech-insider.org/ollama-tutorial-run-llm-locally-2026/)
[Msaleemakhtar/Local-LLM-Deployment-with-Ollama-and-OpenWebUI](https://github.com/Msaleemakhtar/Local-LLM-Deployment-with-Ollama-and-OpenWebUI)


ollama commands

`ollama list` - list down downloaded models
`ollama run [model]` downloads model locally


# OpenVino

docker command for windows
```
docker run -d --rm -p 8000:8000 -v "${PWD}/models:/models:rw" openvino/model_server:latest-gpu --source_model OpenVINO/Qwen3-8B-int4-ov --model_repository_path models --task text_generation --rest_port 8000 --target_device GPU
```
