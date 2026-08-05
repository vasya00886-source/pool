# 🚀 ARKADY STUDIO

> Autonomous AI Coding Agent Studio — hybrid of JCode + ZCode + Ollama

## Что это

ARKADY STUDIO — автономная студия ИИ-агентов для кодинга. Объединяет лучшие черты JCode (локальная память, swarm), ZCode (плагины, UI) и Ollama (приватность, multimodal).

## Архитектура (7 слоёв)

| Слой | Файл | Что делает |
|------|------|-----------|
| **Router** | arkady_router.py | Privacy routing, fallback cascade, cost estimation |
| **Memory** | arkady_memory.py | SQLite сессии + skills library |
| **Plugins** | arkady_plugins.py | Hook bus (PreModelInit, SessionStart, ToolCall) |
| **Security** | arkady_security.py | Keyring, log rotation, secret detection |
| **Token Saver** | token_saver.py | Semantic cache + local routing (-70-85% cloud tokens) |
| **TUI** | arkady_studio.py | Rich terminal UI + 3D visualization |
| **Importer** | session_importer.py | ZCode/JCode/Ollama dialogue migration |

## Возможности

### ✅ ПЛЮСЫ (от каждой системы)
- **От JCode:** Локальный ONNX эмбеддер, behavioral mapping, swarm сессии, hotkeys
- **От ZCode:** Plugin marketplace, SQLite, hook events, remote control, skills
- **От Ollama:** Локальный GGUF runtime, capabilities, FIM-insert, Modelfile, vision

### ✅ ДОБАВЛЕНО (нет ни у одной)
- Privacy-aware routing (//private → local)
- Token/cost dashboard
- Semantic caching (-60% cloud)
- Context compression (-70% tokens)
- Config schema validation
- Sandboxed tool execution (planned)

### ❌ Чего НЕТ (решения минусов)
- ❌ Ключи в открытом виде → ✅ OS keyring (security layer)
- ❌ Мусор в конфигах → ✅ Schema validation
- ❌ Логи без лимита → ✅ RotatingFileHandler
- ❌ Зависимость от облака → ✅ Local-first routing

## Поддержка языков (RAG: 15000+ примеров)

| Язык | Примеров | Уровень |
|------|---------|---------|
| JavaScript | 4125 | Эксперт |
| Bash | 2065 | Эксперт |
| C++ | 1835 | Эксперт |
| SQL | 1260 | Эксперт |
| Java | 761 | Продвинутый |
| Rust | 748 | Продвинутый |
| Python | 522 | Продвинутый |
| Go | 336 | Базовый |

## Технологии агентов (10)

1. Reusable Skills (-50% генераций)
2. TT-SI Test-Time Self-Improvement (+5.5%)
3. MOSS Self-Rewriting
4. Self-Awareness
5. Curiosity Driver
6. Agent Roles (Alpha лидер / Beta помощник)
7. RAG + Vector Search (SemDeDup)
8. Reflection Loop
9. Self-Consistency (3 генерации)
10. DiskCache

## LoRA модель

- Базовая: Qwen2.5-Coder-7B-Instruct
- LoRA: rank=16, 3114 примеров, loss 0.23
- GGUF: Q4_K_M (4.7 GB)
- Docstrings на русском, type hints

## Multi-provider

- Ollama (локально, arkady-coder-7b)
- Groq (Llama 3.3 70B, бесплатно)
- OpenRouter (550B Nemotron, бесплатно)
- Cerebras (GPT-OSS 120B, бесплатно)

## Запуск

```bash
python arkady_main.py
```

Или `ArkadyStudio.exe` (3.2 GB, без Python)

## Лицензия

Proprietary — разработано Антоном и агентами Alpha/Beta
