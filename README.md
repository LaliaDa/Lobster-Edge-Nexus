\# Lobster-Edge-Nexus



\*\*High-Performance Privacy-Centric Distributed Vector Search Engine\*\*



Lobster-Edge-Nexus 是一套專為邊緣運算環境設計的數據中樞，旨在利用極致的硬體性能實現大規模非結構化數據的在地化語義檢索。



\## 🚀 專案願景 (Project Vision)

在不依賴雲端算力的前提下，透過 \*\*HP ZGX Nano (NVIDIA Blackwell)\*\* 的強大算力與 \*\*128GB 統一記憶體\*\*，構建一個具備毫秒級響應速度的「私有數位資產保險箱」。



\## 🛠 技術棧 (Tech Stack)

\- \*\*Vector Engine:\*\* Qdrant (Targeting 1M+ Vector Indexing)

\- \*\*Inference Frame:\*\* vLLM / Ollama (Optimized for Blackwell Architecture)

\- \*\*LLM Backbone:\*\* Llama-3-70B (Full-precision/Quantized testing)

\- \*\*Data Security:\*\* AES-256 AES-NI accelerated encryption layer



\## 📈 為什麼需要 HP ZGX Nano? (Hardware Requirement)

本專案的測試核心在於解決 \*\*記憶體與算力的非對稱性\*\*：

1\. \*\*Memory Density:\*\* 處理百萬級 1536-dim 向量時，傳統 24GB/64GB 環境會因 Swap 導致推理延遲。128GB LPDDR5x 統一記憶體可支持模型權重與向量索引全量駐留。

2\. \*\*Compute Throughput:\*\* 1,000 TOPS (FP4) 算力將用於壓測並發多模態 Embedding 處理，這是實現「即時資產索引」的關鍵。



\## 📊 測試指標 (Target KPI)

\- \*\*Indexing Speed:\*\* > 5,000 items/sec (Multimodal embedding)

\- \*\*Query Latency:\*\* < 30ms for 1M+ vector database

\- \*\*Inference Speed:\*\* > 15 tokens/sec for Llama-3-70B (INT8)



---

\*This project is currently being prepared for the HP AI Innovation Challenge.\*

## 📝 Change Log
- **2026-02-25:** Added `hardware_monitor.py` for VRAM tracking.
- **2026-02-25:** Optimized `quantization_params.yaml` for Blackwell architecture.
- **Next Step:** Implementing HNSW index pre-loading logic.
- **2026-02-26:** Implemented distributed vector sharding logic (distributed_engine.py).
