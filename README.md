\# Lobster Edge Nexus



Lobster Edge Nexus 是一個專為「極致隱私」與「大規模非結構化數據」設計的分散式多模態向量檢索系統。本專案旨在將邊緣運算的效能發揮至極致，實現完全不依賴雲端的在地化 AI 智能中樞。



\## 核心技術架構

\- \*\*Vector Database:\*\* Qdrant (HNSW Indexing)

\- \*\*LLM Engine:\*\* Llama-3-70B (via vLLM / Ollama)

\- \*\*Embedding Model:\*\* Multimodal-CLIP / Whisper-v3

\- \*\*Data Security:\*\* AES-256 Vault-layer Encryption



\## 為什麼選擇 HP ZGX Nano?

本專案在研發過程中面臨嚴重的 \*\*記憶體瓶頸\*\*：

1\. \*\*128GB 統一記憶體需求：\*\* 百萬級別的高維度向量索引 (1536-dim) 需完全駐留於記憶體中以達成 <30ms 的檢索延遲。

2\. \*\*Blackwell 算力壓榨：\*\* 需要 1,000 TOPS 的算力支撐即時的多模態嵌入 (Embedding) 與全精度 LLM 推理，解決目前消費級硬體在並發處理時的 Swap 延遲問題。



\## 測試計畫 (Roadmap)

\- \[ ] \*\*Phase 1:\*\* 部署 Qdrant 容器並進行百萬級數據載入壓測。

\- \[ ] \*\*Phase 2:\*\* 驗證 Llama-3-70B 在 ZGX Nano 上的推理 TPS 表現。

\- \[ ] \*\*Phase 3:\*\* 優化 Vault 加密層與 AI 運算層的 I/O 調度。



\## 免責聲明與隱私

本專案僅用於學術研究與個人數位資產管理，所有數據處理流程均遵循在地化原則，確保用戶數據絕對安全。

